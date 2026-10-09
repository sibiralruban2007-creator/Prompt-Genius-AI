# PromptGenius AI

### An AI-Powered Prompt Engineering Playground

PromptGenius AI is a web application built using Python and Streamlit that helps users improve prompts and explore different prompt engineering techniques using AI.

## Features

* Prompt Optimization
* Zero-Shot Prompting
* One-Shot Prompting
* Few-Shot Prompting
* Role-Based Prompting
* AI Response Generation using Groq API
* Adjustable Temperature
* Maximum Token Control
* Secure API Key Configuration

## Technologies Used

* Python
* Streamlit
* Groq API
* python-dotenv

## Project Structure

```text
PromptGenius-AI/
├── app.py
├── llm.py
├── prompt_optimizer.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd PromptGenius-AI
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the API Key

Create a `.env` file in the project folder:

```dotenv
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from:
https://console.groq.com/keys

Never upload your `.env` file to GitHub.

### 4. Run the Application

```bash
streamlit run app.py
```

## Project Objective

The objective of PromptGenius AI is to demonstrate prompt optimization and different prompt engineering techniques through an interactive web application.

## Future Enhancements

* Prompt quality scoring
* Save and reuse prompts
* Side-by-side prompt comparison
* Support for additional AI models
* Custom prompt templates

## Author

Sibiral Ruban

B.Sc. Computer Science with Artificial Intelligence


