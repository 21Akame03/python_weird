def triangle(number) :
    if number == 1:
        return 1

    print("*"*number)
    return triangle(number - 1)

triangle(100)
