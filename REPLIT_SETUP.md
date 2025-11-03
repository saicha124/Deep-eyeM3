# Deep Eye - Replit Setup Guide

Welcome to Deep Eye on Replit! This security scanner has been configured to run in the Replit environment.

## ✅ What's Already Set Up

- ✅ Python 3.11 environment
- ✅ All required dependencies installed
- ✅ Configuration file created at `config/config.yaml`
- ✅ Required directories created (logs, reports, data)
- ✅ Workflow configured for easy access

## 🚀 Quick Start

### Option 1: Using the Console Workflow
The workflow is pre-configured to show the help menu. You can run scans directly from the Replit Shell:

```bash
# Show help
python deep_eye.py --help

# Show version
python deep_eye.py --version

# Run a basic scan (requires API key configuration)
python deep_eye.py -u https://example.com -v
```

### Option 2: Run Directly in Shell
You can execute any Deep Eye command in the Shell tab.

## 🔑 Configuration Required

**IMPORTANT**: Before running actual scans, you need to configure at least one AI provider API key.

### Setting Up API Keys

1. **Edit the config file**:
   - Open `config/config.yaml`
   - Add your API key(s) for at least one provider

2. **Available AI Providers**:
   
   **OpenAI (GPT-4)**
   - Get API key: https://platform.openai.com/api-keys
   - Update in config: `ai_providers.openai.api_key`
   
   **Claude (Anthropic)**
   - Get API key: https://console.anthropic.com/
   - Update in config: `ai_providers.claude.api_key`
   
   **Grok (xAI)**
   - Get API key: https://console.x.ai/
   - Update in config: `ai_providers.grok.api_key`
   
   **OLLAMA (Local - Not recommended for Replit)**
   - Requires local installation
   - Not suitable for cloud environments

### Recommended Setup for Replit

Edit `config/config.yaml`:

```yaml
ai_providers:
  openai:
    enabled: true
    api_key: "YOUR_OPENAI_KEY_HERE"  # Add your actual key
    model: "gpt-4o"

scanner:
  target_url: ""  # Leave empty or set default target
  ai_provider: "openai"  # or "claude" or "grok"
  default_depth: 2
  default_threads: 5
  enable_recon: false
  full_scan: false
```

## 📖 Usage Examples

### Basic Scan
```bash
python deep_eye.py -u https://example.com
```

### Verbose Scan
```bash
python deep_eye.py -u https://example.com -v
```

### Using Custom Config
```bash
python deep_eye.py -c myconfig.yaml
```

### All options are in config.yaml
All scanning options (depth, threads, scan mode, etc.) are configured in `config/config.yaml`. You only need to provide the target URL via CLI, or set it in the config file.

## 📁 Output Files

- **Reports**: `reports/` directory
  - HTML, PDF, or JSON formats
  - Auto-generated with timestamp
  
- **Logs**: `logs/deep_eye.log`
  - Detailed execution logs
  - Useful for debugging

## ⚠️ Important Notes

### Legal Disclaimer
**CRITICAL**: Only use Deep Eye on systems you own or have explicit written permission to test. Unauthorized security testing is illegal and unethical.

### Limitations in Replit
- No local OLLAMA support (cloud environment)
- Limited to scanning external targets
- Reports are stored temporarily (use Download option)

### Best Practices
1. Always get permission before scanning
2. Start with quick scans on test environments
3. Monitor your API usage/costs
4. Review reports in the `reports/` directory
5. Check logs if you encounter errors

## 🔧 Troubleshooting

### "API key not configured"
- Edit `config/config.yaml`
- Add valid API key for your chosen provider
- Make sure `enabled: true` for that provider

### "Connection errors"
- Check your internet connection
- Verify the target URL is accessible
- Check if target has rate limiting

### "Permission denied" errors
- Make sure you have permission to test the target
- Some targets may block automated scanners

## 📚 Documentation

For detailed documentation, see:
- `README.md` - Full feature list and documentation
- `docs/QUICKSTART.md` - Quick start guide
- `docs/ARCHITECTURE.md` - System architecture
- `config/config.example.yaml` - Configuration reference

## 🆘 Support

For issues and questions:
- GitHub Issues: https://github.com/zakirkun/deep-eye/issues
- Check the logs: `logs/deep_eye.log`

---

**Remember**: Use responsibly, test ethically, learn continuously! 🔒
