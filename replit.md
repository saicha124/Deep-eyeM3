# Deep Eye - Security Scanner

## Overview
Deep Eye is an advanced AI-driven vulnerability scanner and penetration testing tool. It integrates multiple AI providers (OpenAI, Claude, Grok, OLLAMA) with comprehensive security testing modules for automated bug hunting, intelligent payload generation, and professional reporting.

**Version**: 1.3.0 (Hestia)
**Type**: Command-line security testing tool
**Language**: Python 3.11

## Project Architecture
- **Core Engine**: Scanner engine with AI-powered vulnerability detection
- **AI Providers**: Multi-provider support (OpenAI, Claude, Grok, OLLAMA)
- **Security Modules**: 45+ attack methods including SQL injection, XSS, SSRF, API security, WebSocket testing
- **Reconnaissance**: OSINT gathering, subdomain enumeration, DNS records
- **Reporting**: HTML/PDF/JSON report generation

## Key Features
- Multi-AI provider support for intelligent payload generation
- Comprehensive vulnerability scanning (OWASP Top 10 and beyond)
- Advanced reconnaissance capabilities
- Machine learning anomaly detection
- WebSocket security testing
- API and GraphQL security testing
- Custom plugin system
- Multi-channel notifications (Email, Slack, Discord)

## Setup & Configuration
The tool requires configuration in `config/config.yaml`:
1. Copy `config/config.example.yaml` to `config/config.yaml`
2. Add API keys for at least one AI provider (OpenAI, Claude, Grok, or OLLAMA)
3. Configure scanner settings (depth, threads, scan modes)
4. Set up reporting preferences

## Usage
```bash
# Basic scan
python deep_eye.py -u https://example.com

# Scan with verbose output
python deep_eye.py -u https://example.com -v

# Use custom config file
python deep_eye.py -c custom_config.yaml

# Show version
python deep_eye.py --version
```

## Important Notes
- **Legal**: Only use on systems you own or have explicit permission to test
- **API Keys Required**: At least one AI provider API key must be configured
- **Reports**: Generated in the `reports/` directory
- **Logs**: Available in the `logs/` directory

## Directory Structure
- `core/` - Core scanning engine
- `ai_providers/` - AI provider integrations
- `modules/` - Security testing modules
- `utils/` - Utility functions
- `config/` - Configuration files
- `reports/` - Generated reports (gitignored)
- `logs/` - Application logs (gitignored)
- `data/` - Session and model data (gitignored)

## Recent Changes
- Initial Replit setup completed
- Python 3.11 environment configured
- All dependencies installed
- Required directories created
- Configuration template copied
