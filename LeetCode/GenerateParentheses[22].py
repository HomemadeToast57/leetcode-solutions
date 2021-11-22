class Solution:
    def generateParenthesis(self, n: int) -> [str]:

        def backtrack(arr, left_curly, right_curly):
            # base case
            if left_curly == 0 and right_curly == 0:
                answer.append(''.join(arr))
                return

            # constraint for well-formed parentheses
            if left_curly <= right_curly:
                # explore all next candidate
                if left_curly:
                    backtrack(arr + ['('], left_curly - 1, right_curly)
                if right_curly:
                    backtrack(arr + [')'], left_curly, right_curly - 1)

            return

        answer = []
        backtrack(['('], n-1, n)

        return answer


s = Solution()
print(s.generateParenthesis(2))  # ['(())', '()()']


