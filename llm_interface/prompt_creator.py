from lexer.lexer import lex, group_lex, Component

FRAMEWORK = "React"
PROMPT_BASE = """Generate React JSX code for the following components.
                Do NOT describe them in words. Only return JSX code.
                Include proper props and styles. 
                Do not generate components not listed below:\n"""

def create_prompt(text: str):
    tokens = lex(text)
    components = group_lex(tokens)
    prompt = PROMPT_BASE
    prompt += "Red button with black text \"Sign Up\""
    return prompt

