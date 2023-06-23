'''
    This was an amazing question of Floyd's Chain Detection Algorithm.
    We take slow pointer and fast pointer. 
    slow moves one step at a time
    and fast moves two steps
    if there is a chain then they meet eventually at some point. 
    Now if they meet at 1 then happy number, else not a happy number.
'''
class Solution:
    def square(self, n):
        result = 0
        while n>0:
            last = n%10
            result += last * last
            n = n//10
        return result
 
    def isHappy(self, n: int) -> bool:
        slowPointer = self.square(n)
        fastPointer = self.square(self.square(n))
        while slowPointer != fastPointer and fastPointer != 1:
            slowPointer = self.square(slowPointer)
            fastPointer = self.square(self.square(fastPointer))
        
        print(fastPointer==1)
        return fastPointer==1
    
a = Solution()
a.isHappy(n=2)