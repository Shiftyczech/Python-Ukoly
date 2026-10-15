a = 15
b = 42
c = 7

# 1. Porovnání a, b
if a > b:
    temp = a
    a = b
    b = temp

# 2. Porovnání b, c
if b > c:
    temp = b
    b = c
    c = temp

# 3. Porovnání a, b
if a > b:
    temp = a
    a = b
    b = temp

print(f"Čísla v pořadí podle písmen a = {a}, b = {b}, c = {c}")