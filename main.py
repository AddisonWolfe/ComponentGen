# main.py
from llm_interface.interface import StableCodeInterface
from llm_interface.prompt_creator import create_prompt

def main():
    llm = StableCodeInterface(model_name="stabilityai/stable-code-3b")

    text = "a red button with blue text"
    prompt = create_prompt(text)

    print("Prompt:")
    print(prompt)

    response = llm.send_prompt(prompt)
    print("\nResponse:")
    print(response)
    
if __name__ == "__main__":
    main()