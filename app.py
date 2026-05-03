import gradio as gr
import subprocess

def run_code(code):
    try:
        with open("temp.py", "w") as f:
            f.write(code)
        result = subprocess.getoutput("python3 temp.py")
        return result
    except Exception as e:
        return str(e)

interface = gr.Interface(
    fn=run_code,
    inputs=gr.Textbox(lines=10),
    outputs="text",
    title="Cloud IDE"
)

interface.launch(share=True)
