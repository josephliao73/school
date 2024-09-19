print("hi")

def euclid(a, b):
    A = max(a, b)
    B = min(a, b)
    ret = []
    while B:
        x, y = A // B, A % B 
        if not y:
            return ret
        ret.append((A, x, B, y))
        A, B = B, y

x = euclid(54321, 12345)
print(x)

while x:
    last = x.pop()


