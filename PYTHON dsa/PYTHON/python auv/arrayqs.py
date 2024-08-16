def two_sum(nums, target):
  complements = {}
  for i, num in enumerate(nums):
    if num in complements:
      return [complements[num], i]
    else:
      complements[target - num] = i
  return []

# Example input and output
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target)) 
  
