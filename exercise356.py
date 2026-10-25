n = int(input())
expression = ''
total = 0

for i in range(1, n):
    expression += str(i) + '*' + str(i + 1) + '+'
    total += i * (i + 1) 
    
print(expression[:-1] + '=' + str(total))
