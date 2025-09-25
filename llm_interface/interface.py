from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class StableCodeInterface:
    def __init__(self, model_name="stabilityai/stable-code-3b", device=None):
        """
        Load StabilityAI's Stable Code 3B model for code generation.
        """
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Loading {model_name} on {self.device}...")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto" if self.device == "cuda" else None
        )

    def send_prompt(self, prompt: str, max_tokens: int = 512) -> str:
        """
        Generate code from a given prompt.
        """
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=0.2,   # keeps output more deterministic for code
            top_p=0.95
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
