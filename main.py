from agent_orbit import AgentOrbit

if __name__ == "__main__":
    print("🚀 Agent Orbit is starting...\n")
    
    agent = AgentOrbit()
    
    print("Agent is ready! What would you like to build or accomplish today?\n")
    goal = input("> ").strip()
    
    if goal:
        agent.run(goal)
    else:
        print("No goal provided.")
