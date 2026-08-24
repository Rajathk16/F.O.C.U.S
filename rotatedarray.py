class Solution:
    def rotate(self, a: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rev(l,r):
            while l<r:
             a[l],a[r]=a[r],a[l]
             l+=1
             r-=1
        k=k%len(a)
        rev(0,len(a)-1)
        rev(0,k-1)
        rev(k,len(a)-1)
        
