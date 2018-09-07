

def reverse_list(lst):
    if len(lst)==0: return []
    return [lst[-1]] + reverse_list(lst[:-1])

lst=list(range(10))
print(lst)
print(reverse_list(lst))
print(lst)
