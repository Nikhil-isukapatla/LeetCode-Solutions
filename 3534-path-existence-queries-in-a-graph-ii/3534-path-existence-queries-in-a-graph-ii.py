from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        order = sorted(range(n), key=lambda i: nums[i])

        position = [0] * n
        values = [0] * n

        for i, node in enumerate(order):
            position[node] = i
            values[i] = nums[node]

        LOG = n.bit_length()

        jump = [[0] * n for _ in range(LOG)]

        right = 0

        for i in range(n):
            right = max(right, i)

            while (
                right + 1 < n
                and values[right + 1] - values[i] <= maxDiff
            ):
                right += 1

            jump[0][i] = right

        # Binary lifting
        for k in range(1, LOG):
            for i in range(n):
                jump[k][i] = jump[k - 1][jump[k - 1][i]]

        answer = []

        for u, v in queries:

            left = position[u]
            right = position[v]

            if left > right:
                left, right = right, left

            if left == right:
                answer.append(0)
                continue

            steps = 0
            current = left

            # Take largest possible jumps
            for k in range(LOG - 1, -1, -1):
                nxt = jump[k][current]

                if nxt < right and nxt > current:
                    current = nxt
                    steps += 1 << k

            # Check if one final edge can reach target
            if jump[0][current] >= right:
                answer.append(steps + 1)
            else:
                answer.append(-1)

        return answer