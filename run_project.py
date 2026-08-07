"""
run_project.py
--------------------------------
Nestlé Quantum DOM Dashboard Launcher
"""

import subprocess
import sys
from pathlib import Path

dashboard = Path("src/dashboard/planner_dashboard.py")

if dashboard.exists():
    subprocess.run([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(dashboard)
    ])
else:
    print("Dashboard file not found:")
    print(dashboard)