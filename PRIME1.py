# -----------------
#  Solution in Python does not compute in the given time use another programming language such as 
# C++ or Java and the solution will be
# accepted using this same algorithm
# -----------------


def build_prime():
    n = 32000
    prime = [True for i in range(n + 1)]
    prime[0] = False
    prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    output = []
    for i in range(len(prime)):
        if prime[i]:
            output.append(i)
    return output


if __name__ == '__main__':
    t = int(input().strip())
    prime = build_prime()
    print(len(prime))
    while t > 0:
        m, n = list(map(int, input().strip().split(' ')))
        prime_between = [True for i in range(m, n + 1)]
        if m < 2:
            prime_between[0] = False
        for i in range(len(prime_between)):
            if prime_between[i]:
                for j in prime:
                    if (i + m) % j == 0:
                        if (i + m) != j:
                            prime_between[i] = False
                        for k in range((i + m) + j, n + 1, j):
                            prime_between[k - m] = False
                        break
        for i in range(len(prime_between)):
            if prime_between[i]:
                print(i + m)
        if t > 0:
            print("\n")
        t -= 1
