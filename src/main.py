from pathlib import Path
from dotenv import load_dotenv

from src.llm_infrastructure.ollama import call_ollama

def main() -> None:
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    response = call_ollama("Was geht ab?", "gemma4:31b")
    print(response)

if __name__ == "__main__":
    main()
