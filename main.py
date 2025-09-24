# main.py
from llm_interface.interface import LLaMAInterface
from llm_interface.prompt_creator import create_prompt

def main():
    llm = LLaMAInterface(model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

    text = "a red button with blue text"
    
    # Wrap your raw text into a proper chat-style prompt
    prompt = create_prompt(text)
    chat_prompt = f"<s>[INST] {prompt} [/INST]"

    print("Prompt:")
    print(chat_prompt)

    response = llm.send_prompt(chat_prompt)
    print("\nResponse:")
    print(response)
    
if __name__ == "__main__":
    main()