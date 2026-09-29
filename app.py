import os

from dotenv import load_dotenv

from main import run_prompt


load_dotenv()


def main() -> None:
    prompt = "Hello! Please introduce yourself and explain how you can help me."
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    api_key = os.getenv("OPENAI_API_KEY")

    print(run_prompt(prompt=prompt, model=model, api_key=api_key))


if __name__ == "__main__":
    main()
