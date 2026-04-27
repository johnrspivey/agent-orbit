import gradio as gr
from agent_orbit import AgentOrbit

agent = AgentOrbit()

def chat(message, history):
    response = ""
    try:
        for chunk in agent.agent.stream(
            {"messages": [("user", message)]},
            {"configurable": {"thread_id": "ui_session"}}
        ):
            if "messages" in chunk and hasattr(chunk["messages"][-1], "content"):
                response += chunk["messages"][-1].content + "\n"
    except Exception as e:
        response = f"Error: {str(e)}"
    
    history.append((message, response))
    return history

with gr.Blocks(title="🚀 Agent Orbit") as demo:
    gr.Markdown("# Agent Orbit\nPersistent AI Developer Agent")

    chatbot = gr.Chatbot(height=700)
    msg = gr.Textbox(
        placeholder="What should I help you build or do today?",
        label="Your request"
    )

    msg.submit(chat, [msg, chatbot], [chatbot])

    gr.Markdown("**Ready.** Type a goal and press Enter.")

demo.queue().launch(share=True)
