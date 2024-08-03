def calculate_check_digit(data):
    weights = [7, 3, 1]
    total = 0
    for i, char in enumerate(data):
        if char.isdigit():
            value = int(char)
        elif char.isalpha():
            value = ord(char) - 55
        elif char == '<':
            value = 0
        total += value * weights[i % len(weights)]
    return str(total % 10)
