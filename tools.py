from langchain.tools import tool
from pathlib import Path
import subprocess
from git import Repo

@tool
def create_or_edit_file(filepath: str, content: str) -> str:
    """Create or edit any file with the given content."""
    try:
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        Path(filepath).write_text(content, encoding="utf-8")
        return f"✅ Successfully saved: {filepath}"
    except Exception as e:
        return f"❌ Error saving file: {str(e)}"

@tool
def run_command(command: str, cwd: str = ".") -> str:
    """Run a shell command."""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True, timeout=30)
        output = f"Exit code: {result.returncode}\n{result.stdout}"
        if result.stderr:
            output += f"\nError: {result.stderr}"
        return output
    except Exception as e:
        return f"❌ Command error: {str(e)}"

@tool
def git_commit(message: str) -> str:
    """Commit all changes to git."""
    try:
        repo = Repo(".")
        repo.index.add(["."])
        repo.index.commit(message)
        return f"✅ Committed: {message}"
    except Exception as e:
        return f"❌ Git error: {str(e)}"

print("✅ Tools loaded successfully")
