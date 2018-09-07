"""
49. Group Anagrams (变位词归组)

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
1.All inputs will be in lowercase.
2.The order of your output does not matter.
"""
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    def sign(s): # 返回字符串s的签名
        unique_letters = sorted(list(set(s)))
        return ''.join([c+str(s.count(c)) for c in unique_letters])
    tab = {}
    for s in strs:
        signVal = sign(s)
        group = tab.get(signVal)
        if not group: tab[signVal] = [s]
        else: group.append(s)
    print(tab)
    return list(tab.values())
ss = ["eat", "tea", "tan", "ate", "nat", "bat"]
##sign(ss[0])
rs=groupAnagrams(ss)
print(rs)

