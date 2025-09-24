from lexer.lexer import lex, group_lex, Component

FRAMEWORK = "React"
PROMPT_BASE = f"Please create the following components using {FRAMEWORK}. Please only return code:\n"

def create_prompt(text: str):
    tokens = lex(text)
    components = group_lex(tokens)
    prompt = PROMPT_BASE
    prompt += "A red button with black text"
    return prompt

