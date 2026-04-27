# tools.py - Final clean version using StructuredTool
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
from pathlib import Path
import subprocess
from git import Repo
from typing import Optional

class CreateFileInput(BaseModel):
    filepath: str = Field(..., description="Path to the file")
    content: str = Field(..., description="Content to write")

def _create_or_edit_file(filepath: str, content: str) -> str:
    """Create or edit a file."""
    try:
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        Path(filepath).write_text(content, encoding="utf-8")
        return f"✅ Saved: {filepath}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

create_or_edit_file = StructuredTool.from_function(
    func=_create_or_edit_file,
    name="create_or_edit_file",
    description="Create or edit a file with the given content",
    args_schema=CreateFileInput
)

# Similarly for other tools
def _run_command(command: str, cwd: str = ".") -> str:
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True, timeout=30)
        return f"Exit {result.returncode}\n{result.stdout}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

run_command = StructuredTool.from_function(
    func=_run_command,
    name="run_command",
    description="Run a shell command",
)

def _git_commit(message: str) -> str:
    try:
        repo = Repo(".")
        repo.index.add(["."])
        repo.index.commit(message)
        return f"✅ Committed: {message}"
    except Exception as e:
        return f"❌ Git error: {str(e)}"

git_commit = StructuredTool.from_function(
    func=_git_commit,
    name="git_commit",
    description="Commit changes to git",
)

print("✅ Tools loaded (StructuredTool version)")
