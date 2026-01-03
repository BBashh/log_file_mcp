# 📊 MCP Log Analyzer

An intelligent log file analyzer powered by Python and integrated with Cursor IDE through the Model Context Protocol (MCP).

## 🎯 What It Does

Analyzes log files instantly using AI-powered tools. Instead of manually searching through thousands of log lines, ask questions in natural language and get instant insights about errors, patterns, and anomalies.

### Before vs After

**Before (❌):**
- Manually open and search log files
- Hours of tedious analysis
- Error-prone manual work

**After (✅):**
- Ask Claude in natural language
- Get instant analysis in seconds
- Automatic pattern detection
- AI-powered insights

## 🛠️ Features

### 6 Analysis Tools

1. **read_logs** - Fetch and display log content
2. **count_log_types** - Count logs by severity (INFO, ERROR, WARNING, CRITICAL)
3. **generate_statistics** - Analyze patterns and detect anomalies
4. **extract_critical_logs** - Extract only critical issues
5. **detect_anomalies** - Find unusual activity and spikes
6. **generate_report** - Create formatted HTML/text reports


<p align="center">
  <img width="436" height="311"
       src="https://github.com/user-attachments/assets/bf30db06-7dd3-4379-9ee2-ede0c95e1770"
       alt="generate_report output preview">
</p>

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/BBashh/log_file_mcp.git
cd log_file_mcp
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

```bash
# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Test Locally
```bash
python mcp_server.py
# Should show: "Log Analyzer MCP Server starting..."
# Press Ctrl+C to stop
```

### 5. Configure Cursor IDE

Update your mcp.json file:

**Location:** C:\Users\[YourUsername]\AppData\Roaming\Cursor\User\settings\mcp.json

```json
{
  "mcpServers": {
    "log-analyzer": {
      "command": "[FULL_PATH_TO_VENV]\\venv\\Scripts\\python.exe",
      "args": ["[FULL_PATH_TO_PROJECT]\\mcp_server.py"]
    }
  }
}
```

### 6. Use in Cursor
- Restart Cursor IDE
- Look for green dot in Tools & MCP
- Ask questions in Cursor chat:
  - "Read logs from sample_logs"
  - "How many errors are there?"
  - "Generate a report"

## 🔧 Configuration

Edit \`config.py\` to customize:

```python
DEFAULT_LOG_DIR = "C:\\path\\to\\logs"  # Your log directory
LOG_LEVELS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]
STATS_CONFIG = {
    "min_line_length": 5,
    "max_line_length": 1000,
    "rare_threshold": 0.01,
}
```

## 📝 Usage Examples

### In Cursor Chat:

If the chat is giving responses without using the mcp tool, then explicitly mention in the chat to use the xyz tool.

Ex:

**Read logs:**
```txt
Read the logs from sample_logs and show me the last 10 lines using the read_logs mcp tool
```

**Count by type:**
```txt
How many INFO, WARNING, and ERROR logs are there using `xyz` tool?
```

**Get statistics:**
```txt
Analyze the logs for patterns and anomalies using `xyz` tool
```

**Extract critical:**
```txt
Show me all critical logs only using `xyz` tool
```

**Generate report:**
```txt
Create a comprehensive analysis report of the logs using `xyz` tool.
```

Ex:

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/c5ba0094-0c8b-46de-865e-ff758474d43e"
    alt="generate_report example output"
    width="583"
    height="663"
  />
</p>


## 🏛️ Technical Details

### Technologies
- **FastMCP** - MCP server framework
- **Python 3.x** - Programming language
- **Cursor IDE** - IDE integration
- **JSON-RPC** - Communication protocol

### Design Patterns
- **MVC Pattern** - Separation of concerns
- **Factory Pattern** - Tool creation
- **Observer Pattern** - Event handling
- **Singleton Pattern** - Config management

### Key Features
- Modular architecture (easy to extend)
- Error handling and validation
- Configuration management
- Report generation (HTML/Text)
- Pattern detection
- Anomaly detection

## 🔐 Security Notes

- Server runs locally only (no internet exposure)
- Log files processed in memory
- No data stored externally
- Compatible with confidential logs


## 🐛 Troubleshooting

### Green dot not showing?
- Check mcp.json has correct paths
- Verify venv Python path is correct
- Restart Cursor completely

### "Module not found" error?
- Make sure venv is activated
- Run: pip install -r requirements.txt

### Tools not responding?
- Verify server running: python mcp_server.py
- Check sample_logs/sample.log exists
- Restart Cursor and try again
