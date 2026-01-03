"""Configuration settings for MCP Log Analyzer"""
from pathlib import Path

# Default log directory
DEFAULT_LOG_DIR = str(Path.home() / "AppData" / "Roaming" / "Cursor" / "logs")

# Log levels
LOG_LEVELS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]

# Supported log formats
LOG_FORMATS = [".log", ".txt"]

# Statistics
STATS_CONFIG = {
    "min_line_length": 5,
    "max_line_length": 1000,
    "rare_threshold": 0.01,  # 1% of logs
}

# Report settings
REPORT_CONFIG = {
    "include_timestamp": True,
    "include_statistics": True,
    "include_anomalies": True,
}
