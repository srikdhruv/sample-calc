from operations import add, subtract, multiply, divide


ops = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(text):
    parts = text.split()
    if len(parts) != 3:
        raise ValueError("Expected input like: number operator number")

    a_text, operator, b_text = parts

    if operator not in ops:
        raise ValueError("Unknown operator")

    if not is_number(a_text) or not is_number(b_text):
        raise ValueError("Operands must be numbers")

    a = float(a_text)
    b = float(b_text)

    return ops[operator](a, b)


def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    try:
        result = calculate(input("> "))
        print(result)
    except ValueError as error:
        print(error)
