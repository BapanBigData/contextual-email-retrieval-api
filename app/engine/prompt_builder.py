def build_prompt(context: str, query: str) -> str:
    prompt = f"""
    You are a helpful assistant. Use the context below to answer or generate response of common email types.

    Context:
    {context}

    Instruction:
    {query}

    Response:
    """
    
    return prompt