# Multi-Language Report Generation

Deep Eye now supports generating security reports in multiple languages simultaneously, perfect for international teams and compliance requirements.

## Supported Languages

- 🇬🇧 **English** - Complete security reports in English
- 🇫🇷 **French** - Rapports de sécurité complets en Français  
- 🇸🇦 **Arabic** - تقارير أمنية كاملة بالعربية

## How to Use

### Generate Reports in All Languages

Use the `--multilingual` flag to generate reports in all three languages:

```bash
python deep_eye.py -u https://example.com --multilingual
```

This will create three separate report files:
- `deep_eye_example_20251104_123456_en.html` - English report
- `deep_eye_example_20251104_123456_fr.html` - French report  
- `deep_eye_example_20251104_123456_ar.html` - Arabic report

### Generate Report in Single Language

To generate a report in a specific language, configure it in `config/config.yaml`:

```yaml
reporting:
  enabled: true
  language: 'en'  # Options: 'en', 'fr', 'ar'
  default_format: 'html'
  output_directory: 'reports'
```

Then run normally:
```bash
python deep_eye.py -u https://example.com
```

## What's Translated

All report content is fully translated, including:

### Report Sections
- ✅ Report title and headers
- ✅ Executive summary
- ✅ Vulnerability listings
- ✅ Severity levels (Critical, High, Medium, Low)
- ✅ Target information
- ✅ Scan statistics

### Vulnerability Details
- ✅ Descriptions
- ✅ Evidence
- ✅ URL and parameter labels
- ✅ Discovery timestamps
- ✅ OSINT and reconnaissance findings

### Remediation Guidance
- ✅ Priority levels
- ✅ Estimated fix times
- ✅ Step-by-step instructions
- ✅ Code examples headers
- ✅ Solution sections
- ✅ References and resources

**Note:** Technical content like code examples, CWE references, URLs, and technical evidence remain in their original technical format for accuracy and consistency across all language versions.

## Use Cases

### International Security Teams
Generate reports in multiple languages for distributed teams:
```bash
python deep_eye.py -u https://corporate-site.com --multilingual
```
- English report for US/UK teams
- French report for European offices
- Arabic report for Middle East operations

### Compliance Requirements
Meet regulatory requirements for documentation in local languages while maintaining technical accuracy.

### Client Deliverables
Provide security assessment reports in your client's preferred language without manual translation.

## Examples

### Standard Scan with Multilingual Reports
```bash
python deep_eye.py -u https://example.com --multilingual
```

### Verbose Scan with Multilingual Reports
```bash
python deep_eye.py -u https://example.com -v --multilingual
```

### Custom Config with Multilingual Reports
```bash
python deep_eye.py -c myconfig.yaml -u https://example.com --multilingual
```

## Output Structure

When using `--multilingual`, you'll see output like:

```
✓ Reports generated successfully:
  • 🇬🇧 English: reports/deep_eye_example_20251104_123456_en.html
  • 🇫🇷 French: reports/deep_eye_example_20251104_123456_fr.html
  • 🇸🇦 Arabic: reports/deep_eye_example_20251104_123456_ar.html
```

## Benefits

- **No Manual Translation**: Automatically generate reports in all languages
- **Consistent Content**: Same vulnerabilities, evidence, and remediation across all versions
- **Time Saving**: Generate 3 reports in the same time as 1
- **Professional**: Deliver reports in stakeholder's native language
- **Compliance Ready**: Meet documentation requirements in multiple jurisdictions

## Language-Specific Features

### Arabic Support
- Right-to-left (RTL) text direction supported
- Arabic numerals and proper formatting
- Full Arabic translations for all UI elements

### French Support  
- Proper accents and special characters (é, è, à, ç, etc.)
- Formal French terminology for security concepts
- European French conventions

### English Support
- International English (not US-specific)
- Industry-standard security terminology
- OWASP and CWE standard references

## Note on Technical Content

For consistency and accuracy, the following elements remain in their original format across all language versions:

- Code examples (remain in original programming language syntax)
- URLs and domains
- CWE identifiers
- OWASP references
- Technical commands and configurations
- File paths and system commands

This ensures technical accuracy and makes it easier for technical staff to implement remediation steps regardless of the report language.
