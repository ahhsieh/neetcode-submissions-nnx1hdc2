class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elementCounts = {}
        maxCount = 0
        for num in nums: # O(n)
            count = elementCounts.get(num, 0) + 1
            elementCounts[num] = count
            if count > maxCount:
                maxCount = count
        print(f"{elementCounts}")

        buckets = [ [] for i in range(maxCount+1) ]
        for element, count in elementCounts.items(): # O(2001)
            buckets[count].append(element)
        print(f"{buckets}")

        count = maxCount
        result = []
        while len(result) < k:
            result = result + buckets[count]
            count -= 1

        return result
        # iterate through nums, increment counts store in hashmap O(n)
        #.  store top k counts, corresponding elements, if new count is > least of top k counts, remove lost count, add new count O(k)
        # time O(n*k) space O(n + k)

        # array counts [[], [elem1, elem2]]
        # array element Counts [ count for -1000, count for -999, ..., count for 1000]

        