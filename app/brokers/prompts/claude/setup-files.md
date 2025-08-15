# CrewAI Data Broker Agent - Setup Guide

## Prerequisites

1. **Install Ollama**
   ```bash
   # Install Ollama (macOS/Linux)
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Or download from https://ollama.ai for Windows
   ```

2. **Pull Required Model**
   ```bash
   ollama pull llama3.1:8b
   # Or use a different model like:
   # ollama pull llama3.2:3b  (lighter)
   # ollama pull codellama:7b (code-focused)
   ```

## Installation Steps

### 1. Create Project Directory
```bash
mkdir data-broker-agent
cd data-broker-agent
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Create Requirements File
Create `requirements.txt`:
```txt
crewai==0.41.1
crewai-tools==0.4.26
ollama==0.1.7
requests==2.31.0
beautifulsoup4==4.12.2
selenium==4.15.2
python-dotenv==1.0.0
schedule==1.2.0
validators==0.22.0
whois==0.9.27
urllib3==2.0.7
lxml==4.9.3
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Create Environment Configuration
Create `.env` file:
```bash
# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1:8b

# Data Storage
DATA_FILE=data_brokers.json

# Logging
LOG_LEVEL=INFO

# Search Configuration
SEARCH_DELAY=2
MAX_RETRIES=3

# Optional: Add API keys if you want to use other search engines
# GOOGLE_API_KEY=your_key_here
# BING_API_KEY=your_key_here
```

### 6. Project Structure
```
data-broker-agent/
├── main.py                 # Main agent code
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables
├── data_brokers.json      # Database file (auto-created)
├── data_broker_agent.log  # Application logs
├── agent_runs.log         # Scheduled run logs
└── README.md              # This file
```

## Running the Agent

### 1. Start Ollama Server
```bash
ollama serve
```

### 2. Run the Agent
```bash
python main.py
```

The agent will present a menu with options:
- **Option 1**: Run discovery cycle once (great for testing)
- **Option 2**: Run continuous monitoring every 6 hours
- **Option 3**: View current database contents
- **Option 4**: Test individual tools
- **Option 5**: Exit

### 3. First Run Recommendations
1. Start with **Option 4** to test all tools work correctly
2. Then try **Option 1** to run a single discovery cycle
3. Check **Option 3** to see discovered brokers
4. Finally use **Option 2** for continuous monitoring

## Configuration Options

### Customizing Search Terms
Edit the discovery task in `main.py` to add your own search terms:
```python
# In discovery_task description, modify search terms:
"Search for terms like: 'data broker', 'people search', 'your custom term'"
```

### Adjusting Schedule
Change the monitoring frequency in the main function:
```python
# Current: every 6 hours
schedule.every(6).hours.do(run_scheduled_agent)

# Options:
schedule.every(30).minutes.do(run_scheduled_agent)  # Every 30 min
schedule.every().day.at("09:00").do(run_scheduled_agent)  # Daily at 9 AM
schedule.every().monday.do(run_scheduled_agent)  # Weekly on Monday
```

### Using Different Models
Update your `.env` file:
```bash
# For faster, lighter model:
OLLAMA_MODEL=llama3.2:3b

# For code-focused tasks:
OLLAMA_MODEL=codellama:7b

# For more capable model (requires more RAM):
OLLAMA_MODEL=llama3.1:70b
```

## Data Output Format

The agent stores discovered brokers in `data_brokers.json` with this structure:
```json
[
  {
    "name": "Example Data Broker",
    "url": "https://example.com",
    "category": "People search websites",
    "description": "Short summary of services",
    "country": "US",
    "regulations": ["GDPR", "CCPA"],
    "opt_out_url": "https://example.com/opt-out",
    "created_timestamp": "2024-12-19 10:30:00",
    "updated_timestamp": "2024-12-19 15:45:00",
    "last_crawled_timestamp": "2024-12-19 15:45:00",
    "last_categorised_timestamp": "2024-12-19 15:45:00",
    "last_monitored_status": "Success",
    "last_monitored_message": "Opt-out page accessible",
    "last_monitored_source": "Direct crawl",
    "last_monitored_timestamp": "2024-12-19 15:45:00",
    "last_monitored_duration": "00:00:15",
    "source": "DuckDuckGo search",
    "aliases": ["old-domain.com"],
    "notes": "Additional context about the broker"
  }
]
```

