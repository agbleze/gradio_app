import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(fn=greet, input=["text", "slider"],
                    output=["text"]
                    )