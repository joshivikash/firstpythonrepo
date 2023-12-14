def is_prime(n):
    '''
    Checks whether a given number is prime or not

    Argument: positive integer

    Returns : True or False depending upon whether the number is prime or not
    '''
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def primes_galore(L):
    '''
    This function returns the count of prime numbers present in a list, located at the prime indexes

    Argument: list L of non-negative integers

    Returns : The number of primes that are located at prime indices in L
    '''
    count = 0
    for i in range(len(L)):
        if i != 0 and i != 1 and is_prime(i) and is_prime(L[i]):
            count += 1
    return count