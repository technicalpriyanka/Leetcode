class Solution:
    def repairCars(self, a: List[int], k: int) -> int:
        return bisect_left(range(min(a)*k*k),k,key=lambda t:sum(isqrt(t//v) for v in a))