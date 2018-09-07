"""
10. Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression
matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
"""

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    def disp(m):
        for r in m: print(r)
    lens, lenp = len(s), len(p)
    # dp[i][j] 表示s取i长度,p取j长度的匹配结果
    dp = [[0]*(lenp+1) for _ in range(lens+1)]
    dp[0][0] = 1 # 空串与空模式是匹配的
    # 初始化dp的第一行, 即串为空时的匹配结果
    for j in range(1,lenp+1):
        dp[0][j] = dp[0][j-2] if p[j-1]=='*' else 0 # p的第j个字符应为 p[j-1]

    for i in range(1, lens+1):
        for j in range(1, lenp+1):
            if s[i-1]==p[j-1] or p[j-1]=='.':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1]=='*':
                dp[i][j] = dp[i][j-2] or (dp[i-1][j] if s[i-1]==p[j-2] or p[j-2]=='.' else 0)
                
    disp(dp)
    return bool(dp[lens][lenp])

s,p = 'xaabyc', 'xa*b.c'
s,p = "aa", "a*"
s,p = "ab", ".*"
s,p = "aab","c*a*b*"
s,p = "mississippi", "mis*is*p*."
ism = isMatch(s, p)
print(ism)
