from pathlib import Path

print("🚀 Simple Agent Orbit Test")

# Direct file creation test
try:
    Path("hello.txt").write_text("Hello from Agent Orbit!\nThis was created successfully.", encoding="utf-8")
    print("✅ File 'hello.txt' created successfully!")
except Exception as e:
    print(f"❌ Error: {e}")

print("\nTest complete.")
