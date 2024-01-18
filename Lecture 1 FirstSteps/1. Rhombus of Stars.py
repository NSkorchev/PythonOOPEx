def print_row(stars, count):
    print(" " * (stars - count), end="")
    print(*['*'] * count)


def print_triangle(stars):
    for count in range(1, stars + 1):
        print_row(stars, count)


def print_reversed_triangle(stars):
    for count in range(stars - 1, 0, -1):
        print_row(stars, count)


def print_square(stars):
    for count in range(stars):
        print_row(stars, stars)


def print_rhombus(stars):
    print_triangle(stars)
    print_reversed_triangle(stars)


stars = int(input())

print_rhombus(stars)
# print("")
# print_triangle(stars)
# print("")
# print_square(stars)