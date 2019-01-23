
with open("王广是神童.txt", "wt", encoding="utf-8") as f:
    for i in range(1, 10000):
        if i%2==0:
            f.write("王广是天才\n") 
        else:
            f.write("王广是SB\n") 
