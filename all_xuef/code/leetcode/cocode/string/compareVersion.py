

def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    def del_start0(s):
        if len(s)>1 and s[0] == '0':
            return del_start0(s[1:])
        return s
    def f(v1, v2):
        if not v1 and not v2: return 0
        if not v2: return 1
        if not v1: return -1
        # 都不为[]
        v1head = v1[0]
        v2head = v2[0]
        if int(v1head) > int(v2head): return 1
        if int(v1head) < int(v2head): return -1
        return f(v1[1:], v2[1:])
    v1 = version1.split('.')
    v1 = list(map(lambda x:del_start0(x), v1))
    print(v1)
    v2 = version2.split('.')
    v2 = list(map(lambda x:del_start0(x), v2))
    print(v2)
    for i in range(len(v1)-1, -1, -1):
        if v1[i] == '0': v1 = v1[:-1]
        else: break
    for i in range(len(v2)-1, -1, -1):
        if v2[i] == '0': v2 = v2[:-1]
        else: break
    print(v1)
    print(v2)
    return f(v1, v2)
version1 = "7.5.2.4"; version2 = "7.5.3"

#version1 = "1.0.1"; version2 = "1"
version1 = "01"; version2 = "1"
version1 = "0.1"; version2 = "1.1"

version1 = "1.2"; version2 = "1.10" # 不是按字符顺序比较，而是按数字
version1 = "1.0"; version2 = "1"
rs = compareVersion(version1, version2)
print(rs)


def del_start0(s):
    if s[0] == '0':
        return del_start0(s[1:])
    return s

