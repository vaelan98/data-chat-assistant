# 🤖 Data Chat Assistant
·
> Chat with your data using natural language — powered by OpenAI GPT-4o-mini + Streamlit

---

## Overview

An AI-powered web app that lets you upload any CSV file and ask questions about your data in plain English or Spanish. The LLM analyzes the dataset, generates Python/pandas code to answer your question, and explains the findings in plain language.

**No SQL, no coding required — just ask.**

---

## Features

- 📂 **Upload any CSV** — works with any tabular dataset
- 💬 **Natural language queries** — ask in English or Spanish
- 🧠 **LLM-generated analysis** — GPT-4o-mini writes and explains the pandas code
- 📊 **Instant insights** — averages, rankings, correlations, summaries
- 🔄 **Conversation memory** — follow-up questions keep context
- 🔒 **Secure** — API key stored locally in `.env`, never exposed

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/vaelan98/data-chat-assistant.git
cd data-chat-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the root folder:
```
OPENAI_API_KEY=sk-your-key-here
```
Get your key at [platform.openai.com](https://platform.openai.com)

### 4. Run the app
```bash
python -m streamlit run app.py
```

---

## Example Questions

| Question | What it does |
|---|---|
| "What are the top 5 clients by expected loss?" | Rankings and sorting |
| "What is the average credit score by region?" | Groupby analysis |
| "Are there any null values in the data?" | Data quality check |
| "What is the correlation between loan amount and days overdue?" | Correlation analysis |
| "Summarize the data in an executive paragraph" | LLM text generation |

---

## Author

**Juan Gerardo González Morales**
Mechatronics Engineer | Data & AI | INCAE MBA
🔗 [linkedin.com/in/juan-gonzalez98](https://linkedin.com/in/juan-gonzalez98)
💻 [github.com/vaelan98](https://github.com/vaelan98)
