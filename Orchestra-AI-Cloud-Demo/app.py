import gradio as gr
from router import call_phi3_groq, call_mixtral_together

chat_history = []

def handle_message(message, history):
    if len(message.split()) < 10:
        reply = call_phi3_groq(message)
        model_used = "Phi-3 via Groq"
    else:
        reply = call_mixtral_together(message)
        model_used = "Mixtral via Together"

    history.append((f"You: {message}", f"{model_used} says:\n{reply}"))
    return "", history

with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Orchestra AI Support Assistant")
    with gr.Row():
        chatbot = gr.Chatbot(label="Claude-Style Assistant")
    with gr.Row():
        msg = gr.Textbox(placeholder="Ask your question here...")
    with gr.Row():
        send_btn = gr.Button("Send")

    send_btn.click(fn=handle_message, inputs=[msg, chatbot], outputs=[msg, chatbot])

demo.launch()
