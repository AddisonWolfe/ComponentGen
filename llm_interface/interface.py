from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class LLaMAInterface:
    def __init__(self, model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0", device=None):
        """
        Load a LLaMA or LLaMA-like model (TinyLlama, Phi, etc.) for text generation.
        """
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Loading {model_name} on {self.device}...")

        # Use Auto classes (works for both LLaMA and TinyLlama)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto" if self.device == "cuda" else None
        )

    def send_prompt(self, prompt: str, max_tokens: int = 200) -> str:
        """
        Generate text from a given prompt.
        """
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
