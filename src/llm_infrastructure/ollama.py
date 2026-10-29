import os
from ollama import Client
from pathlib import Path

ollama_api = "https://ollama.com"
llm_prompts_path = Path(__file__).resolve().parent.parent / "llm_prompts"
default_prompt = (llm_prompts_path / "default.md").read_text(encoding="utf-8")

def call_ollama(prompt: str, model: str) -> str:
    client = Client(host = ollama_api, headers = {'Authorization': 'Bearer ' + os.environ['OLLAMA_API_KEY']})
    response = client.chat(model=model, messages=[{"role": "system", "content": default_prompt}, {"role": "user", "content": prompt}])
    return response.message["content"]

