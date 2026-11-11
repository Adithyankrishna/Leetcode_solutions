class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        stack = []
        visited = set()

        for char in s:

            freq[char] -= 1

            if char in visited:
                continue

            while stack and stack[-1] > char and freq[stack[-1]] > 0:
                removed = stack.pop()
                visited.remove(removed)

            stack.append(char)
            visited.add(char)

        return "".join(stack)