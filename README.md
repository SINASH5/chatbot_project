# Chatbot Project using FastAPI and Streamlit

This project implements a conversational chatbot using **FastAPI** for the backend and **Streamlit** for the user interface. The chatbot leverages an open-source large language model (LLM) such as GPT-2, Falcon, or LLaMA to generate human-like text responses based on user queries. This solution works entirely offline and does not require API keys.

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The chatbot project integrates the following components:
- **FastAPI**: Acts as the backend server that processes incoming requests and interacts with the LLM.
- **Streamlit**: Serves as the frontend UI, providing an intuitive interface for users to chat with the bot.
- **LLM Integration**: An open-source language model (such as GPT-2, Falcon, or LLaMA) is used to generate responses.
  
This system operates completely offline and can be deployed on your local machine without the need for external API keys.

## Requirements

- Python 3.8 or later
- FastAPI
- Streamlit
- Huggingface's `transformers` library (or any other relevant LLM library)
- Uvicorn (for running FastAPI)
- torch (for model loading, if using PyTorch-based LLM)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/chatbot-project.git
    cd chatbot-project
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have the necessary model weights downloaded for your chosen LLM (e.g., GPT-2, Falcon, or LLaMA).

## Usage

1. Run the backend FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. Run the Streamlit UI:

    ```bash
    streamlit run streamlit_app.py
    ```

3. Visit the URL provided by Streamlit (usually `http://localhost:8501`) to interact with the chatbot.

## Project Structure

