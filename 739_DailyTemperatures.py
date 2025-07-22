"""
TC: O(N)
SC: O(N)
Logic:
- Use Monotonic stack.
- Start processing from end.
- If element is less than stack top, update result array and append element to stack
- If element is greater or equal to stack top and stack isnt empty, keep popping, then update result array and append element to stack
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while(stack and temperatures[i]>=stack[-1][0]):
                stack.pop()
            res[i] = stack[-1][1]-i if stack else 0
            stack.append([temperatures[i],i])
        return res