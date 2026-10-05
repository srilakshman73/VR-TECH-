#!/bin/bash
echo "=== Starting Vercel Build for VR TECH Solutions ==="

# Install dependencies in the build environment
python3 -m pip install -r requirements.txt --break-system-packages || pip install -r requirements.txt --break-system-packages || pip3 install -r requirements.txt

# Collect static files into staticfiles directory
python3 manage.py collectstatic --noinput --clear

echo "=== Static file collection complete ==="
