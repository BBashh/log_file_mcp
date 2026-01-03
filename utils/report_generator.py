"""Report generation utilities"""
from typing import List, Dict
from datetime import datetime
from utils.statistics import StatisticsAnalyzer

class ReportGenerator:
    @staticmethod
    def generate_summary_report(
        directory: str,
        lines: List[str],
        log_levels: Dict[str, int]
    ) -> str:
        """Generate summary report"""
        stats = StatisticsAnalyzer.get_statistics(lines)
        patterns = StatisticsAnalyzer.find_common_patterns(lines, top_n=5)
        
        report = []
        report.append("=" * 60)
        report.append("LOG ANALYSIS REPORT")
        report.append("=" * 60)
        report.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Log Directory: {directory}\n")
        
        # Statistics
        report.append("STATISTICS:")
        report.append(f"  Total Lines: {stats['total_lines']}")
        report.append(f"  Non-Empty Lines: {stats['non_empty_lines']}")
        report.append(f"  Min Length: {stats['min_length']}")
        report.append(f"  Max Length: {stats['max_length']}")
        report.append(f"  Avg Length: {stats['avg_length']:.2f}\n")
        
        # Log Levels
        report.append("LOG LEVELS:")
        for level, count in log_levels.items():
            if count > 0:
                percentage = (count / stats['total_lines']) * 100 if stats['total_lines'] > 0 else 0
                report.append(f"  {level}: {count} ({percentage:.1f}%)")
        
        # Common Patterns
        if patterns:
            report.append("\nMOST COMMON ERRORS:")
            for i, (pattern, count) in enumerate(patterns, 1):
                report.append(f"  {i}. {pattern} (x{count})")
        
        report.append("\n" + "=" * 60)
        
        return "\n".join(report)

    @staticmethod
    def generate_html_report(
        directory: str,
        lines: List[str],
        log_levels: Dict[str, int]
    ) -> str:
        """Generate HTML report"""
        stats = StatisticsAnalyzer.get_statistics(lines)
        
        html = []
        html.append("<!DOCTYPE html>")
        html.append("<html>")
        html.append("<head>")
        html.append("<title>Log Analysis Report</title>")
        html.append("<style>")
        html.append("body { font-family: Arial; margin: 20px; }")
        html.append("table { border-collapse: collapse; width: 100%; }")
        html.append("th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }")
        html.append("th { background-color: #4CAF50; color: white; }")
        html.append("</style>")
        html.append("</head>")
        html.append("<body>")
        
        html.append(f"<h1>Log Analysis Report</h1>")
        html.append(f"<p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>")
        html.append(f"<p>Directory: {directory}</p>")
        
        html.append("<h2>Statistics</h2>")
        html.append("<table>")
        html.append("<tr><th>Metric</th><th>Value</th></tr>")
        html.append(f"<tr><td>Total Lines</td><td>{stats['total_lines']}</td></tr>")
        html.append(f"<tr><td>Average Length</td><td>{stats['avg_length']:.2f}</td></tr>")
        html.append("</table>")
        
        html.append("<h2>Log Levels</h2>")
        html.append("<table>")
        html.append("<tr><th>Level</th><th>Count</th></tr>")
        for level, count in log_levels.items():
            if count > 0:
                html.append(f"<tr><td>{level}</td><td>{count}</td></tr>")
        html.append("</table>")
        
        html.append("</body>")
        html.append("</html>")
        
        return "\n".join(html)
