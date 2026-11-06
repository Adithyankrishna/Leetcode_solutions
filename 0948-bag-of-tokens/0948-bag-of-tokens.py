class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()

        left = 0
        right = len(tokens) - 1

        score = 0
        maxscore = 0

        while left <= right:

            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1

                maxscore = max(maxscore, score)
            elif score > 0 and left < right:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return maxscore