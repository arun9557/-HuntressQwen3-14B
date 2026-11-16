import requests
import json
import sys

OLLAMA_API = "http://127.0.0.1:11434/api/chat"
MODEL = "HuntressQwen3"

def chat(prompt, think=True):
    payload = {
        "model": MODEL,
        "stream": False,
        "think": think,
        "messages": [{"role": "user", "content": prompt}],
        "options": {
            "temperature": 0.4,
            "top_p": 0.85,
            "repeat_penalty": 1.15,
            "num_ctx": 16384
        }
    }
    
    try:
        r = requests.post(OLLAMA_API, json=payload, timeout=120)
        r.raise_for_status()
        data = r.json()
        msg = data.get("message", {})
        
        if think and msg.get("thinking"):
            print("\n[Thinking]")
            print(msg["thinking"].strip())
            print("[/Thinking]\n")
            
        print("[Response]")
        print(msg.get("content", "").strip())
        print()
    except Exception as e:
        print(f"Error communicating with Ollama: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        chat(query)
    else:
        print("=== HuntressQwen3 Interactive Terminal ===")
        print("Model: HuntressQwen3 (v5 - Uncensored Agentic 14B)")
        print("Type 'exit' or 'quit' to close.\n")
        while True:
            try:
                user_input = input("Huntress> ").strip()
                if not user_input:
                    continue
                if user_input.lower() in ["exit", "quit"]:
                    break
                chat(user_input)
            except KeyboardInterrupt:
                print("\nExiting.")
                break
