class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            largest=max(stones)
            stones.remove(largest)

            second_largest=max(stones)
            stones.remove(second_largest)

            if largest!=second_largest:
                diff=largest-second_largest
                stones.append(diff)

        return stones[0] if stones else 0
