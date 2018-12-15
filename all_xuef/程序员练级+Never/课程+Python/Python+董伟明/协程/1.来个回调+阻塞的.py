

# 来个回调，阻塞的

def framework(logic, callback):
    s = logic()
    print("[FX] logic: ", s)
    print("[FX] do something ") # 这一步可能很耗时
    callback("async: " + s)

def logic():
    s = "mylogic"
    return s

def callback(s):
    print(s)

framework(logic, callback)

    
