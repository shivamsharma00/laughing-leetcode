class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ranges = defaultdict(list)
        uniq = set()
        res = 0

        for num in nums:

            if num in uniq:
                continue
            uniq.add(num)
            
            left = right = num

            if ranges[num-1]:
                left = ranges[num-1][0]
            if ranges[num+1]:
                right = ranges[num+1][1]
            
            ranges[left] = [left, right]
            ranges[right] = [left, right]
            res = max(res, right-left+1)

        return res 