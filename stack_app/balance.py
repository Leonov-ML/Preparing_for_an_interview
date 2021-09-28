from stack_app.stack import Stack

PAIRS = ('()', '[]', '{}')

stack = Stack()

def check_is_line_correct(line):
    for char in line:
        if char in '([{':
            stack.push(char)
        else:
            if stack.isEmpty():
                return False
            else:
                if stack.peek() + char in PAIRS:
                    stack.pop()
                else:
                    return False

    return stack.isEmpty() or False
