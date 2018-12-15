

# 来个回调，异步的

def framework(logic):
    try:
        it = logic()
        s = next(it)
        print("[FX] logic: ", s)
        print("[FX] do something ") # 这一步可能很耗时
        it.send("async: " + s)
    except StopIteration:
        pass

def logic():
    s = "mylogic"
    r = yield s
    print(r)


framework(logic)

    













