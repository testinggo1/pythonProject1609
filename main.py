# Первое задание.
# s - сколько яблок достанется каждому школьнику;
# p - сколько яблок останется в корзине;

k = int(input())
n = int(input())
s = k // n
p = k - (s * n)
print(s)
print(p)

# Второе задание.

a = int(input())
b = int(input())
c = int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)

# Третье задание.

num = 2321
result = 0
while num > 0:
    result = result * 10 + num % 10
    num = num // 10

print(result)

# Задание про перевод секунд в часы:минуты:секунды.

second = int(input())
hours = second // 3600
second = second % 3600
minutes = second // 60
second = second % 60
print(hours, ':', minutes, ':', second)
