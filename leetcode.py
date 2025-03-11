
def sum_num(nums,target):
    
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                
                return [i,j]
    return -1
print(sum_num([2,7,11,15],9))
        

square=[x**2 for x in range(1,6)]
print(square)