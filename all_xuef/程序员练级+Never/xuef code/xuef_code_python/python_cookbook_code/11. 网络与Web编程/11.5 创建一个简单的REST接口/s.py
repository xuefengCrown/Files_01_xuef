

up=float(input("上底："))
down=float(input("下底："))
h=float(input("高："))
s=float(input("面积："))

p=print
if up==0:
    p("上底为：", s*2/h-down)
elif down==0:
    p("下底为：", s*2/h-up)
else:
    p("高为：", s*2/(up+down))


