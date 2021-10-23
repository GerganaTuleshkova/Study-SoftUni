def list_manipulator(numbers: list, action, from_where, *args):
    if action == "add":
        numbers_to_add = list(args)
        if from_where == "beginning":
            numbers = numbers_to_add + numbers
        else:
            numbers = numbers + numbers_to_add

    elif action == "remove":
        if from_where == "beginning":
            if args:
                numbers_to_remove = args[0]

                for _ in range(min(numbers_to_remove, len(numbers))):
                    numbers.pop(0)
            elif not args and len(numbers) > 0:
                numbers.pop(0)
        elif from_where == "end":
            if args:
                numbers_to_remove = args[0]

                for _ in range(min(numbers_to_remove, len(numbers))):
                    numbers.pop()
            elif not args and len(numbers) > 0:
                numbers.pop()

    return numbers


print(list_manipulator([1,2,3], "remove", "end"))                   
print(list_manipulator([1,2,3], "remove", "beginning"))             
print(list_manipulator([1,2,3], "add", "beginning", 20))            
print(list_manipulator([1,2,3], "add", "end", 30))                  
print(list_manipulator([1,2,3], "remove", "end", 2))                
print(list_manipulator([1,2,3], "remove", "beginning", 2))          
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))    
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))          
