def print_diamond(min_width, max_width):
    if min_width > max_width:
        print("Warning: Minimum width is greater than maximum width.")
        return

    if (max_width - min_width) % 2 != 0:
        print("Warning: The difference between maximum and minimum widths is not a multiple of 2.")
        return

    step = 2
    for width in range(min_width, max_width + 1, step):
        spaces = (max_width - width) // 2
        if width == 1:
            print(' ' * spaces + '*')
        elif width == min_width:
            print(' ' * spaces + '*' * width)
        else:
            print(' ' * spaces + '*' + ' ' * (width - 2) + '*')

    for width in range(max_width - step, min_width - 1, -step):
        spaces = (max_width - width) // 2
        if width == 1:
            print(' ' * spaces + '*')
        elif width == min_width:
            print(' ' * spaces + '*' * width)
        else:
            print(' ' * spaces + '*' + ' ' * (width - 2) + '*')


try:
    min_width = int(input("Enter minimal width: "))
    max_width = int(input("Enter maximal width: "))
    print_diamond(min_width, max_width)
except ValueError:
    print("Invalid input. Please enter integers for the widths.")












