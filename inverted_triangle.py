def inverted_triangle(num):
    num = ( num - 1 ) *2
    space = 0
    for x in range(num, 0, -2):
        char = f" * " * x
        print("\n","   "*space,char[:-2])
        space += 1



inverted_triangle(20)
