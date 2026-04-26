# tools.py - Simple version (no LangChain @tool issues)

class AgentTools:
    def __init__(self, cm):
        self.cm = cm

    def create_or_edit_file(self, filepath: str, content: str):
        """Create or edit a file."""
        try:
            from pathlib import Path
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            Path(filepath).write_text(content, encoding="utf-8")
            return f"✅ Created/Updated file: {filepath}"
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def run_command(self, command: str):
        """Run shell command."""
        try:
            import subprocess
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            return f"Exit {result.returncode}\n{result.stdout}\n{result.stderr}"
        except Exception as e:
            return f"❌ Error: {str(e)}"

print("✅ Simple tools loaded (no LangChain decorators)")
