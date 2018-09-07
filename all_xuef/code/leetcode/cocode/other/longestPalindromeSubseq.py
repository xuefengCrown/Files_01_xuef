"""
516. Longest Palindromic Subsequence
"""
def longestPalindromeSubseq(s):
    """
    :type s: str
    :rtype: int
    """
    tab = {}
    letters = set(s)
    def longest(s):
        # 空串的最大子串的长度为0; 单字符的最大子串的长度为1
        if len(s) <= 1:
            return len(s)
        if len(s) == 2:
            return 2 if s[0]==s[1] else 1

        
        # 检查表格中是否备注了 s
        if s in tab.keys():
            print("find: ", s, "==", tab[s])
            return tab[s]
        # 没有备注s, 再计算
        maxLen = 0
        for l in letters:
            i,j = s.find(l), s.rfind(l)
            if i == j:
                maxLen = max(1, maxLen)
            else:
                maxNew = longest(s[i+1:j])
                maxLen = max(maxNew+2, maxLen)
                tab[s[i+1:j]] = maxNew
                tab[s] = maxNew+2
        return maxLen       
    return longest(s)

s = "hiddqscdxr"
print(longestPalindromeSubseq(s))   
