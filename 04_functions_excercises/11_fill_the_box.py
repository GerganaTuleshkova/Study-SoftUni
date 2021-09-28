def fill_the_box(*args):
    height = args[0]
    length = args[1]
    width = args[2]
    volume = height * width * length
    cubes_left = 0
    for i in args[3:]:
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

