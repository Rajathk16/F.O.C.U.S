class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        marea=0
        while l<r:
            if h[l]<=h[r]:
                area=h[l]*(r-l)
            else:
                area=h[r]*(r-l)
            marea=max(marea,area)
            if h[l]<=h[r]:
                l+=1
            else:
                r-=1
        return marea
