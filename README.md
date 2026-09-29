# OpenAI API Lab Agent

This project is a minimal Python agent scaffold powered by the OpenAI API.

## Features
- Simple CLI entry point
- Reusable `OpenAIAgent` class
- Environment-based configuration
- Ready for extension with tools, memory, or multi-step workflows

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy the example environment file and add your API key:
   ```bash
   copy .env.example .env
   ```

4. Edit `.env` and set your key:
   ```env
   OPENAI_API_KEY=your_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

## Run the agent

```bash
python main.py "Summarize the benefits of using AI agents in a business workflow."
```

You can also override the model:

```bash
python main.py "Plan a 3-step launch strategy." --model gpt-4o-mini
```

## Project structure

- `main.py` – CLI entry point
- `src/openai_agent/agent.py` – agent implementation
- `.env.example` – environment template
- `requirements.txt` – Python dependencies
