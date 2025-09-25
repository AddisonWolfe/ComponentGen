# main.py
from llm_interface.interface import StableCodeInterface
from llm_interface.prompt_creator import create_prompt

def main():
    llm = StableCodeInterface(model_name="stabilityai/stable-code-3b")

    text = "a red button with blue text"
    prompt = prompt = (
        "<SYSTEM>\n"
        "You are a helpful assistant that writes React JSX code.\n"
        "You should ONLY return code, with proper props and styles.\n"
        "Do not describe anything in words.\n"
        "Do not generate components that are not listed.\n"
        "</SYSTEM>\n"
        "<USER>\n"
        "Generate React JSX code for the following components:\n"
        "COMPONENT: Red button with black text 'Sign Up'\n"
        "COMPONENT: Green button with white text 'Login'\n"
        "</USER>\n"
        "<ASSISTANT>\n"
    )

    print("Prompt:")
    print(prompt)

    response = llm.send_prompt(prompt)
    print("\nResponse:")
    print(response)
    
if __name__ == "__main__":
    main()