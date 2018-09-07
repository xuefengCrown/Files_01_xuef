"""
127. Word Ladder
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
1. Return 0 if there is no such transformation sequence.
2. All words have the same length.
3. All words contain only lowercase alphabetic characters.
4. You may assume no duplicates in the word list.
5. You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
import string
def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    def can_trans(p,q):
        for idx, i in enumerate(p):
            if i != q[idx]: return p[:idx]==q[:idx] and p[idx+1:]==q[idx+1:]
        return False
    if not endWord in wordList: return 0
    #wordList.remove(endWord)
    # 第一遍出错，因为没有搞清楚一步是什么意思
    q = [beginWord]
    sz = len(beginWord)
    already = [beginWord]
    q2 = [endWord]
    already2 = [endWord]
    words1 = wordList[:]
    words2 = wordList[:]
    steps, t = 0, True
    while len(q)>0 and len(q2)>0:
        if set(q).intersection(set(q2)): return steps+1
        exts = []
        if t:
            for b in q: # 扩展一层
                #exts = exts+[b[:i]+c+b[i+1:] for i in range(sz) for c in string.ascii_lowercase]
                exts += [w for w in words1 if can_trans(w,b)]
            #filtered = list(filter(lambda x:x in wordList and not x in already, exts))
            #already = already + filtered
            words1 = list(set(words1)-set(exts))
            print('-->', exts)
            q = exts[:] 
        else:
            for b in q2: # 扩展一层
                exts += [w for w in words2 if can_trans(w,b)]
            #filtered = list(filter(lambda x:x in wordList and not x in already, exts))
            #already = already + filtered
            words2 = list(set(words2)-set(exts))
            print('<--', exts)
            q2 = exts[:] 
        steps += 1
        t = not t
        
    return 0
b = "hit"
e = "cog"
w = ["hot","dot","dog","lot","log","cog"]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

b = "qa"
e = "sq"
w = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

##b="hot"
##e="dog"
##w=["hot","cog","dog","tot","hog","hop","pot","dot"]
##b="a"
##e="c"
##w=["a","b","c"]

l = ladderLength(b, e, w)
print(l)
