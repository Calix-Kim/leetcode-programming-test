class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # My solution
#         num_dict = {}
        
#         for i, num in enumerate(nums):
#             if num_dict.get(num, 0) == 0:
#                 num_dict[num] = [i]
#             else:
#                 num_dict[num].append(i)
        
#         for k in num_dict.keys():
#             if 2*k == target:
#                 if len(num_dict[k]) == 2:
#                     return sorted(num_dict[k])
#                 else:
#                     continue
#             if num_dict.get(target-k, 0):
#                 return sorted([num_dict[k][0], num_dict[target-k][0]])

        # Simple solution
        for i, num in enumerate(nums):
            remaining = target - num
            nums[i] = None
            
            if remaining in nums:
                return [i, nums.index(remaining)]