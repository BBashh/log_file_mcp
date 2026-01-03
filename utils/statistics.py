"""Statistical analysis utilities"""
from typing import List, Dict, Tuple
from collections import Counter
import re
from datetime import datetime

class StatisticsAnalyzer:
    @staticmethod
    def analyze_log_levels(lines: List[str]) -> Dict[str, int]:
        """Count logs by severity level"""
        levels = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]
        counts = {level: 0 for level in levels}
        
        for line in lines:
            for level in levels:
                if f"[{level}]" in line or f"{level}" in line.upper():
                    counts[level] += 1
                    break
        
        return counts

    @staticmethod
    def get_statistics(lines: List[str]) -> Dict:
        """Generate comprehensive statistics"""
        if not lines:
            return {"error": "No logs found"}
        
        line_lengths = [len(line.strip()) for line in lines]
        
        return {
            "total_lines": len(lines),
            "min_length": min(line_lengths) if line_lengths else 0,
            "max_length": max(line_lengths) if line_lengths else 0,
            "avg_length": sum(line_lengths) / len(line_lengths) if line_lengths else 0,
            "non_empty_lines": len([l for l in lines if l.strip()]),
        }

    @staticmethod
    def find_common_patterns(lines: List[str], top_n: int = 5) -> List[Tuple[str, int]]:
        """Find most common error messages"""
        # Extract error/warning messages
        patterns = []
        for line in lines:
            if "ERROR" in line or "WARNING" in line:
                # Extract message after level indicator
                match = re.search(r'\[(ERROR|WARNING)\]\s*(.+?)(?:\s|$)', line)
                if match:
                    patterns.append(match.group(2)[:50])  # First 50 chars
        
        # Count and return top N
        counter = Counter(patterns)
        return counter.most_common(top_n)

    @staticmethod
    def find_rare_logs(lines: List[str], threshold: float = 0.01) -> List[str]:
        """Find rare/unusual log entries"""
        # Simple heuristic: very long lines or unusual patterns
        rare = []
        avg_length = sum(len(l) for l in lines) / len(lines) if lines else 0
        
        for line in lines:
            if len(line) > avg_length * 2:  # 2x average length
                rare.append(line.strip())
        
        return rare[:10]  # Return top 10

    @staticmethod
    def detect_spike(lines: List[str], window_size: int = 10) -> Dict:
        """Detect sudden spikes in ERROR/CRITICAL logs"""
        errors = [line for line in lines if "ERROR" in line or "CRITICAL" in line]
        
        if len(errors) < window_size:
            return {"spikes_detected": 0, "message": "Not enough errors to detect spikes"}
        
        # Simple spike detection: compare moving averages
        first_half = errors[:len(errors)//2]
        second_half = errors[len(errors)//2:]
        
        first_avg = len(first_half) / (len(errors)//2) if len(errors)//2 > 0 else 0
        second_avg = len(second_half) / (len(errors) - len(errors)//2) if len(errors) - len(errors)//2 > 0 else 0
        
        spike_detected = second_avg > first_avg * 1.5
        
        return {
            "spike_detected": spike_detected,
            "first_half_errors": len(first_half),
            "second_half_errors": len(second_half),
            "increase_percentage": ((second_avg - first_avg) / (first_avg + 0.1)) * 100 if first_avg > 0 else 0
        }
