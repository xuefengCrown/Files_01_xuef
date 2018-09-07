"""
394. Decode String (Stack)
Examples:
    s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a2[c]]", return "accaccacc".
    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    def decompose(s):
        left = s.find('[')
        k, r = 1, left + 1
        for letter in s[left+1:]:
            if letter == '[':
                k += 1
            elif letter ==']':
                k -= 1
            if k == 0: break
            r += 1
        return (s[:left], s[left+1:r], s[:r+1])

    if not s: return ""
    if not ('[' in s or ']' in s): return s
    if not s[0].isdigit():
        for idx,i in enumerate(s):
            if i.isdigit():
                return s[:idx] + decodeString(s[idx:])
    
    res = decompose(s)
    #print(res)
    return int(res[0])*decodeString(res[1]) + decodeString(s.replace(res[2], ""))
    
s = "3[a]2[bc]"
s = "3[a2[c]]"
s = "zz2[abc]3[cd]ef"
print(decodeString(s))
