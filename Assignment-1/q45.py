# 45. Find the sum of 28 terms of an Arithmetic Progression -21 -18 -15 -12 . . . . .

a = -21
d = 3
n = 28

last_term = a + (n - 1) * d

sum_ap = n * (a + last_term) / 2

print(sum_ap)