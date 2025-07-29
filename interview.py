# Use a generator expression to count uppercase letters
paragraph = """Your paragraph goes here. For Example: This Is A Sample TEXT."""
capital_count = sum(1 for c in paragraph if c.isupper())
print("Number of capital letters:", capital_count)


# Python code to check balanced parentheses/brackets
def is_balanced(text: str):
    stack = []
    brackets = {'(': ')', '[': ']'}

    for char in text:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    return not stack


paragraph = "This is a (sample [text]) with (balanced) brackets."

if is_balanced(paragraph):
    print("Brackets and parentheses are balanced.")
else:
    print("Brackets and parentheses are NOT balanced.")
