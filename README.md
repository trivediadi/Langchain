# LangChain Components Guide

This repository is a **hands-on exploration of LangChain** — a framework for building applications powered by large language models (LLMs).  
It breaks down LangChain into **individual components** (Chains, Chat Models, Embeddings, Prompts, etc.) with clear examples for learning and reference.

---

## 📂 Repository Structure

| Folder / File         | Description |
|-----------------------|-------------|
| **Chains/**           | Examples and implementations of different LangChain chains, showing how to link multiple LLM calls together. |
| **ChatModels/**       | Code for working with Chat-based models (e.g., OpenAI Chat API, local chat models). |
| **EmbeddingModels/**  | Scripts to generate and use vector embeddings for text and documents. |
| **OutPut_Parser/**    | Parsers to convert raw LLM output into structured formats (JSON, tables, etc.). |
| **Prompts/**          | Prompt templates and formatting examples for different use cases. |
| **Runnables/**        | End-to-end runnable scripts combining multiple components. |
| **Structured_Output/**| Examples of how to enforce structured output from LLMs using schemas. |
| `.gitignore`          | Ignored files & directories for Git. |
| `requirement.txt`     | Python dependencies needed to run the examples. |

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/trivediadi/Langchain.git
cd Langchain
pip install -r requirement.txt
```

---

## 🚀 Usage

Run any example script from the respective folder:

```bash
# Example: running a chain example
python Chains/simple_chain.py

# Example: generating embeddings
python EmbeddingModels/embed_example.py
```

> 📌 Make sure to set your **API keys** (e.g., `OPENAI_API_KEY`) as environment variables before running.

---

## 🧠 Learning Focus

This repo is designed for **learning LangChain step-by-step**:

1. **Understand each component** — study individual folders.
2. **Combine components** — experiment with `Runnables/` scripts.
3. **Build your own LLM app** — adapt these patterns to real-world use cases.

---

## 📜 License

This project is for **educational purposes**.  
Feel free to fork and modify for your own experiments.

---
