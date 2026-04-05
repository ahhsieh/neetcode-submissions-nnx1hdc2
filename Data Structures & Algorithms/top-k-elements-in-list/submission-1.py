class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elementCounts = {}
        maxCount = 0
        for num in nums: # time O(n), space O(n)
            count = elementCounts.get(num, 0) + 1
            elementCounts[num] = count
            if count > maxCount:
                maxCount = count
        print(f"{elementCounts}")

        buckets = [ [] for i in range(maxCount+1) ]
        for element, count in elementCounts.items(): # time O(2001), space O(n+n)
            buckets[count].append(element)
        print(f"{buckets}")

        count = maxCount
        result = []
        while len(result) < k: # time O(k <= n), space O(n)
            result = result + buckets[count]
            count -= 1

        return result

        