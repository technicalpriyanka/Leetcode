class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Compute sum and zero count for nums1
        sum1, cnt1 = 0, 0
        for x in nums1:
            if x == 0:
                cnt1 += 1
            else:
                sum1 += x
        
        # Compute sum and zero count for nums2
        sum2, cnt2 = 0, 0
        for x in nums2:
            if x == 0:
                cnt2 += 1
            else:
                sum2 += x
        
        # Case 1: Both have no zeros
        if cnt1 == 0 and cnt2 == 0:
            return sum1 if sum1 == sum2 else -1
        
        # Case 2: nums1 has no zeros
        if cnt1 == 0:
            if cnt2 == 0:
                return sum1 if sum1 == sum2 else -1
            # nums2 has zeros, needs to reach sum1
            if sum2 <= sum1 and sum2 + cnt2 <= sum1:
                return sum1
            return -1
        
        # Case 3: nums2 has no zeros
        if cnt2 == 0:
            if cnt1 == 0:
                return sum2 if sum1 == sum2 else -1
            # nums1 has zeros, needs to reach sum2
            if sum1 <= sum2 and sum1 + cnt1 <= sum2:
                return sum2
            return -1
        
        # Case 4: Both have zeros
        return max(sum1 + cnt1, sum2 + cnt2)