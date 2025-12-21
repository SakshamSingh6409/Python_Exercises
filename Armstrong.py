def ang_loop(n):
    num_str = str(n)
    num_digits = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** num_digits

    return total == n