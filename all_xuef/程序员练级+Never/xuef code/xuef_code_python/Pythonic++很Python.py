######
p=print # 方便输出
######

evens = (i for i in range(1, 10) if i%2==0)
p(list(evens))

seq = ['one', 'two', 'three']
seq_with_idx = {idx:c for idx,c in enumerate(seq)}
p(seq_with_idx)
