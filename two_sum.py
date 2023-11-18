# nput: nums = [2,7,11,15], target = 9
# Output: [0,1]


def twoSum(nums, target):
    #l  = sorted([x for x in nums if x<=target])
    nums_c = sorted(nums[:])
    to_add = []
    for i in range(len(nums_c)):
        v = target - nums_c[i]
        if v in nums_c:
            to_add.append(nums_c[i])
            to_add.append(v)
            break
    return [index for index, element in enumerate(nums) if element in to_add]



nums = [3,2,3]
target = 6
print(twoSum(nums,target))


