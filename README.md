# 🎮 AI-Powered Game Generator

**Streamlit · n8n · Google Gemini LLM**

An AI-powered web application that generates **complete game ideas**—including mechanics, characters, storylines, and gameplay concepts—from a simple text prompt.
Built using **Streamlit** for the UI, **n8n** for automation, and **Google Gemini LLM** for intelligence.

---

##  Project Overview

This project was developed during my **Gen AI Internship at Innomatics Research Labs** to demonstrate how **LLMs + automation workflows + lightweight web apps** can transform creative ideation into an instant, interactive experience.

Users simply describe the type of game they want, and the system automatically generates a structured game design in seconds.

---

##  Features

*  AI-generated **game concepts** from natural language prompts
*  Detailed **core mechanics & rules**
*  Characters with abilities and roles
*  Storyline, themes, and level ideas
*  Gameplay style & user experience breakdown
*  Clean, interactive **Streamlit web interface**
*  Fully automated backend using **n8n workflows**
*  Real-time communication via **Webhooks**

---

##  How It Works

1. User enters a game idea prompt in the **Streamlit UI**
2. Streamlit sends the prompt to an **n8n Webhook**
3. **Google Gemini LLM** analyzes the prompt and generates a structured game design
4. n8n returns the response to Streamlit
5. The generated content is displayed instantly in the web app
6. *(Optional)* Results can be saved, logged, or forwarded via automation

---

##  System Architecture

```
User Prompt
     ↓
Streamlit Web App
     ↓
n8n Webhook
     ↓
Google Gemini LLM
     ↓
Structured Game Design Output
     ↓
Streamlit UI Display
```

---

##  Tech Stack

* **Streamlit** – Frontend web application
* **n8n** – Workflow automation & orchestration
* **Google Gemini LLM** – AI text generation
* **Python** – Application logic
* **Webhooks** – Real-time communication

---

##  Use Cases

* Game designers & indie developers
* Creative brainstorming & ideation
* AI-assisted storytelling
* Educational demos for GenAI & automation
* Rapid prototyping of game concepts

---

##  Key Learnings

* Designing LLM-powered automation workflows
* Prompt engineering for structured creative outputs
* Integrating Streamlit apps with external automation tools
* Building scalable GenAI systems without heavy backend infrastructure

---

##  Demo

🎥 Video demo included in the repository:
`AI Game Generator.mp4`

---

If you like this project, consider giving it a **star**!

---




