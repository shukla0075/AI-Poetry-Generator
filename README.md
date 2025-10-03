# ✒️ AI Poetry Generator

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A web application that generates unique poetry based on a user's prompt, powered by a modern, instruction-tuned language model.


## 📜 Project Overview

This project is a user-friendly web app built with Gradio that allows users to generate poetry on any topic. It leverages the `TinyLlama-1.1B-Chat-v1.0` model, a powerful yet efficient instruction-tuned AI, to produce creative and contextually relevant poems. The project showcases skills in generative AI, prompt engineering, and model deployment.

## ✨ Features

-   **Interactive UI:** Simple and clean user interface built with Gradio.
-   **High-Quality Generation:** Utilizes the instruction-tuned TinyLlama model for coherent and creative output.
-   **Advanced Prompting:** Employs a "chat template" with a system prompt to guide the model's tone and format, ensuring poetic output.
-   **Optimized for Apple Silicon:** The application runs efficiently on an M1 Mac by leveraging the MPS backend via PyTorch.

## 🛠️ Tech Stack

-   **Backend:** Python 3.11
-   **AI/ML Libraries:** PyTorch, Hugging Face `transformers` & `accelerate`
-   **Model:** `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
-   **Web Framework:** Gradio


## ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/shukla0075/AI-Poetry-Generator.git](https://github.com/shukla0075/AI-Poetry-Generator.git)
    cd AI-Poetry-Generator
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```bash
    python app.py
    ```
    Open the local URL provided in your browser.

## 🧠 The Journey & Key Learnings

This project was a deep dive into the practical challenges of building a generative AI application. My journey involved several key stages and learnings:

1.  **Initial Model Selection:** I began with a base `gpt2` model. While it could generate text, the output was often incoherent.
2.  **Fine-Tuning:** To improve quality, I fine-tuned `gpt2` on a small, curated dataset of poetry. This was a valuable exercise in using the Hugging Face `Trainer` API.
3.  **Diagnosing Overfitting:** The fine-tuned model suffered from severe **overfitting** and **hallucination**. It had memorized the style of the tiny dataset but lost its general world knowledge, producing nonsensical output for new prompts.
4.  **Pivoting to a Better Model:** Realizing the limitations of fine-tuning a small model on a small dataset, I pivoted my strategy. I switched to a larger, pre-trained but **instruction-tuned** model (`gpt2-medium` and finally `TinyLlama-1.1B-Chat-v1.0`).
5.  **Advanced Prompt Engineering:** I learned that for modern instruction-tuned models, the prompt is everything. I implemented a chat-based prompt with a system message to explicitly command the AI to act as a poet, which yielded far superior and more reliable results.

This iterative process taught me that choosing the right model and engineering the right prompt are often more effective than fine-tuning for many real-world applications.