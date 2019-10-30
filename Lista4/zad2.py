def build_triangle(size):
    for x in range(size-1):
        print("*", end='')
        if x == 0:
            print()
        if x > 0:
            for y in range(x - 1):
                print(" ", end='')

            print("*")
    for x in range(size):
        print("*", end='')


build_triangle(5)
