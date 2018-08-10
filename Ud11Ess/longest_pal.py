class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = list(s)
        y = x.copy()
        y.reverse()
        longest = []
        so_far = []
        for i, l in enumerate(x):
            if l == y[i]:
                so_far.append(l)
            else:
                if len(so_far)> len(longest):
                    longest = so_far.copy()
                    so_fat = []
        return ''.join(longest)