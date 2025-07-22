"""
TC: O(N)
SC: O(N)
Logic:
Use a monotonic stack.
Instead of copying elements, use indexes to emulate copying
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        cap = 2*N
        res = [-1]*N
        stack= []
        for i in range(cap-1,-1,-1):
            val = nums[i%N]
            if i>N-1: #Second half, populate stack
                while(stack and val>=stack[-1]):
                    stack.pop()
                stack.append(val)
            elif i<N: #first half, populate stack as well as result array
                while(stack and val>=stack[-1]):
                    stack.pop()
                res[i] = stack[-1] if stack else -1
                stack.append(val)
        return res
