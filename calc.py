from operations import add, subtract, multiply, divide
from memory import get_last_result, set_last_result


ops = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(text):
    parts = text.split()
    if len(parts) == 3:
        return calculate_fresh(parts)

    if len(parts) == 2:
        return calculate_add_on(parts)

    raise ValueError("Expected input like: number operator number or operator number")


def calculate_fresh(parts):
    a_text, operator, b_text = parts
    result = calculate_operation(a_text, operator, b_text)
    set_last_result(result)
    return result


def calculate_add_on(parts):
    operator, b_text = parts
    last_result = get_last_result()

    if last_result is None:
        raise ValueError("No previous result")

    if operator == "-":
        result = calculate_operation(str(last_result), operator, b_text)
    else:
        result = calculate_operation(str(last_result), operator, b_text)

    set_last_result(result)
    return result


def calculate_operation(a_text, operator, b_text):
    if operator not in ops:
        raise ValueError("Unknown operator")

    if not is_number(a_text) or not is_number(b_text):
        raise ValueError("Operands must be numbers")

    a = float(a_text)
    b = float(b_text)

    return ops[operator](a, b)


def run():
    errors = 0

    while True:
        text = input("> ")

        if text == "stop":
            break

        try:
            result = calculate(text)
            print(result)
            errors = 0
        except ValueError as error:
            print(error)
            errors = errors + 1

            if errors == 3:
                break


def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    run()
