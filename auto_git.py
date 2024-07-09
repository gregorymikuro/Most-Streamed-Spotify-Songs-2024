import subprocess
import time
from datetime import datetime

def git_auto_commit():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        # Check for changes
        subprocess.run(["git", "diff", "--quiet"], check=True)
        print(f"[{now}] No changes to commit.")
    except subprocess.CalledProcessError:
        # Stage all changes
        subprocess.run(["git", "add", "."])

        # Commit changes
        commit_message = f"Auto-commit: {now}"
        subprocess.run(["git", "commit", "-m", commit_message])
        print(f"[{now}] Committed changes.")

        # Push changes (optional)
        # subprocess.run(["git", "push"])

while True:
    git_auto_commit()
    time.sleep(3600) # Sleep for 1 hour
