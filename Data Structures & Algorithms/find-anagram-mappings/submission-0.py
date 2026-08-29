class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a hashmap where hash[nums2[i]] = i
        nums2Dict = {}

        for i in range(len(nums2)):
            nums2Dict[nums2[i]] = i

        res = [] 
        for num in nums1:
            res.append(nums2Dict[num])
        
        return res



