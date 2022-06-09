def incrementer(nums):
    plus = 1
    for i in range(0,len(nums)):
        if nums[i] + plus > 9:
            nums[i] += plus
            nums[i] %= 10
        else:
            nums[i] += plus
        plus += 1
    return nums

print(incrementer([4, 6, 7, 1, 3]))