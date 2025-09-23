import re

class Component:
    def __init__(self, ctype, modifiers=None):
        self.ctype = ctype
        self.modifiers = modifiers if modifiers else {"COLOR": None, "PROPERTIES": []}

    def add_modifier(self, kind, value):
        if kind == "PROPERTY":
            self.modifiers["PROPERTIES"].append(value)
        else:
            self.modifiers[kind] = value

    def __str__(self):
        color = self.modifiers.get("COLOR")
        props = self.modifiers.get("PROPERTIES", [])
        props_str = ", ".join(props) if props else "None"
        return f"Component(type={self.ctype}, COLOR={color}, PROPERTIES=[{props_str}])"

# -------------------------------
# 1. Define token regexe
# -------------------------------
token_regex = re.compile(
    r"(?P<TYPE>\b(button|card|input|navbar)\b)|"
    r"(?P<PROPERTY>\b(text|rounded|shadow|disabled|outline|large|small|medium)\b)|"
    r"(?P<COLOR>\b(red|blue|green|black|white)\b)|"
    r"(?P<PREP>\b(about|above|across|after|against|along|among|around|at|before|behind|below|beneath|beside|between|beyond|by|despite|down|during|except|for|from|in|inside|into|like|near|of|off|on|onto|out|outside|over|past|since|through|throughout|to|toward|under|underneath|until|up|upon|with|within|without)\b)|"
    r"(?P<CONJ>\b(and|or|but|nor|for|yet|so)\b)|"
    r"(?P<A>\b(a)\b)"
)   #use 1 regex to maintain input order when identifying tokens


# -------------------------------
# 2. Basic lexer function
# -------------------------------
#returns a list of tuples formatted as ['('TYPE', 'VALUE')']
def lex(text: str):
    tokens = []
    for match in token_regex.finditer(text):
            tokens.append((match.lastgroup, match.group()))
    return tokens


def group_lex(tokens):
    components = []
    pending_modifiers = []
    new_comp = None
    for token in tokens:
        if token[0] == "TYPE":
            if new_comp:
                components.append(new_comp)
            new_comp = Component(token[1])
            if pending_modifiers:
                add_modifiers(pending_modifiers,new_comp)
                pending_modifiers.clear()

        elif token[0] == "PROPERTY":
            pending_modifiers.append(token)
        
        elif token[0] == "CONJ":
            if(pending_modifiers and new_comp):
                new_comp = add_modifiers(pending_modifiers,new_comp)
            pending_modifiers.clear()
    if new_comp:
        if pending_modifiers:
            add_modifiers(pending_modifiers,new_comp)
        components.append(new_comp)
    return components
    

def add_modifiers(mods, comp: Component):
    for mod in mods:
        comp.add_modifier(mod[0],mod[1])
    return comp