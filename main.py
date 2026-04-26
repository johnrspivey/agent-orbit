from pathlib import Path

print("🚀 Simple Agent Orbit Test Mode")

print("\nTesting file creation...")

try:
    Path("hello.txt").write_text("Hello from Agent Orbit!\nThis file was created successfully at " + str(Path(".").absolute()), encoding="utf-8")
    print("✅ SUCCESS: hello.txt created!")
except Exception as e:
    print(f"❌ Failed to create file: {e}")

print("\nAgent Orbit basic test complete.")
print("You can now expand from here.")
