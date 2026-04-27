import os
from datetime import datetime
from typing import Optional

from langchain_xai import ChatXAI
from credential_manager import CredentialManager
from tools import create_or_edit_file, run_command, git_commit

class AgentOrbit:
    def __init__(self):
        self.cm = CredentialManager()
        self.cm.setup("trello")
        self.cm.setup("xai")

        self.llm = ChatXAI(
            model="grok-4",
            temperature=0.7,
            api_key=self.cm.get("XAI_API_KEY")
        )

        self.tools = {
            "create_or_edit_file": create_or_edit_file,
            "run_command": run_command,
            "git_commit": git_commit,
        }

    def run(self, goal: str, thread_id: Optional[str] = None):
        print(f"\n🚀 Agent Orbit Started")
        print(f"Goal: {goal}\n")

        # Simple direct call for now
        try:
            # For file creation, call tool directly
            if "hello.txt" in goal.lower():
                result = create_or_edit_file.invoke({"filepath": "hello.txt", "content": "Hello from Agent Orbit!"})
                print(f"🤖 {result}")
            else:
                print("🤖 (Tool calling active - this goal not yet mapped)")
        except Exception as e:
            print(f"❌ Error: {str(e)}")

        print("✅ Session finished.\n")
