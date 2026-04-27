from datetime import datetime
from typing import Optional

from langchain_xai import ChatXAI
from credential_manager import CredentialManager
from tools import AgentTools

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

        self.tools = AgentTools(self.cm)

        print("✅ Agent Orbit initialized (direct tools mode)")

    def run(self, goal: str, thread_id: Optional[str] = None):
        print(f"\n🚀 Agent Orbit Started")
        print(f"Goal: {goal}\n")

        try:
            if "hello.txt" in goal.lower() or "create a file" in goal.lower():
                result = self.tools.create_or_edit_file.invoke({"filepath": "hello.txt", "content": "Hello from Agent Orbit!\nThis actually works."})
                print(f"🤖 {result}")
            else:
                print("🤖 Goal received.")
        except Exception as e:
            print(f"❌ Error: {str(e)}")

        print("✅ Session finished.\n")
