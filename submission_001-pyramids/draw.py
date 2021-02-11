

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape_list = ["pyramid", "square", "triangle", "re_triangle", "rectangle", "diamond"]
    while True:
        shape_type = input("Shape?: ")
        shape_type = shape_type.lower()
        if len(shape_type) == 0:
            continue
        if shape_type in shape_list:
            break
        else:
            continue

    return shape_type


# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:    
        height = input("Height?: ")
        if not height.isdigit():
            continue
        if len(height) == 0:
            continue
        if int(height) < 0:
            continue
        if int(height) > 80:
            continue
        if int(height) > 0 and int(height) < 80:
            break
    return int(height)


# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == False:
         for row in range(0, height):
            for col in range(0, height - row - 1):
                print(" ", end="")
            for col in range(0, (row * 2) + 1):
                print('*', end="")
            print()
    if outline == True:
        m = height -1
        shape = 1
        print(" " * (height - 1) + "*")
        shape += 2
        m -= 1
        for row in range(height - 2):
            print(" " * m + "*" + " " * (shape - 2) + "*")
            m = m - 1
            shape  = shape + 2
        print("*" * (shape))


# TODO: Step 3
def draw_square(height, outline):
    if outline == False:
        row = 0
        for row in range(0, height):
            col = 0
            for col in range(0, height):
                col = col + 1
                print('*', end= "")
            row = row + 1
            print()
    if outline == True:
        for row in range(0, height):
            for col in range(0, height):
                if(row == 0 or row == height - 1 or col == 0 or col == height - 1):
                    print("*", end='')
                else:
                    print(' ', end='')
            print()    


# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        row = 0
        for row in range(0, height):
            col = 0
            for row in range(0, row + 1):
                print("*", end='')
            print()
    if outline == True:
        for row in range(height):
            for col in range(row + 1):
                if row == 0 or row == height - 1 or col == 0 or col == row:
                    print("*", end= "")
                else:
                    print(" ", end= "")
            print()


def draw_reverse_triangle(height, outline):
    if outline == False:
        for row in range(height, 0, -1):
            for col in range(1, row + 1):
                print("*", end="")
            print()
    if outline == True:
        for row in range(0, height):
            for col in range(0, height):
                if(col == 0 or row == 0 or col + row == height - 1):
                    print("*", end="")
                else:
                    print(end=" ")
            print()

def draw_rectangle(height, outline):
    if outline == False:
        m = height * 2
        for row in range(0, height):
            for col in range(0, m):
                print("*", end='')
            print()
    if outline == True:
        m = height + 2
        for row in range(height):
            for col in range(m):
                if(row == 0 or row == (height - 1) or col == 0 or col == (m - 1)):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print() 


def draw_diamond(height, outline):
    if outline == False:
        for row in range(height):
            print(" " * (height - row - 1), end="")
            for col in range(row + 1):
                print("* ", end="")
            print()
        for row in range(height - 1):
            print(" " * (row + 1), end="")
            for col in range(height - row - 1):
                print("* ", end="")
            print()
    if outline == True:
        m = height - 1
        n = 1
        print(" " * (height - 1) + "*")
        n += 2
        m -= 1
        for row in range(height - 2):
            print(" " * (m) + "*" + " " * (n - 2) + "*")
            m = m - 1
            n = n + 2
        for row in range(height - 1):
            print(" " * (m) + "*" + " " * (n - 2) + "*")
            m = m + 1
            n = n - 2
        print(" " * (height - 1) + "*")    


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "re_triangle":
        draw_reverse_triangle(height, outline)
    elif shape == "rectangle":
        draw_rectangle(height, outline)
    elif shape == "diamond":
        draw_diamond(height, outline)
    else:
        print("choose a valid shape")


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (y/N): ")
    if outline == "y":
        return True
    if outline == "N":
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)
