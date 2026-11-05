#  MicroSprout: Microclimate Garden Assistant

**MicroSprout** is an offline microclimate gardening advisor built for the **Hacktoberfest Challenge: Touch Grass**. 

It analyzes hyper-localized climate inputs, sunlight, space constraints, and soil conditions to generate immediate, actionable outdoor gardening tasks in under 60 seconds.

---

##  Demo & Output

![MicroSprout Output Demo](output.png)

---

##  Key Features
- **Instant Microclimate Analysis:** Provides 2-3 immediate sowing candidates based on localized weather/region.
- **Action-Oriented Prompts:** Delivers a focused 15-minute hands-in-the-dirt task to get users away from screens.
- **Privacy-First & Open-Weights:** Runs locally using `Qwen/Qwen2.5-1.5B-Instruct` with zero external cloud dependencies.
- **Interactive Interface:** Interactive dashboard powered by Gradio.

---

##  Tech Stack
- **Language:** Python 3.10+
- **Model:** `Qwen/Qwen2.5-1.5B-Instruct`
- **Frameworks:** PyTorch, Hugging Face `transformers`, `accelerate`
- **Frontend/UI:** Gradio (`gr.Blocks`)

---

##  License
This project is open-source under the MIT License. Built with  for the Hacktoberfest Open-Source AI Challenge.
