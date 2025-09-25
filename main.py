# main.py
from llm_interface.interface import StableCodeInterface
from llm_interface.prompt_creator import create_prompt

def main():
    llm = StableCodeInterface(model_name="stabilityai/stable-code-3b")

    text = "a red button with blue text"
    prompt = prompt = (
"""Generate React JSX code for the following components. Only output code, with proper props and styles. Do NOT describe the components in words. Only generate code for the components listed below:

- Red button with black text 'Sign Up'
- Green button with white text 'Login'"""
    )

    print("Prompt:")
    print(prompt)

    response = llm.send_prompt(prompt)
    print("\nResponse:")
    print(response)
    
if __name__ == "__main__":
    main()