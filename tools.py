from langchain.tools import tool
from pathlib import Path
import subprocess
from git import Repo

@tool
def create_or_edit_file(filepath: str, content: str) -> str:
    """Create or edit any file."""
    try:
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        Path(filepath).write_text(content, encoding="utf-8")
        return f"✅ Saved: {filepath}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

@tool
def run_command(command: str, cwd: str = ".") -> str:
    """Run a shell command."""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True, timeout=30)
        return f"Exit code: {result.returncode}\n{result.stdout}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

@tool
def git_commit(message: str) -> str:
    """Commit changes to git."""
    try:
        repo = Repo(".")
        repo.index.add(["."])
        repo.index.commit(message)
        return f"✅ Committed: {message}"
    except Exception as e:
        return f"❌ Git error: {str(e)}"

print("✅ Tools loaded (standalone functions)")
