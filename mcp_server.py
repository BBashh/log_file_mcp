"""FastMCP Server for Log Analysis"""
from fastmcp import FastMCP
from log_analyzer import LogAnalyzer
from config import DEFAULT_LOG_DIR
from typing import Optional

# Initialize FastMCP server
mcp = FastMCP("log-analyzer")

@mcp.tool()
def read_logs(
    customPath: str = DEFAULT_LOG_DIR,
    filter: Optional[str] = None,
    lines: int = 100,
    fileLimit: int = 5,
    page: int = 1
) -> dict:
    """
    Read logs from a directory with optional filtering and pagination.
    
    Args:
        customPath: Path to log directory
        filter: Text to filter logs (case-insensitive)
        lines: Number of lines to read
        fileLimit: Max number of files to read
        page: Page number for pagination
    
    Returns:
        Dictionary with log entries and metadata
    """
    analyzer = LogAnalyzer(customPath)
    return analyzer.read_logs(filter, lines, fileLimit, page)

@mcp.tool()
def count_log_types(
    customPath: str = DEFAULT_LOG_DIR,
    logLevel: Optional[str] = None
) -> dict:
    """
    Count logs by severity level.
    
    Args:
        customPath: Path to log directory
        logLevel: Specific level to count (CRITICAL, ERROR, WARNING, INFO, DEBUG)
    
    Returns:
        Dictionary with counts and percentages
    """
    analyzer = LogAnalyzer(customPath)
    return analyzer.count_log_types(logLevel)

@mcp.tool()
def generate_statistics(
    customPath: str = DEFAULT_LOG_DIR,
    statsType: str = "summary"
) -> dict:
    """
    Generate log statistics.
    
    Args:
        customPath: Path to log directory
        statsType: 'summary', 'detailed', or 'anomalies'
    
    Returns:
        Dictionary with statistical analysis
    """
    analyzer = LogAnalyzer(customPath)
    return analyzer.generate_statistics(statsType)

@mcp.tool()
def extract_critical_logs(
    customPath: str = DEFAULT_LOG_DIR,
    severity: str = "CRITICAL",
    outputPath: Optional[str] = None
) -> dict:
    """
    Extract critical/error logs to a separate file.
    
    Args:
        customPath: Path to log directory
        severity: Log level to extract (CRITICAL, ERROR, WARNING)
        outputPath: Where to save extracted logs
    
    Returns:
        Dictionary with extracted log information
    """
    analyzer = LogAnalyzer(customPath)
    return analyzer.extract_critical_logs(severity, outputPath)

@mcp.tool()
def detect_anomalies(
    customPath: str = DEFAULT_LOG_DIR,
    anomalyType: str = "spike"
) -> dict:
    """
    Detect anomalies in logs.
    
    Args:
        customPath: Path to log directory
        anomalyType: Type of anomaly detection ('spike', 'pattern', 'missing')
    
    Returns:
        Dictionary with detected anomalies
    """
    analyzer = LogAnalyzer(customPath)
    return analyzer.detect_anomalies(anomalyType)

@mcp.tool()
def generate_report(
    customPath: str = DEFAULT_LOG_DIR,
    reportType: str = "summary",
    outputPath: Optional[str] = None
) -> dict:
    """
    Generate comprehensive log analysis report.
    
    Args:
        customPath: Path to log directory
        reportType: 'summary', 'detailed', or 'html'
        outputPath: Where to save the report
    
    Returns:
        Dictionary with report information and preview
    """
    analyzer = LogAnalyzer(customPath)
    return analyzer.generate_report(reportType, outputPath)

if __name__ == "__main__":
    import uvicorn
    # Run server with: python mcp_server.py
    # Or use: mcp run mcp_server:mcp
    print("Log Analyzer MCP Server starting...")
    mcp.run()
