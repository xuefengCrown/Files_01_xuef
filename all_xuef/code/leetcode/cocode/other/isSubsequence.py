"""
392. Is Subsequence (dynamic programming)
Given a string s and a string t, check if s is subsequence of t.
"""
def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) == 0:
        return True
    s0 = s[0]
    for idx, letter in enumerate(t):
        if s0 == letter:
            return isSubsequence(s[1:], t[idx:])
    return False

s = "let"
t = "leeeeetcode"
print(isSubsequence(s, t))