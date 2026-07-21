class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=[]
        a=1
        for i in nums:
            r.append(a)
            a=a*i
        a=1
        for i in range(len(nums)-1,-1,-1):
            r[i]=r[i]*a
            a=a*nums[i]
        return r
