import os
import subprocess
from pathlib import Path
from git import Repo
from trello import TrelloClient
from langchain.tools import tool

class AgentTools:
    def __init__(self, cm):
        self.cm = cm

    def get_tools(self):
        """Return list of LangChain tools"""
        return [
            self.create_or_edit_file,
            self.run_command,
            self.git_commit,
            self.trello_create_card,
        ]

    @tool
    def create_or_edit_file(self, filepath: str, content: str) -> str:
        """Create or edit a file with given content."""
        try:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            Path(filepath).write_text(content, encoding="utf-8")
            return f"✅ Saved file: {filepath}"
        except Exception as e:
            return f"❌ Error saving file: {str(e)}"

    @tool
    def run_command(self, command: str, cwd: str = ".") -> str:
        """Run a shell command."""
        try:
            result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True, timeout=30)
            output = f"Exit code: {result.returncode}\n{result.stdout}"
            if result.stderr:
                output += f"\nError: {result.stderr}"
            return output
        except Exception as e:
            return f"❌ Command failed: {str(e)}"

    @tool
    def git_commit(self, message: str) -> str:
        """Commit all changes to git."""
        try:
            repo = Repo(".")
            repo.index.add(["."])
            repo.index.commit(message)
            return f"✅ Git commit successful: {message}"
        except Exception as e:
            return f"❌ Git commit failed: {str(e)}"

    @tool
    def trello_create_card(self, list_id: str, name: str, desc: str = "") -> str:
        """Create a Trello card."""
        try:
            client = TrelloClient(
                api_key=self.cm.get("TRELLO_API_KEY"),
                token=self.cm.get("TRELLO_TOKEN")
            )
            card = client.get_list(list_id).add_card(name=name, desc=desc)
            return f"✅ Trello card created: {card.url}"
        except Exception as e:
            return f"❌ Trello error: {str(e)}"
