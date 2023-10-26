def print_super_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, n + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    super_primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            digits = [int(digit) for digit in str(p)]
            is_super_prime = all(is_prime[d] for d in digits)
            if is_super_prime:
                super_primes.append(p)

    return super_primes

n = 241
print("Super-Primes less than or equal to", n)
super_primes = print_super_primes(n)
print(super_primes)
