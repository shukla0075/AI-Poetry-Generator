import gradio as gr
import torch
from transformers import pipeline

print("Loading TinyLlama-Chat model... This is ~1.1GB and will take time on the first run.")
# --- THE FINAL MODEL ---
# Using a modern, instruction-tuned model designed to follow commands.
generator = pipeline(
    'text-generation', 
    model='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    torch_dtype=torch.float16, # Optimized for performance
    device_map="auto"          # Automatically uses Mac's GPU
)
print("Model loaded successfully!")

def generate_content(prompt):
    # --- MODERN CHAT PROMPT ---
    # We create a conversation to give the model clear instructions.
    messages = [
        {
            "role": "system",
            "content": "You are a world-class poet. Your task is to write a short, creative, and emotionally resonant poem based on the user's topic. Do not write a story or prose.",
        },
        {"role": "user", "content": f"Write a poem about: {prompt}"},
    ]

    # The pipeline applies the correct chat template for the model.
    outputs = generator(
        messages, 
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95
    )
    
    # The output is a complex structure, so we extract just the generated part.
    generated_text = outputs[0]["generated_text"]
    
    # We find the assistant's response and clean it up.
    assistant_response = generated_text[-1]['content']
    return assistant_response

with gr.Blocks() as demo:
    gr.Markdown("# ✒️ Advanced Poetry Generator")
    gr.Markdown("Enter a topic to generate a poem using an instruction-tuned AI (TinyLlama-Chat).")
    
    prompt_input = gr.Textbox(label="Topic / Prompt", placeholder="e.g., a lonely wolf")
    generate_button = gr.Button("Generate Poem", variant="primary")
    output_text = gr.Textbox(label="Generated Poem", lines=12)
    
    generate_button.click(
        fn=generate_content, 
        inputs=[prompt_input], 
        outputs=output_text
    )

print("Starting the web server...")
demo.launch()