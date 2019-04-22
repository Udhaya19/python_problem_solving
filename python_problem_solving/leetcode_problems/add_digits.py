def add_digits(num):
    if num < 10:
        print(num)
    elif num // 9:
        print("9")
    else:
        num = num % 9
        print(num)


num = 18
add_digits(num)
