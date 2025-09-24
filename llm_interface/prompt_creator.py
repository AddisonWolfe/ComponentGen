from lexer.lexer import lex, group_lex, Component

FRAMEWORK = "React"
PROMPT_BASE = f"Please create the following components using {FRAMEWORK}. Please only return code:\n"

def create_prompt(text: str):
    tokens = lex(text)
    components = group_lex(tokens)
    prompt = PROMPT_BASE
    for comp in components:
        # Turn Component(...) into human-readable instructions for code generation
        props = ", ".join(comp.modifiers.get("PROPERTIES", [])) if comp.modifiers.get("PROPERTIES") else "None"
        color = comp.modifiers.get("COLOR", "None")
        prompt += f"A {color} {comp.ctype} with properties: {props}\n"
    return prompt

