import re

# -------------------------------
# 1. Define token regexes
# -------------------------------
TOKEN_SPEC = {
    "TYPE": r"\b(button|card|input)\b",
    "PROPERTY": r"\b(rounded|shadow|disabled|outlined|small|large|medium)\b",
    "COLOR": r"\b(red|blue|green|black|white)\b"
}

# Compile for efficiency
TOKENS = {name: re.compile(pattern, re.IGNORECASE)
          for name, pattern in TOKEN_SPEC.items()}


# -------------------------------
# 2. Basic lexer function
# -------------------------------
def lex(text: str):
    """Return list of (TOKEN_TYPE, value) tuples."""
    tokens = []
    for name, regex in TOKENS.items():
        for match in regex.finditer(text):
            tokens.append((name, match.group()))
    return tokens


# -------------------------------
# 3. Hierarchical lexer (T-F-C)
# -------------------------------
def lex_hierarchical(text: str):
    """Return a dict with TYPE, PROPERTIES, COLOR in hierarchical order."""
    tokens = lex(text)
    current = {
        "TYPE": None,
        "PROPERTIES": [],
        "COLOR": None
    }

    i = 0
    while i < len(tokens):
        token_type, value = tokens[i]

        if token_type == "TYPE":
            current["TYPE"] = value
            i += 1
            # lookahead for PROPERTY + COLOR pairs
            while i + 1 < len(tokens):
                t1, v1 = tokens[i]
                t2, v2 = tokens[i + 1]
                if t1 == "PROPERTY" and t2 == "COLOR":
                    current["PROPERTIES"].append(v1)
                    current["COLOR"] = v2
                    i += 2
                else:
                    break
        elif token_type == "COLOR" and current["TYPE"] is None:
            # standalone color without type
            current["COLOR"] = value
            i += 1
        elif token_type == "PROPERTY":
            # property without TYPE or COLOR, optional to include
            current["PROPERTIES"].append(value)
            i += 1
        else:
            i += 1

    return current