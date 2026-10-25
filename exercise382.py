a, b, c, d = int(input()), int(input()), int(input()), int(input())
text = '\t'

for k in range(c, d + 1):
    text += str(k) + '\t'
print(text)

for i in range(a, b + 1):
    text = str(i) + '\t'
    for j in range(c, d + 1):
        text += str(i * j) + '\t'
    print(text)