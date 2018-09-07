
def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    # lst中数字升序, 如[1,2,3]; 返回它的所有排列, 按升序;
    def f(lst):
        if len(lst) == 1: return [lst] # [[3]]
        perms = []
        for idx,i in enumerate(lst):
            perms += [[i]+p for p in f(lst[:idx]+lst[idx+1:])]
            
        return perms
    nthP = f(list(range(1,n+1)))[k-1]
    return ''.join(map(str, nthP))

n,k=9,24
print(getPermutation(n, k)) # 很慢
#n,k=4,9
fac_dict = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320}
def p(n,k,lst):
    if n==1: return lst
    i,j=k//fac_dict[n-1],k%fac_dict[n-1]
    if j>0:
        return lst[i:i+1]+p(n-1,j,lst[:i]+lst[i+1:])
    if j==0:
        return lst[i-1:i]+p(n-1,fac_dict[n-1],lst[:i-1]+lst[i:])

res_lst = p(n,k,list(range(1,n+1)))
print(''.join(map(str, res_lst)))

    
#print(getPermutation(n, k))
