import os
import sqlite3
from datetime import datetime
from typing import Optional

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_xai import ChatXAI

from credential_manager import CredentialManager
from tools import create_or_edit_file, run_command, git_commit

class AgentOrbit:
    def __init__(self):
        self.cm = CredentialManager()
        self.cm.setup("trello")
        self.cm.setup("xai")

        self.tools = [create_or_edit_file, run_command, git_commit]

        conn = sqlite3.connect("agent_orbit_memory.db", check_same_thread=False)
        self.checkpointer = SqliteSaver(conn)

        self.llm = ChatXAI(
            model="grok-4",
            temperature=0.7,
            api_key=self.cm.get("XAI_API_KEY")
        )

        self.agent = create_react_agent(self.llm, self.tools, checkpointer=self.checkpointer)

    def run(self, goal: str, thread_id: Optional[str] = None):
        if not thread_id:
            thread_id = f"orbit_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        config = {"configurable": {"thread_id": thread_id}}

        print(f"\n🚀 Agent Orbit Started")
        print(f"Goal: {goal}")
        print(f"Thread: {thread_id}\n")

        inputs = {"messages": [("user", goal)]}

        try:
            for chunk in self.agent.stream(inputs, config, stream_mode="values"):
                if "messages" in chunk:
                    msg = chunk["messages"][-1]
                    if hasattr(msg, "content"):
                        print(f"🤖 {msg.content}\n")
        except Exception as e:
            print(f"❌ Agent error: {str(e)}")

        print("✅ Session finished.\n")
