from pathlib import Path

print("🚀 Agent Orbit - Simple Test Mode\n")

# Direct file creation (no tools / LangGraph)
try:
    filepath = "hello.txt"
    content = "Hello from Agent Orbit!\nThis file was created successfully at " + str(Path(".").absolute())
    Path(filepath).write_text(content, encoding="utf-8")
    print(f"✅ SUCCESS: Created file '{filepath}'")
    print("Check your project folder — the file should be there now.")
except Exception as e:
    print(f"❌ Failed: {e}")

print("\nBasic file creation test complete.")
print("We can add the full agent once this works reliably.")
