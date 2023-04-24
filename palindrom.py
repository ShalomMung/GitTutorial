
# sjekk om en str er en palindrom
def is_palindrom(x):
    """Returns True is x is a palidrom"""
    if not isinstance(x, str):
        raise ValueError(f"type {type(x)} is not supported!")
    print(f"Check if {x} is a palindrom")
    x = x.lower()
    x = x.strip()
    x = x.replace(" ", "")
    return "".join(list(reversed(x))) == x