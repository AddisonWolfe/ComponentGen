from lexer.lexer import lex
from lexer.lexer import lex_hierarchical  # your T-F-C post-processor

examples = [
    "make a large red rounded button with shadow",
    "create a green input with disabled property",
    "blue card outlined small",
    "just a red",
    "small button shadow blue rounded"
]

for ex in examples:
    print(f"\nInput: {ex}")
    
    # Step 1: Lex into tokens
    tokens = lex(ex)
    print("Tokens:", tokens)
    
    # Step 2: Apply T-F-C hierarchy
    component = lex_hierarchical(ex)
    print("Hierarchical Component:", component)