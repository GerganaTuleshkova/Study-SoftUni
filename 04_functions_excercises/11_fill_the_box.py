def fill_the_box(height, length, width, *args):

    volume = height * width * length
    cubes_left = 0
    for i in args:
        if i == "Finish":
            break
        if volume >= i:
            volume -= i
        else:
            difference = i - volume
            volume = 0
            cubes_left += difference

    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {cubes_left} more cubes."



print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

