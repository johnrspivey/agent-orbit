# tools.py - Minimal working version
from pathlib import Path
import subprocess
from git import Repo

def create_or_edit_file(filepath: str, content: str):
    """Create or edit a file."""
    try:
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        Path(filepath).write_text(content, encoding="utf-8")
        return f"✅ Saved file: {filepath}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def run_command(command: str, cwd: str = "."):
    """Run shell command."""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True, timeout=30)
        return f"Exit code: {result.returncode}\n{result.stdout}\n{result.stderr}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def git_commit(message: str):
    """Git commit."""
    try:
        repo = Repo(".")
        repo.index.add(["."])
        repo.index.commit(message)
        return f"✅ Committed: {message}"
    except Exception as e:
        return f"❌ Git error: {str(e)}"

print("✅ Minimal tools loaded")
