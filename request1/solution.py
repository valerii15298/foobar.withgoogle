def solution(index):
    # Your code here
    n = 20231
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    string = ''
    # Concat all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            string += str(p)
    return string[index:index + 5]
