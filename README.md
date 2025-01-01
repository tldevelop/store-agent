# Store Assistant Agent

This project is an AI Agent/Assistant that can connect to a store API using a custom Structured Tool made with LangChain and LangGraph, it uses SQLite Saver as memory to preserve context and data within conversations, it can be wrapped in an API to deploy and add more functionality according to the needs.

## Features

- Connects to any API
- You need to update the API schema in the system prompt and in the message_parser according to your API
- You can use any LLM of your choice, for this case I used Meta's Llama 3.3 Instruct from HuggingFace
- Use your own env variables and keys

## Technologies Used

- **Language**: Python
- **Libraries**:
  - [LangChain](https://python.langchain.com/v0.2/docs/introduction/)
  - [LangGraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
  - [ipykernel](https://pypi.org/project/ipykernel/)
  - [HuggingFace](https://huggingface.co/docs)
  - [python-dotenv](https://saurabh-kumar.com/python-dotenv/)

## Prerequisites

- A text editor or IDE compatible with Python and its virtual environments

## Installation

### Clone the Repository

```bash
git clone https://github.com/tldevelop/store-agent.git
cd store-agent
```

### Create the environment
```bash
python -m venv StoreAgent
```

### Activate the environment
```bash
source StoreAgent/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```