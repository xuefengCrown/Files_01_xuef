
import os

cur_path = os.getcwd() # .py 所在的当前全路径

# print(cur_path)

for i in range(5, 100):
    fn = str(i) + '. .txt'
    f = open(fn, 'w') # 'w' mode: if not exist, create it
    f.close()
    
# os.mknod("5. txt")
