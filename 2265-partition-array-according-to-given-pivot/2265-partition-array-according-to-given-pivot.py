class Solution:
    def pivotArray(self, num: List[int], pivot: int) -> List[int]:
        l1=[]
        l2=[]
        l3=[]
        i=0
        m=len(num)
        for nu in num:
            if nu==pivot:
                l1.append(nu)
            elif nu>pivot:
                l2.append(nu)
            else:
                l3.append(nu)
        return l3+l1+l2