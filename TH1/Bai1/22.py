def find4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1
  return count

print(find4([1, 4, 6, 7, 4, 5, 4, 7, 8, 6]))
print(find4([1, 4, 6, 4, 7, 4, 5, 4, 4, 4]))