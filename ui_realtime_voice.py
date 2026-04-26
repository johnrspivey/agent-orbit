import gradio as gr
from agent_orbit import AgentOrbit

agent = AgentOrbit()

def chat(message, history):
    response = ""
    try:
        for chunk in agent.agent.stream(
            {"messages": [("user", message)]},
            {"configurable": {"thread_id": "github_ui"}}
        ):
            if "messages" in chunk and hasattr(chunk["messages"][-1], "content"):
                response += chunk["messages"][-1].content + "\n"
    except Exception as e:
        response = f"Error: {str(e)}"
    
    history.append((message, response))
    return history

with gr.Blocks(title="🚀 Agent Orbit") as demo:
    gr.Markdown("# Agent Orbit\nPersistent Voice-Ready AI Developer")

    chatbot = gr.Chatbot(height=600)
    msg = gr.Textbox(
        placeholder="What should I help you build today?",
        label="Your request"
    )

    msg.submit(chat, [msg, chatbot], [chatbot])

    gr.Markdown("**Status**: Basic version running. Add XAI_API_KEY in .env for full power.")

demo.queue().launch(share=True)
