"""Main log analysis module"""
from typing import List, Dict, Optional
from pathlib import Path
from utils.file_handler import FileHandler
from utils.statistics import StatisticsAnalyzer
from utils.report_generator import ReportGenerator
from config import LOG_LEVELS

class LogAnalyzer:
    def __init__(self, directory: str):
        self.directory = directory
        self.file_handler = FileHandler()
        self.stats_analyzer = StatisticsAnalyzer()

    def read_logs(
        self,
        filter_text: Optional[str] = None,
        lines: int = 100,
        file_limit: int = 5,
        page: int = 1
    ) -> Dict:
        """Read and optionally filter logs"""
        try:
            log_files = self.file_handler.get_log_files(self.directory, file_limit)
            
            if not log_files:
                return {"error": "No log files found"}
            
            all_lines = []
            for log_file in log_files:
                file_lines = self.file_handler.read_file(str(log_file), lines)
                all_lines.extend(file_lines)
            
            # Filter if specified
            if filter_text:
                filter_text = filter_text.upper()
                all_lines = [line for line in all_lines if filter_text in line.upper()]
            
            # Pagination
            page_size = 50
            start_idx = (page - 1) * page_size
            end_idx = start_idx + page_size
            paginated_lines = all_lines[start_idx:end_idx]
            
            return {
                "status": "success",
                "total_found": len(all_lines),
                "page": page,
                "lines": [line.strip() for line in paginated_lines],
                "files_read": [f.name for f in log_files],
                "filter_applied": filter_text or "None"
            }
        except Exception as e:
            return {"error": str(e)}

    def count_log_types(self, log_level: Optional[str] = None) -> Dict:
        """Count logs by severity level"""
        try:
            log_files = self.file_handler.get_log_files(self.directory)
            all_lines = []
            
            for log_file in log_files:
                all_lines.extend(self.file_handler.read_all_lines(str(log_file)))
            
            level_counts = self.stats_analyzer.analyze_log_levels(all_lines)
            
            if log_level:
                log_level = log_level.upper()
                return {
                    "status": "success",
                    "level": log_level,
                    "count": level_counts.get(log_level, 0),
                    "total_logs": len(all_lines)
                }
            
            total = sum(level_counts.values()) or 1
            return {
                "status": "success",
                "counts": level_counts,
                "total_logs": len(all_lines),
                "percentages": {
                    level: round((count / total) * 100, 2) 
                    for level, count in level_counts.items()
                }
            }
        except Exception as e:
            return {"error": str(e)}

    def generate_statistics(self, stats_type: str = "summary") -> Dict:
        """Generate comprehensive statistics"""
        try:
            log_files = self.file_handler.get_log_files(self.directory)
            all_lines = []
            
            for log_file in log_files:
                all_lines.extend(self.file_handler.read_all_lines(str(log_file)))
            
            stats = self.stats_analyzer.get_statistics(all_lines)
            
            if stats_type == "summary":
                return {
                    "status": "success",
                    "type": "summary",
                    "statistics": stats
                }
            elif stats_type == "detailed":
                patterns = self.stats_analyzer.find_common_patterns(all_lines)
                rare = self.stats_analyzer.find_rare_logs(all_lines)
                return {
                    "status": "success",
                    "type": "detailed",
                    "statistics": stats,
                    "common_patterns": patterns,
                    "rare_logs": rare
                }
            elif stats_type == "anomalies":
                spike = self.stats_analyzer.detect_spike(all_lines)
                return {
                    "status": "success",
                    "type": "anomalies",
                    "spike_detection": spike
                }
            else:
                return {"error": "Invalid stats type"}
        except Exception as e:
            return {"error": str(e)}

    def extract_critical_logs(
        self,
        severity: str = "CRITICAL",
        output_path: Optional[str] = None
    ) -> Dict:
        """Extract critical/error logs to separate file"""
        try:
            log_files = self.file_handler.get_log_files(self.directory)
            all_lines = []
            
            for log_file in log_files:
                all_lines.extend(self.file_handler.read_all_lines(str(log_file)))
            
            severity = severity.upper()
            critical_lines = [line for line in all_lines if severity in line]
            
            # Save to file if output path provided
            saved_path = None
            if output_path:
                self.file_handler.write_file(output_path, critical_lines)
                saved_path = output_path
            
            return {
                "status": "success",
                "severity": severity,
                "count": len(critical_lines),
                "logs": [line.strip() for line in critical_lines[:20]],  # First 20
                "saved_to": saved_path,
                "total_found": len(critical_lines)
            }
        except Exception as e:
            return {"error": str(e)}

    def detect_anomalies(self, anomaly_type: str = "spike") -> Dict:
        """Detect anomalies in logs"""
        try:
            log_files = self.file_handler.get_log_files(self.directory)
            all_lines = []
            
            for log_file in log_files:
                all_lines.extend(self.file_handler.read_all_lines(str(log_file)))
            
            if anomaly_type == "spike":
                result = self.stats_analyzer.detect_spike(all_lines)
            else:
                result = {"error": "Invalid anomaly type"}
            
            return {"status": "success", "anomalies": result}
        except Exception as e:
            return {"error": str(e)}

    def generate_report(
        self,
        report_type: str = "summary",
        output_path: Optional[str] = None
    ) -> Dict:
        """Generate analysis report"""
        try:
            log_files = self.file_handler.get_log_files(self.directory)
            all_lines = []
            
            for log_file in log_files:
                all_lines.extend(self.file_handler.read_all_lines(str(log_file)))
            
            log_levels = self.stats_analyzer.analyze_log_levels(all_lines)
            
            if report_type == "summary":
                report = ReportGenerator.generate_summary_report(
                    self.directory, all_lines, log_levels
                )
            elif report_type == "html":
                report = ReportGenerator.generate_html_report(
                    self.directory, all_lines, log_levels
                )
            else:
                return {"error": "Invalid report type"}
            
            # Save report if output path provided
            saved_path = None
            if output_path:
                with open(output_path, 'w') as f:
                    f.write(report)
                saved_path = output_path
            
            return {
                "status": "success",
                "report_type": report_type,
                "saved_to": saved_path,
                "report_preview": report[:500] + "..." if len(report) > 500 else report
            }
        except Exception as e:
            return {"error": str(e)}
