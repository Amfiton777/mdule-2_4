numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i <= 1:
        continue
    elif i > 1:
        is_prime = True
        for j in range(2, 16):
            if i % j == 0 and i != j:
                not_primes.append(i)
                break
            else:
                primes.append(i)
                break
print(primes)
print(not_primes)
