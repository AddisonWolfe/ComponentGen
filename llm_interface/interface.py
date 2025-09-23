from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

class LLaMAInterface:
    def __init__(self, model_name="meta-llama/Llama-7b-hf", device=None):
        """
        Load a LLaMA model for text generation.
        """
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Loading LLaMA model on {self.device}...")
        self.tokenizer = LlamaTokenizer.from_pretrained(model_name)
        self.model = LlamaForCausalLM.from_pretrained(
            model_name,
            device_map="auto" if self.device == "cuda" else None
        )

    def send_prompt(self, prompt: str, max_tokens: int = 200) -> str:
        """
        Generate text from a given prompt.
        """
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)