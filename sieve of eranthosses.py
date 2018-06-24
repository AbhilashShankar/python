max_prime_number = 120
prime = range(max_prime_number+1)

def multiple(i,n):
    """
    Mark the multiples
    :param i: multiples of
    :param n: max number of prime
    :return: None
    """
    # retain the start number
    start = i + i
    for i in range(start,n,i):
        # take out multiples
        prime[i] = -1
        # print i


def print_primes(n):
    """
    Print prime numbers
    :param n: The max number to check for prime
    :return: None
    """
    for i in range(2,n+1):
        if prime[i] != -1:
            print i,


def seive(n):
    """
    Seive of E
    :param n: The max number to check for prime
    :return: None
    """
    for i in range(2,n+1):
        multiple(i,n+1)
        # return

if __name__ == "__main__":
    seive(max_prime_number)
    print_primes(max_prime_number)

