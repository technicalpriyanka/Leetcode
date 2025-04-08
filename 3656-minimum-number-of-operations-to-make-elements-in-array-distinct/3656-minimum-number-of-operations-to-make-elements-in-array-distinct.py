class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        
        while True:
    
            if len(nums)<=3:
                if len(nums)==3:
                    if nums[0]!=nums[1] and nums[1]!=nums[2] and nums[2]!=nums[0]:
                        break
                    else:
                        c=c+1
                        break
                if len(nums)==2:
                    if nums[0]!=nums[1] :
                        break
                    else:
                        c=c+1
                        break
                if len(nums)==1:
                    break
            l=[]
            n=len(nums)
            for i in nums:
                if i not in l:
                    l.append(i)
                else:
                    nums=nums[3:]
                    c=c+1
                    break
            if len(l)==n:
                break
        return c