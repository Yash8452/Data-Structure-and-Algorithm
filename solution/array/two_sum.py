def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)-1):
        for j in range (i+1,len(nums)):
            if(nums[i]+nums[j]) == target:
                return [nums[i],nums[j]] 
            # print(nums[i],nums[j])



nums = [2,7,11,15] 
target = 9

print(twoSum(nums,target))