def is_palindrome(given_number):
    number = given_number
    backwards_num = 0
    while number>0:
        remainder = number % 10
        backwards_num = (backwards_num * 10) + remainder
        number = number//10
    if backwards_num == given_number:
        return True
    else:
        return False


nums_list = input().split(", ")
for num in nums_list:
    print(is_palindrome(int(num)))