## Extending the Agent

### Adding New Search Sources
1. **Create new search method** in `WebSearchTool`:
```python
def _search_bing(self, query: str, num_results: int) -> List[Dict]:
    # Implement Bing search API
    pass
```

2. **Add to search execution**:
```python
# In WebSearchTool._run method:
bing_results = self._search_bing(query, num_results)
results.extend(bing_results)
```

### Adding New Categories
Update the `CategoryClassificationTool` with new categories:
```python
categories = {
    # Existing categories...
    "Your New Category": [
        "keyword1", "keyword2", "specific terms"
    ]
}
```

### Custom MCP Integration
To integrate with MCP servers, add this tool:
```python
class MCPTool(BaseTool):
    name: str = "mcp_search"
    description: str = "Search using MCP server"
    
    def _run(self, query: str) -> str:
        # Connect to your MCP server
        # Send search request
        # Return formatted results
        pass
```

## Troubleshooting

### Common Issues

**1. Ollama Connection Error**
```
Error: Failed to connect to Ollama
```
**Solution**: Make sure Ollama is running: `ollama serve`

**2. Model Not Found**
```
Error: Model not available
```
**Solution**: Pull the model: `ollama pull llama3.1:8b`

**3. Rate Limiting**
```
Error: Too many requests
```
**Solution**: Increase `SEARCH_DELAY` in `.env` file

**4. Permission Denied on Data File**
```
Error: Cannot write to data_brokers.json
```
**Solution**: Check file permissions and ensure directory is writable

### Performance Tips

1. **Use lighter models for testing**: `llama3.2:3b` instead of `llama3.1:8b`
2. **Increase search delays**: Set `SEARCH_DELAY=5` for slower but more reliable searches
3. **Run discovery less frequently**: Change schedule to daily instead of every 6 hours
4. **Limit search results**: Reduce `num_results` parameter in search calls

### Monitoring Performance

Check the logs for performance metrics:
```bash
# View main log
tail -f data_broker_agent.log

# View scheduled runs
tail -f agent_runs.log

# Check for errors
grep ERROR data_broker_agent.log
```

## Advanced Features

### Database Export
Add this function to export data to CSV:
```python
import csv
import json

def export_to_csv():
    with open('data_brokers.json', 'r') as f:
        data = json.load(f)
    
    with open('data_brokers.csv', 'w', newline='') as f:
        if data:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
```

### Custom Notifications
Add Slack/Discord notifications for new discoveries:
```python
import requests

def notify_new_broker(broker_data):
    webhook_url = "your_webhook_url"
    message = f"🔍 New data broker discovered: {broker_data['name']}"
    
    requests.post(webhook_url, json={"text": message})
```

### Analytics Dashboard
Create a simple web dashboard to view results:
```python
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    with open('data_brokers.json', 'r') as f:
        brokers = json.load(f)
    return render_template('dashboard.html', brokers=brokers)
```

## Security Considerations

1. **Rate Limiting**: Respect website rate limits to avoid being blocked
2. **User Agent**: Tool uses realistic user agent strings
3. **Delay Between Requests**: Built-in delays prevent aggressive scraping
4. **Error Handling**: Graceful failure handling to prevent crashes
5. **Data Privacy**: All data stored locally, no external services required

## Support and Updates

- **GitHub Issues**: Report bugs or request features
- **Documentation**: Check CrewAI docs for agent configuration options
- **Ollama Models**: Visit Ollama library for new model releases
- **Community**: Join CrewAI Discord for support

## License and Legal

- Ensure compliance with website terms of service when scraping
- Respect robots.txt files
- Use discovered information responsibly
- Consider data protection laws in your jurisdiction
- This tool is for research and privacy protection purposes

---

**Happy Data Broker Hunting! 🔍🛡️**