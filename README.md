# dsa-tutor-chatbot
An AI-powered DSA tutor chatbot built with Google Gemini and Streamlit-explains concepts,gives hints on problems and rememebers conversations.
# 📚 AI Study Buddy - DSA Tutor Chatbot

A conversational AI assistant that helps students learn Data Structures 
and Algorithms, built using Google's Gemini API and deployed live with 
Streamlit.

🔗 **[Try the live app here](https://dsa-tutor-chatbot-7eqk9j9kvhhyvxhh7hh7yy.streamlit.app/)**

## Overview

This project is an AI-powered tutor chatbot designed to help students 
understand DSA concepts through clear explanations and guided problem-solving, 
rather than simply providing direct answers. The chatbot maintains conversation 
context, allowing for natural follow-up questions.

## Features

- Custom persona via system prompting — tutor-style responses tailored 
  for a beginner CS student
- Guided hints rather than direct solutions for coding problems
- Persistent conversation memory across the session
- Simple, chat-style interface

## Approach

1. Configured the Gemini API with a custom system prompt defining the 
   chatbot's tutoring behavior and constraints
2. Implemented conversation state using Gemini's chat session, enabling 
   context-aware follow-up responses
3. Built an interactive chat interface using Streamlit's chat components
4. Deployed the app with securely managed API credentials via Streamlit Secrets

## Tech Stack

- Python
- Google Gemini API (google-generativeai)
- Streamlit

## Files

| File | Description |
|---|---|
| `app.py` | Streamlit app with chatbot logic and UI |
| `requirements.txt` | Python dependencies for deployment |



Note: requires a Gemini API key set as an environment variable 


- Expand beyond DSA to other CS subjects
- Add code execution to verify user-submitted solutions
- Support file/document upload for topic-specific Q&A (RAG)
