def find_the_smallest(num_1,num_2, num_3):
    numbers_list = [num_1, num_2, num_3]
    smallest_num = min(numbers_list)
    return smallest_num


n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
print(find_the_smallest(n_1, n_2, n_3))