def generate_expressions(nums, current_result=0, current_expression=""):
    if not nums:
        print(f"{current_expression}={current_result}")
        return
    generate_expressions(nums[1:], current_result+nums[0], f"{current_expression}+{nums[0]}")
    generate_expressions(nums[1:], current_result-nums[0], f"{current_expression}-{nums[0]}")


nums = [int(n) for n in input().split(", ")]
generate_expressions(nums)