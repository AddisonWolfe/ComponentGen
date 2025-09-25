# main.py
from llm_interface.interface import StableCodeInterface
from llm_interface.prompt_creator import create_prompt

def main():
    llm = StableCodeInterface(model_name="stabilityai/stable-code-3b")

    text = "a red button with blue text"
    prompt = prompt = (
"""You are a helpful assistant that writes React JSX code.
You should ONLY return code, with proper props and styles.
Do not describe anything in words.
Do not generate components that are not listed.

Generate React JSX code for the following components:
COMPONENT: Red button with black text 'Sign Up'
COMPONENT: Green button with white text 'Login'"""
    )

    print("Prompt:")
    print(prompt)

    response = llm.send_prompt(prompt)
    print("\nResponse:")
    print(response)
    
if __name__ == "__main__":
    main()