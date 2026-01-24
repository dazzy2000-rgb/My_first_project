

nums=[15,14,21,35,7,2]
for i in range (len(nums)):
    for j in range (i+1,len(nums)):
         if nums[i] > nums[j]:
            nums[j],nums[i] = nums[i],nums[j]
print(nums)

