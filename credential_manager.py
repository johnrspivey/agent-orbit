import os
import webbrowser
from dotenv import load_dotenv, set_key, find_dotenv
from typing import Optional

class CredentialManager:
    def __init__(self, env_file: str = ".env"):
        self.env_file = env_file
        load_dotenv(find_dotenv(env_file))

    def get(self, key: str) -> Optional[str]:
        """Get credential from environment."""
        return os.getenv(key.upper())

    def setup(self, service: str):
        """Interactive setup wizard."""
        print(f"\n🔑 Setting up {service.upper()}...")

        if service.upper() == "TRELLO":
            if self.get("TRELLO_API_KEY") and self.get("TRELLO_TOKEN"):
                print("✅ Trello already configured.")
                return
            
            webbrowser.open("https://trello.com/power-ups/admin")
            input("→ Create Power-Up → copy API Key. Press Enter: ")
            key = input("TRELLO_API_KEY: ").strip()
            
            token_url = f"https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&key={key}"
            webbrowser.open(token_url)
            input("→ Approve → copy token. Press Enter: ")
            token = input("TRELLO_TOKEN: ").strip()
            
            set_key(self.env_file, "TRELLO_API_KEY", key)
            set_key(self.env_file, "TRELLO_TOKEN", token)
            print("✅ Trello credentials saved!")

        elif service.upper() == "XAI":
            if self.get("XAI_API_KEY"):
                print("✅ xAI key already configured.")
                return
            key = input("Paste xAI API Key: ").strip()
            set_key(self.env_file, "XAI_API_KEY", key)
            print("✅ xAI key saved!")

print("CredentialManager loaded.")
