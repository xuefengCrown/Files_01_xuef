"""
140. Word Break II
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
        if not s: return [[]]
        words_startwith_s0 = [word for word in wordDict if word[0]==s[0]]
        words = list(filter(lambda x:s.startswith(x), words_startwith_s0))
        for w in words:
            can = tab.get(s[len(w):])
            if can is None: # 表中没有该结果, 才计算
                can = helper(s[len(w):], wordDict, tab)
                if can:
                    tab[s[len(w):]] = can
                    tab[s] = (tab[s] if tab.get(s) else []) + [[w]+ circum for circum in can]
                else:
                    tab[s[len(w):]] = []
            elif can:
                tab[s] = (tab[s] if tab.get(s) else []) + [[w]+ circum for circum in can]
            
        print(s)  
        return tab[s] if tab.get(s) else []
    tab = {} # key为s, value为[[]]
    rs = helper(s, wordDict, tab)
    print(tab)
    return list(map(lambda x:" ".join(x), rs))
    
s, wordDict = "catsandog", ["cats", "dog", "sand", "and", "cat"]
s, wordDict = "applepenapple", ["apple", "pen"]
#s, wordDict = "leetcode", ["leet", "code"]
#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
#wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
s, wordDict = "catsanddog", ["cat", "cats", "and", "sand", "dog"]
#s, wordDict = "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
s, wordDict = "catsandog", ["cats", "dog", "sand", "and", "cat"]
rs = wordBreak(s, wordDict)
print(rs)
