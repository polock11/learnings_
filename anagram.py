class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            s = sorted(s)
            t = sorted(t)
            if s == t:
                return True
            else:
                return False

s = 'cat'
t = 'atct'
solution = Solution()
val = solution.isAnagram(s,t)
print(val)