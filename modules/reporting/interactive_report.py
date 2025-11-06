"""
Interactive HTML Report Generator
Generates interactive, feature-rich HTML reports with charts and filtering
"""

import json
from typing import Dict, List
from datetime import datetime
from utils.logger import get_logger

logger = get_logger(__name__)


class InteractiveReportGenerator:
    """Generate interactive HTML reports with JavaScript functionality."""
    
    def __init__(self, config: Dict):
        """Initialize interactive report generator."""
        self.config = config
    
    def generate_interactive_report(self, scan_results: Dict, output_file: str) -> str:
        """
        Generate interactive HTML report.
        
        Args:
            scan_results: Scan results dictionary
            output_file: Output file path
            
        Returns:
            Path to generated report
        """
        html_content = self._build_interactive_html(scan_results)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        logger.info(f"Interactive report generated: {output_file}")
        return output_file
    
    def _build_interactive_html(self, results: Dict) -> str:
        """Build interactive HTML report."""
        vulnerabilities = results.get('vulnerabilities', [])
        target = results.get('target', 'Unknown')
        scan_time = results.get('scan_time', datetime.now().isoformat())
        
        # Prepare data for JavaScript
        vuln_data_json = json.dumps(vulnerabilities)
        severity_stats = self._calculate_severity_stats(vulnerabilities)
        type_stats = self._calculate_type_stats(vulnerabilities)
        
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deep Eye Security Report - {target}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        :root {{
            --bg-gradient-start: #667eea;
            --bg-gradient-end: #764ba2;
            --container-bg: #ffffff;
            --card-bg: #ffffff;
            --text-primary: #333333;
            --text-secondary: #666666;
            --border-color: #ecf0f1;
            --shadow: 0 2px 10px rgba(0,0,0,0.1);
            --shadow-hover: 0 5px 20px rgba(0,0,0,0.15);
            --header-bg: #2c3e50;
            --accent-color: #3498db;
        }}
        
        [data-theme="dark"] {{
            --bg-gradient-start: #1a1a1a;
            --bg-gradient-end: #2d2d2d;
            --container-bg: #1e1e1e;
            --card-bg: #2d2d2d;
            --text-primary: #e0e0e0;
            --text-secondary: #b0b0b0;
            --border-color: #404040;
            --shadow: 0 2px 10px rgba(0,0,0,0.3);
            --shadow-hover: 0 5px 20px rgba(0,0,0,0.4);
            --header-bg: #1a1a1a;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, var(--bg-gradient-start) 0%, var(--bg-gradient-end) 100%);
            padding: 20px;
            color: var(--text-primary);
            transition: all 0.3s ease;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: var(--container-bg);
            border-radius: 15px;
            box-shadow: var(--shadow-hover);
            overflow: hidden;
        }}
        
        .controls-bar {{
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        
        .control-btn {{
            background: var(--accent-color);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 14px;
            font-weight: bold;
            box-shadow: var(--shadow);
            transition: all 0.3s ease;
        }}
        
        .control-btn:hover {{
            transform: translateY(-2px);
            box-shadow: var(--shadow-hover);
        }}
        
        .header {{
            background: var(--header-bg);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header .subtitle {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .stats-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: var(--container-bg);
        }}
        
        .stat-card {{
            background: var(--card-bg);
            padding: 25px;
            border-radius: 12px;
            box-shadow: var(--shadow);
            text-align: center;
            transition: all 0.3s ease;
            border: 1px solid var(--border-color);
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
            box-shadow: var(--shadow-hover);
        }}
        
        .stat-card .number {{
            font-size: 3em;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        
        .stat-card .label {{
            color: var(--text-secondary);
            font-size: 1.1em;
        }}
        
        .critical {{ color: #e74c3c; }}
        .high {{ color: #e67e22; }}
        .medium {{ color: #f39c12; }}
        .low {{ color: #3498db; }}
        .info {{ color: #95a5a6; }}
        
        .controls {{
            padding: 30px;
            background: var(--container-bg);
            border-bottom: 2px solid var(--border-color);
        }}
        
        .controls h2 {{
            margin-bottom: 20px;
            color: var(--text-primary);
        }}
        
        .filter-group {{
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }}
        
        .filter-btn {{
            padding: 10px 20px;
            border: 2px solid var(--accent-color);
            background: var(--container-bg);
            color: var(--accent-color);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1em;
            font-weight: 500;
        }}
        
        .filter-btn:hover {{
            background: var(--accent-color);
            color: white;
        }}
        
        .filter-btn.active {{
            background: var(--accent-color);
            color: white;
        }}
        
        .search-box {{
            width: 100%;
            padding: 15px;
            border: 2px solid var(--border-color);
            border-radius: 8px;
            font-size: 1em;
            background: var(--card-bg);
            color: var(--text-primary);
        }}
        
        .charts-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
            padding: 30px;
            background: var(--container-bg);
        }}
        
        .chart-card {{
            background: var(--card-bg);
            padding: 25px;
            border-radius: 12px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
        }}
        
        .chart-card h3 {{
            margin-bottom: 20px;
            color: var(--text-primary);
            text-align: center;
        }}
        
        .vulnerabilities {{
            padding: 30px;
            background: var(--container-bg);
        }}
        
        .vuln-card {{
            background: var(--card-bg);
            border-left: 5px solid;
            padding: 25px;
            margin-bottom: 25px;
            border-radius: 10px;
            box-shadow: var(--shadow);
            transition: all 0.3s ease;
        }}
        
        .vuln-card:hover {{
            box-shadow: var(--shadow-hover);
            transform: translateX(5px);
        }}
        
        .vuln-card.critical {{ border-left-color: #e74c3c; }}
        .vuln-card.high {{ border-left-color: #e67e22; }}
        .vuln-card.medium {{ border-left-color: #f39c12; }}
        .vuln-card.low {{ border-left-color: #3498db; }}
        .vuln-card.info {{ border-left-color: #95a5a6; }}
        
        .vuln-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            flex-wrap: wrap;
            gap: 10px;
        }}
        
        .vuln-title {{
            font-size: 1.3em;
            font-weight: bold;
            color: var(--text-primary);
        }}
        
        .severity-badge {{
            padding: 8px 16px;
            border-radius: 20px;
            color: white;
            font-weight: bold;
            text-transform: uppercase;
            font-size: 0.85em;
        }}
        
        .severity-badge.critical {{ background: #e74c3c; }}
        .severity-badge.high {{ background: #e67e22; }}
        .severity-badge.medium {{ background: #f39c12; }}
        .severity-badge.low {{ background: #3498db; }}
        .severity-badge.info {{ background: #95a5a6; }}
        
        .vuln-url {{
            color: var(--text-secondary);
            font-size: 0.95em;
            margin-bottom: 10px;
            word-break: break-all;
        }}
        
        .vuln-description {{
            margin-bottom: 15px;
            line-height: 1.6;
            color: var(--text-primary);
        }}
        
        .vuln-evidence {{
            background: var(--card-bg);
            padding: 15px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            margin-bottom: 15px;
            white-space: pre-wrap;
            word-break: break-all;
            border: 1px solid var(--border-color);
            color: var(--text-primary);
        }}
        
        .vuln-remediation {{
            background: #e8f5e9;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #4caf50;
        }}
        
        .vuln-remediation strong {{
            color: #2e7d32;
        }}
        
        .footer {{
            background: var(--header-bg);
            color: white;
            text-align: center;
            padding: 25px;
        }}
        
        .hidden {{
            display: none !important;
        }}
        
        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}
            
            .controls-bar {{
                position: static;
                justify-content: center;
                margin-bottom: 20px;
            }}
            
            .header h1 {{
                font-size: 2em;
            }}
            
            .stats-container {{
                grid-template-columns: repeat(2, 1fr);
                gap: 15px;
                padding: 20px;
            }}
            
            .charts-container {{
                grid-template-columns: 1fr;
                padding: 20px;
            }}
            
            .filter-group {{
                flex-direction: column;
            }}
            
            .filter-btn {{
                width: 100%;
            }}
        }}
        
        @media print {{
            .controls-bar, .controls, .charts-container {{
                display: none !important;
            }}
            
            body {{
                background: white;
                color: black;
                padding: 0;
            }}
            
            .container {{
                box-shadow: none;
            }}
            
            .vuln-card {{
                page-break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
    <div class="controls-bar">
        <button class="control-btn" onclick="toggleTheme()">🌙 Dark Mode</button>
        <button class="control-btn" onclick="exportToJSON()">📥 Export JSON</button>
        <button class="control-btn" onclick="exportToCSV()">📊 Export CSV</button>
        <button class="control-btn" onclick="window.print()">🖨️ Print</button>
    </div>
    
    <div class="container">
        <div class="header">
            <h1>🔍 Deep Eye Security Report</h1>
            <div class="subtitle">
                Target: {target}<br>
                Scan Date: {scan_time}
            </div>
        </div>
        
        <div class="stats-container">
            <div class="stat-card">
                <div class="number critical">{severity_stats.get('critical', 0)}</div>
                <div class="label">Critical</div>
            </div>
            <div class="stat-card">
                <div class="number high">{severity_stats.get('high', 0)}</div>
                <div class="label">High</div>
            </div>
            <div class="stat-card">
                <div class="number medium">{severity_stats.get('medium', 0)}</div>
                <div class="label">Medium</div>
            </div>
            <div class="stat-card">
                <div class="number low">{severity_stats.get('low', 0)}</div>
                <div class="label">Low</div>
            </div>
            <div class="stat-card">
                <div class="number info">{severity_stats.get('info', 0)}</div>
                <div class="label">Info</div>
            </div>
        </div>
        
        <div class="controls">
            <h2>Filters & Search</h2>
            <div class="filter-group">
                <button class="filter-btn active" onclick="filterBySeverity('all')">All</button>
                <button class="filter-btn" onclick="filterBySeverity('critical')">Critical</button>
                <button class="filter-btn" onclick="filterBySeverity('high')">High</button>
                <button class="filter-btn" onclick="filterBySeverity('medium')">Medium</button>
                <button class="filter-btn" onclick="filterBySeverity('low')">Low</button>
                <button class="filter-btn" onclick="filterBySeverity('info')">Info</button>
            </div>
            <input type="text" class="search-box" id="searchBox" placeholder="Search vulnerabilities..." onkeyup="searchVulnerabilities()">
        </div>
        
        <div class="charts-container">
            <div class="chart-card">
                <h3>Severity Distribution</h3>
                <canvas id="severityChart"></canvas>
            </div>
            <div class="chart-card">
                <h3>Vulnerability Types</h3>
                <canvas id="typeChart"></canvas>
            </div>
        </div>
        
        <div class="vulnerabilities" id="vulnerabilitiesContainer">
            {self._generate_vulnerability_cards(vulnerabilities)}
        </div>
        
        <div class="footer">
            <p>Generated by Deep Eye v1.1.0 | &copy; 2025 | For authorized testing only</p>
        </div>
    </div>
    
    <script>
        const vulnerabilities = {vuln_data_json};
        let currentFilter = 'all';
        
        // Dark Mode Toggle
        function toggleTheme() {{
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? '' : 'dark';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            const btn = document.querySelector('.controls-bar .control-btn');
            btn.textContent = newTheme === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
        }}
        
        // Load saved theme
        document.addEventListener('DOMContentLoaded', function() {{
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme === 'dark') {{
                document.documentElement.setAttribute('data-theme', 'dark');
                const themeBtn = document.querySelector('.controls-bar .control-btn');
                if (themeBtn) themeBtn.textContent = '☀️ Light Mode';
            }}
        }});
        
        // Export to JSON
        function exportToJSON() {{
            const dataStr = JSON.stringify({{
                target: '{target}',
                scan_date: '{scan_time}',
                vulnerabilities: vulnerabilities
            }}, null, 2);
            
            const blob = new Blob([dataStr], {{type: 'application/json'}});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'deep-eye-report-{target}.json';
            a.click();
            URL.revokeObjectURL(url);
        }}
        
        // Export to CSV
        function exportToCSV() {{
            let csv = 'Severity,Type,URL,Description,Evidence,Remediation\\n';
            vulnerabilities.forEach(vuln => {{
                const severity = vuln.severity || '';
                const type = (vuln.type || '').replace(/"/g, '""');
                const url = (vuln.url || '').replace(/"/g, '""');
                const desc = (vuln.description || '').replace(/"/g, '""');
                const evidence = (vuln.evidence || '').replace(/"/g, '""');
                const remediation = (vuln.remediation || '').replace(/"/g, '""');
                csv += `"${{severity}}","${{type}}","${{url}}","${{desc}}","${{evidence}}","${{remediation}}"\\n`;
            }});
            
            const blob = new Blob([csv], {{type: 'text/csv'}});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'deep-eye-report-{target}.csv';
            a.click();
            URL.revokeObjectURL(url);
        }}
        
        // Initialize charts
        const severityCtx = document.getElementById('severityChart').getContext('2d');
        const severityChart = new Chart(severityCtx, {{
            type: 'doughnut',
            data: {{
                labels: ['Critical', 'High', 'Medium', 'Low', 'Info'],
                datasets: [{{
                    data: [{severity_stats.get('critical', 0)}, {severity_stats.get('high', 0)}, {severity_stats.get('medium', 0)}, {severity_stats.get('low', 0)}, {severity_stats.get('info', 0)}],
                    backgroundColor: ['#e74c3c', '#e67e22', '#f39c12', '#3498db', '#95a5a6'],
                    borderWidth: 2,
                    borderColor: '#ffffff'
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: true,
                plugins: {{
                    legend: {{
                        position: 'bottom',
                        labels: {{
                            padding: 15,
                            font: {{
                                size: 12
                            }}
                        }}
                    }},
                    tooltip: {{
                        callbacks: {{
                            label: function(context) {{
                                const label = context.label || '';
                                const value = context.parsed || 0;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = total > 0 ? ((value / total) * 100).toFixed(1) : 0;
                                return label + ': ' + value + ' (' + percentage + '%)';
                            }}
                        }}
                    }}
                }}
            }}
        }});
        
        const typeCtx = document.getElementById('typeChart').getContext('2d');
        const typeData = {json.dumps(type_stats)};
        const typeChart = new Chart(typeCtx, {{
            type: 'bar',
            data: {{
                labels: Object.keys(typeData),
                datasets: [{{
                    label: 'Vulnerability Count',
                    data: Object.values(typeData),
                    backgroundColor: '#3498db',
                    borderWidth: 0
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: true,
                plugins: {{
                    legend: {{
                        display: false
                    }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        ticks: {{
                            stepSize: 1
                        }}
                    }}
                }}
            }}
        }});
        
        function filterBySeverity(severity) {{
            currentFilter = severity;
            const cards = document.querySelectorAll('.vuln-card');
            const buttons = document.querySelectorAll('.filter-btn');
            
            buttons.forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            cards.forEach(card => {{
                if (severity === 'all' || card.classList.contains(severity)) {{
                    card.classList.remove('hidden');
                }} else {{
                    card.classList.add('hidden');
                }}
            }});
        }}
        
        function searchVulnerabilities() {{
            const searchTerm = document.getElementById('searchBox').value.toLowerCase();
            const cards = document.querySelectorAll('.vuln-card');
            
            cards.forEach(card => {{
                const text = card.textContent.toLowerCase();
                if (text.includes(searchTerm)) {{
                    if (currentFilter === 'all' || card.classList.contains(currentFilter)) {{
                        card.classList.remove('hidden');
                    }}
                }} else {{
                    card.classList.add('hidden');
                }}
            }});
        }}
    </script>
</body>
</html>'''
        
        return html
    
    def _generate_vulnerability_cards(self, vulnerabilities: List[Dict]) -> str:
        """Generate HTML cards for vulnerabilities."""
        if not vulnerabilities:
            return '<div class="vuln-card info"><p>No vulnerabilities found!</p></div>'
        
        cards_html = []
        
        for vuln in vulnerabilities:
            severity = vuln.get('severity', 'info')
            vuln_type = vuln.get('type', 'Unknown')
            url = vuln.get('url', 'N/A')
            description = vuln.get('description', 'No description available')
            evidence = vuln.get('evidence', 'No evidence available')
            remediation = vuln.get('remediation', 'No remediation available')
            
            card = f'''
            <div class="vuln-card {severity}">
                <div class="vuln-header">
                    <div class="vuln-title">{vuln_type}</div>
                    <div class="severity-badge {severity}">{severity}</div>
                </div>
                <div class="vuln-url"><strong>URL:</strong> {url}</div>
                <div class="vuln-description">{description}</div>
                <div class="vuln-evidence"><strong>Evidence:</strong><br>{evidence}</div>
                <div class="vuln-remediation"><strong>Remediation:</strong><br>{remediation}</div>
            </div>
            '''
            cards_html.append(card)
        
        return ''.join(cards_html)
    
    def _calculate_severity_stats(self, vulnerabilities: List[Dict]) -> Dict[str, int]:
        """Calculate severity statistics."""
        stats = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0, 'info': 0}
        
        for vuln in vulnerabilities:
            severity = vuln.get('severity', 'info').lower()
            if severity in stats:
                stats[severity] += 1
        
        return stats
    
    def _calculate_type_stats(self, vulnerabilities: List[Dict]) -> Dict[str, int]:
        """Calculate vulnerability type statistics."""
        stats = {}
        
        for vuln in vulnerabilities:
            vuln_type = vuln.get('type', 'Unknown')
            # Shorten long type names
            vuln_type = vuln_type[:30] + '...' if len(vuln_type) > 30 else vuln_type
            stats[vuln_type] = stats.get(vuln_type, 0) + 1
        
        # Get top 10 types
        sorted_stats = dict(sorted(stats.items(), key=lambda x: x[1], reverse=True)[:10])
        return sorted_stats
