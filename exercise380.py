n = input()
total = int(n[0])

for i in range(1, len(n), 2):
    if n[i] == '-':
        total -= int(n[i + 1])
    else:
        total += int(n[i + 1])

print(total)