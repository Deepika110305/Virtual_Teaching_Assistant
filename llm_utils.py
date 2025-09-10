import subprocess

def ask_question_to_llm(context, question):
    prompt = f"Answer the following question using the context below:\n\nContext:\n{context}\n\nQuestion: {question}"
    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama3', prompt],
            stdout=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"LLM Error: {e}"
