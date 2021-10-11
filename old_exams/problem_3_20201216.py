def get_magic_triangle(n):
    result = [[1]]
    for i in range(2, n+1):
        len_of_line = i
        current_line = []
        first_el = result[i - 2][0]
        last_el = result[i - 2][-1]
        current_line.append(first_el)

        for index in range(1, len_of_line-1):
            current_el = result[i - 2][index - 1] + result[i - 2][index]
            current_line.append(current_el)
        current_line.append(last_el)

        result.append(current_line)
    return (result)


get_magic_triangle(7)