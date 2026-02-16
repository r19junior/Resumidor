import os, requests

def generate_summary(text):
    """Genera un resumen breve con Llama 3 via Ollama."""
    url = os.getenv('OLLAMA_URL', 'http://localhost:11434/api/generate')
    prompt = f"Resume en 1 oración (max 15 palabras): {text[:5000]}"
    try:
        res = requests.post(url, json={"model": os.getenv('AI_MODEL', 'llama3'), "prompt": prompt, "stream": False})
        res.raise_for_status()
        return res.json().get('response', '').strip().replace('Resumen:', '').strip()
    except Exception as e:
        print(f"❌ AI Error: {e}")
        return None
