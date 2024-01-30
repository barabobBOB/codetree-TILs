N = input()

def f(n):
    return (n*n)

cut = 0
for i in N:
    cut += f(int(i))

print(cut)