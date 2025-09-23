# main.py
from llm_interface.interface import LLaMAInterface
from llm_interface.prompt_creator import create_prompt

def main():
    llm = LLaMAInterface(model_name="meta-llama/CodeLlama-7b-Instruct-hf")

    text = "a red button with blue text"
    prompt = create_prompt(text)

    print("Prompt:")
    print(prompt)

    response = llm.send_prompt(prompt)
    print("\nResponse:")
    print(response)
    
if __name__ == "__main__":
    main()