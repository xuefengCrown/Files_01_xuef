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
    if not endWord in wordList: return 0
    sz = len(beginWord)
    q4forward = []
    q4backward = []
    q4forward.append(beginWord)
    q4backward.append(endWord)
    words1 = wordList[:]
    words2 = wordList[:]
    already1, already2 = [beginWord], [endWord]
    
    s = True
    steps = 0
    # 第一遍出错，因为没有搞清楚一步是什么意思
    while q4forward and q4backward:
        if set(q4forward).intersection(set(q4backward)): return steps+1
        if s:
            b = q4forward.pop(0)
            exts = [b[:i]+c+b[i+1:]  for i in range(sz) for c in string.ascii_lowercase]
            filtered = list(filter(lambda x:x in words1 and not x in already1, exts))
            
            already1.append(b)
            for e in filtered:
                q4forward.append(e)
            for w in already1:
                if w in words1: words1.remove(w)
            s = False
            print('-->', q4forward)
        else:
            b = q4backward.pop(0)
            exts = [b[:i]+c+b[i+1:]  for i in range(sz) for c in string.ascii_lowercase]
            filtered = list(filter(lambda x:x in words2 and not x in already2, exts))
            already2.append(b)
            for e in filtered:
                q4backward.append(e)
            for w in already2:
                if w in words2: words2.remove(w)
            s = True
            print('<--', q4backward)
        steps += 1 # 什么叫一步？
    return 0
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

beginWord = "hit"
endWord = "cog"
#wordList = ["hot","dot","dog","lot","log"]

beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

l = ladderLength(beginWord, endWord, wordList)
print(l)
