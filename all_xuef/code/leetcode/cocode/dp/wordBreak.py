"""
139. Word Break
Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    # 没有记忆化已经得到的结果, 会超时
    def helper1(s, wordDict, parts): # s 是否能分解为 wordDict 中的词
        if not s: return True
        words_startwith_s0 = [word for word in wordDict if word[0]==s[0]]
        words = list(filter(lambda x:s.startswith(x), words_startwith_s0))
        for w in words:
            if helper1(s[len(w):], wordDict, parts):
                parts.append(w)
                return True
        return False
    def helper(s, wordDict, tab): # s 是否能分解为 wordDict 中的词
        if not s: return True
        words_startwith_s0 = [word for word in wordDict if word[0]==s[0]]
        words = list(filter(lambda x:s.startswith(x), words_startwith_s0))
        for w in words:
            can = tab.get(s[len(w):])
            if can is None: # 表中没有该结果, 才计算
                can = helper(s[len(w):], wordDict, tab)
                tab[s[len(w):]] = can
                if can: return True
            elif can is True: return True
            else: tab[s[len(w):]] = False
        return False
    tab = {}
    rs = helper(s, wordDict, tab)
    return rs
    
s, wordDict = "catsandog", ["cats", "dog", "sand", "and", "cat"]
s, wordDict = "applepenapple", ["apple", "pen"]
#s, wordDict = "leetcode", ["leet", "code"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
rs = wordBreak(s, wordDict)
print(rs)
