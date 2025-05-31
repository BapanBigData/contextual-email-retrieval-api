def build_prompt(context: str, query: str) -> str:
    prompt = f"""
    You are a helpful assistant. Use the context below to answer or generate the requested email.

    Context:
    {context}

    Instruction:
    {query}

    Response:
    """
    
    return prompt