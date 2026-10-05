#!/bin/bash
echo "=== Starting Vercel Build for VR TECH Solutions ==="
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "=== Static file collection complete ==="
