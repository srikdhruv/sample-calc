from operations import add, subtract


ops = {
    "+": add,
    "-": subtract,
}


def calculate(text):
    parts = text.split()
    a = float(parts[0])
    operator = parts[1]
    b = float(parts[2])

    if len(parts) != 3:
        raise ValueError("Expected input like: number operator number")

    if operator not in ops:
        raise ValueError("Unknown operator")

    return ops[operator](a, b)


if __name__ == "__main__":
    try:
        result = calculate(input("> "))
        print(result)
    except ValueError as error:
        print(error)
