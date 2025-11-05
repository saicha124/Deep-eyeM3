#!/bin/bash
echo "Running test scan to generate enhanced vulnerability digest..."
python deep_eye.py -u https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files -v
echo ""
echo "✅ Scan complete! Check the reports/ directory for:"
echo "   - vulnerability_digest_YYYYMMDD_HHMMSS.html"
