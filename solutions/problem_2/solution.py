class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [nums[0]**2]
        for b in range(len(nums)):
            if nums[b]>=0:
                break;
        a=b-1
        ans=[]
        while(a>=0)and(b<len(nums)):
            if (nums[a]**2)<=(nums[b]**2):
                ans.append(nums[a]**2)
                a-=1
            else:
                ans.append(nums[b]**2)
                b+=1
        if a>=0:
            for i in range(a,-1,-1):
                ans.append(nums[i]**2)
        if b<len(nums):
            for i in range(b,len(nums)):
                ans.append(nums[i]**2)
        return ans
