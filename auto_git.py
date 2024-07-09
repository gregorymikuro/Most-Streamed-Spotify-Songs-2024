import os
import subprocess
import time

def git_auto_commit():
    # Get the current working directory
    repo_path = os.getcwd()

    # Git commands to stage all changes, commit, and push
    commands = [
        ["git", "-C", repo_path, "add", "."],
        ["git", "-C", repo_path, "commit", "-m", "Auto-commit"],
        ["git", "-C", repo_path, "push"]
    ]

    for cmd in commands:
        subprocess.run(cmd)

while True:
    git_auto_commit()
    time.sleep(3600)  # Sleep for 1 hour
