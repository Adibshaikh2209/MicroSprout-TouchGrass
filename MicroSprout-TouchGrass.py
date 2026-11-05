import gradio as gr
import torch
from transformers import pipeline

# Load lightweight open-weight model (Ungated, no login required)
pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)


def plan_garden(region, sunlight, garden_type, soil_condition):
    system_instruction = (
        "You are an offline Microclimate Garden Advisor designed for the 'Touch Grass' challenge. "
        "Your mission is to get gardeners outside immediately. "
        "Analyze the user's localized conditions and output exactly:\n"
        "1. Current Sowing Candidates (2-3 plants ready to sow right now)\n"
        "2. Soil & Bed Prep (2 concise bullet points)\n"
        "3. Today's 15-Minute Outdoor Task (a clear actionable step in the dirt)\n"
        "End with: 'Now close your laptop, grab your trowel, and step outside!'"
    )

    user_query = (
        f"Location/Climate: {region}\n"
        f"Sunlight: {sunlight}\n"
        f"Space: {garden_type}\n"
        f"Soil/Moisture: {soil_condition}"
    )

    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": user_query},
    ]

    response = pipe(messages, max_new_tokens=300, temperature=0.6)
    return response[0]["generated_text"][-1]["content"]


# Gradio Interface
with gr.Blocks(title="MicroSprout Planner") as demo:
    gr.Markdown("# 🌱 MicroSprout: Microclimate Garden Assistant")
    gr.Markdown(
        "Enter your space parameters to get your planting tasks for today. "
        "The goal: spend 60 seconds on this screen, then get your hands in the dirt."
    )

    with gr.Row():
        region_input = gr.Textbox(
            label="Location / Region",
            placeholder="e.g., Pune / Mumbai plateau, USDA Zone 9b, or coastal mild",
        )
        sun_input = gr.Dropdown(
            choices=[
                "Full Sun (6+ hrs)",
                "Partial Shade (3-6 hrs)",
                "Full Shade (<3 hrs)",
            ],
            value="Full Sun (6+ hrs)",
            label="Sunlight Exposure",
        )

    with gr.Row():
        type_input = gr.Dropdown(
            choices=[
                "Balcony Pots & Containers",
                "Raised Beds",
                "Direct In-Ground",
                "Window Sill",
            ],
            value="Raised Beds",
            label="Growing Setup",
        )
        soil_input = gr.Textbox(
            label="Soil / Moisture Condition",
            placeholder="e.g., Dry clay, well-draining potting mix, damp loam",
        )

    action_btn = gr.Button("Get Today's Planting Plan", variant="primary")
    output_display = gr.Markdown(label="Outdoor Action Plan")

    action_btn.click(
        fn=plan_garden,
        inputs=[region_input, sun_input, type_input, soil_input],
        outputs=output_display,
    )

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft(), share=True)