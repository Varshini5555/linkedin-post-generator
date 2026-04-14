# 🚀 LLM-Powered LinkedIn Post Generator

An AI-powered application that generates high-quality LinkedIn posts using Large Language Models (LLMs) with controllable tone, length, language, and writing style (persona-based generation).

---

## 🔥 Features

- Generate LinkedIn posts based on topic, length, and language  
- Persona-based writing styles (multiple authors)  
- Few-shot learning for improved output quality  
- Dynamic topic filtering based on selected writing style  
- Optional emoji inclusion  
- Real-time generation using LLM APIs (Groq / OpenAI-compatible)  

---

## 🧠 How It Works

1. User selects:
   - Topic  
   - Length  
   - Language  
   - Writing Style (Persona)  

2. System:
   - Filters relevant examples from dataset  
   - Selects top examples based on engagement  
   - Constructs a dynamic prompt  

3. LLM generates:
   - Structured LinkedIn post  

---

## 🧠 System Architecture

- Data Layer → Processed post dataset with tags and metadata
- Filtering Layer → Selects examples based on topic, language, persona
- Prompt Layer → Constructs few-shot prompt dynamically
- LLM Layer → Generates post using Groq API
- UI Layer → Streamlit interface for user interaction

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- LangChain  
- Groq API (LLM)  
- Pandas  

---

## 📸 Demo

### Application UI  
![UI](assets/ui.png)

### Generated Output  
![Output](assets/output_1.png)
![Output](assets/output_2.png)

---

## ✨ Sample Output

We prioritize deadlines. But neglect self-care. Stress builds up. Anxiety kicks in. Sleepless nights.

That's not productivity. That's a ticking bomb 🚨. Take a breath 🌟. Prioritize your mental health 🧠. Your well-being matters 💖.

---

## 🚀 Future Improvements
- Multi-post generation
- Engagement prediction model
- RAG-based personalization

---

## 🙌 Acknowledgment

This project was inspired by a foundational LinkedIn post generator tutorial by Codebasics.  
I extended the base idea by implementing persona-based content generation, dynamic filtering logic, and a structured few-shot prompting pipeline.

