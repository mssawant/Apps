import hashlib

def encode(counter):
    digitmap = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ-_"

    res = ""
    while counter > 0:
        res = digitmap[(counter % 64)] + "" + res
        counter = counter // 64
        print(res)
    return "http://ms.saw/" + res

print(encode(23000000000))
