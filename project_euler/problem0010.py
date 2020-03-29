"""
Find the sum of all the primes below two million.
"""


from helper import prime_sieve


def sum_of_primes(limit):
    """
    This function will use the Sieve of Eratosthenes
    from the helper module and will generate a list
    of primes uptill the limit that the user
    provides.

    Then it will return the sum of all those primes.
    """
    return sum(prime_sieve(limit))


def main():
    print(sum_of_primes(2000000))


if __name__ == '__main__':
    main()
