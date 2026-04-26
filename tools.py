# tools.py - Minimal version to bypass LangChain decorator issues

def create_or_edit_file(filepath: str, content: str):
    """Create or edit a file."""
    from pathlib import Path
    try:
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        Path(filepath).write_text(content, encoding="utf-8")
        return f"✅ Created/updated file: {filepath}"
    except Exception as e:
        return f"❌ Failed to save file: {str(e)}"

def run_command(command: str):
    """Run shell command."""
    import subprocess
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        return f"Exit code: {result.returncode}\n{result.stdout}"
    except Exception as e:
        return f"❌ Command failed: {str(e)}"

print("✅ Minimal tools loaded successfully")
