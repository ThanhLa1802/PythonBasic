import collections 
nums = [4,1,2,1,2]
def singleNumber(nums):
    dict_temp = collections.defaultdict(int)
    for x in nums:
        dict_temp[x] += 1
    for key, value in dict_temp.items():
        if value == 1:
            return key
def singleNumber2(nums):
    temp = nums[0]
    for i in range (1 , len(nums)):
        temp = temp ^ nums[i]
    return temp

#print(singleNumber2(nums))
