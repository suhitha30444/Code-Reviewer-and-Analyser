import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def analyze_code(code, language):
    prompt = f"""You are an expert code reviewer. Analyze the following {language} code and provide:
1. **Bugs / Issues** - List any bugs or potential errors.
2. **Time & Space Complexity** - State the Big-O complexity.
3. **Improvements** - Suggest 2-3 concrete improvements.
4. **Cleaned Version** - Provide a cleaner rewritten version.

Code:
```{language}
{code}
```
Be concise and structured."""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 800,
        "temperature": 0.3
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
    print("Response:", response.status_code, response.text[:300])

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    else:
        return f"API Error {response.status_code}: {response.text[:500]}"