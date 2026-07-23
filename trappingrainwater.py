class Solution:
    def trap(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        lmax=h[l]
        rmax=h[r]
        sum=0
        while l<r:
            if lmax<=rmax:
                l+=1
                lmax=max(lmax,h[l])
                sum+=(lmax-h[l])
            else:
                r-=1
                rmax=max(rmax,h[r])
                sum+=(rmax-h[r])
        return sum
