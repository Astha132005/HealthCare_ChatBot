# 🩺 HealthCare ChatBot

A simple healthcare assistant chatbot built using **Chainlit**, **LangChain**, and **Hugging Face Transformers**. This project demonstrates how conversational AI can be used to deliver basic health information in a user-friendly, interactive format.

> ⚠️ This chatbot is for **educational and demo purposes only**. It does **not** provide medical advice.

---

## 🚀 Features

- Responds to general health-related queries
- Friendly, informative tone guided by prompt engineering
- Interactive chat interface powered by **Chainlit**
- Runs locally with support for Hugging Face models (DistilGPT-2)

---

## 🛠️ Tech Stack

- 🧠 [LangChain](https://www.langchain.com/)
- 🖼️ [Chainlit](https://www.chainlit.io/)
- 🤗 [Hugging Face Transformers](https://huggingface.co/)
- 🔤 Model: `distilgpt2`
- 🐍 Python

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Astha132005/HealthCare_ChatBot.git
cd HealthCare_ChatBot
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install chainlit transformers langchain torch
```

### 3. Add your Hugging Face token

Edit `healthcare_bot.py` and replace:

```python
os.environ['HUGGINGFACEHUB_API_TOKEN'] = "hf_your_actual_token_here"
```

with your token from [huggingface.co](https://huggingface.co/settings/tokens).

---

## 🧪 Running the Chatbot

```bash
chainlit run healthcare_bot.py -w
```

* This will launch a local web interface at [http://localhost:8000](http://localhost:8000)
* Ask questions like:

  * "What should I eat when I have a fever?"
  * "Give me tips to stay hydrated."

---

## 📸 Screenshots

> Coming soon: UI preview & sample responses

---

## 📚 Learning Insights

* How to integrate Hugging Face models with LangChain
* Using `PromptTemplate` to guide response tone
* Setting up Chainlit as a lightweight chat UI
* Deploying a local chatbot without heavy infra

---

## 🙋‍♀️ About Me

Built by **Astha Dakhinray**
B.Tech CSE (AIML) | Front-End Developer | ML Enthusiast
📎 [LinkedIn](https://www.linkedin.com/in/astha-dakhinray-02b0852a0/)
📎 [Portfolio](https://astha132005.github.io/3D-Portfolio/)

---

## 📌 Disclaimer

This project is not intended for real medical diagnosis or treatment. It is a demonstration of AI capabilities in NLP and conversational design.

---

## 🌟 Star this repo if you found it helpful!

```

---

Let me know if you'd like:
- A `requirements.txt` file
- Screenshots added to the README
- A badge section (stars, license, python version) at the top

I can add them for you!
```
