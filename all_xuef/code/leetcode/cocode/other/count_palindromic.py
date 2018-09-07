def mem(s):
    cache = [(idx, idx) for idx, _ in enumerate(s)]
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            cache.append((i, i+1))
    cnt = len(cache)
    i = 1
    while i < len(s):
        i += 1
        new_cache = []
        for l,r in cache:
            if l>0 and r<len(s)-1:
                if s[l-1] == s[r+1]:
                    new_cache.append((l-1, r+1))
        cnt += len(new_cache)
        cache = new_cache
    print(cnt)

mem("abc")
