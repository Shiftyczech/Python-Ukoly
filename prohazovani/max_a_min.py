a = 15
b = 42
c = 7

min_val = a
max_val = a


if b < min_val:
    min_val = b
if b > max_val:
    max_val = b

if c < min_val:
    min_val = c
if c > max_val:
    max_val = c

print(f"Nejmenší hodnota je {min_val}, největší hodnota je {max_val}")