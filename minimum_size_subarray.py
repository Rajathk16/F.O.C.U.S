class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        l=0
        m=float('inf')
        for i in range (0,len(nums)):
            sum=sum+nums[i]
            while sum>=target:
             length=i-l+1
             if length<m:
                m=length
             sum=sum-nums[l]
             l+=1
        return m if m!=float('inf') else 0
