from lexer.lexer import lex

examples = [
    "make a large red rounded button with shadow and a blue navbar",
    "make a input field with black text"
]

for ex in examples:
    print(f"\nInput: {ex}")
    
    # Step 1: Lex into tokens
    tokens = lex(ex)
    print("Tokens:", tokens)
    
    # Step 2: Apply T-F-C hierarchy
    #component = lex_hierarchical(ex)
   # print("Hierarchical Component:", component)