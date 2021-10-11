nums = [3, 2, -2, 2, 5]
import collections
def subarraySum(nums, k):
    aSum_dict = collections.defaultdict(int)
    aSum_dict[0] = 1
    aSum = 0
    cnt = 0
    for x in nums:
        aSum += x
        if aSum_dict[aSum - k]:
            cnt += aSum_dict[aSum - k]
        aSum_dict[aSum] += 1
    return cnt

subarraySum(nums , 5)
