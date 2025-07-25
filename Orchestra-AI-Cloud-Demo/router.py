import os
import requests

def call_phi3_groq(prompt):
    api_key = os.environ.get("GROQ_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "phi-3",
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=payload,
    )
    return response.json()["choices"][0]["message"]["content"]


def call_mixtral_together(prompt):
    api_key = os.environ.get("TOGETHER_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers=headers,
        json=payload,
    )
    return response.json()["choices"][0]["message"]["content"]
