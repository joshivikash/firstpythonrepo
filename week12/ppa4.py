def std_dev(X):
    """
    Compute the standard deviation
    
    Argument:
        X: list of integers
    Return:
        sigma: float
    """
    mean = sum(X)/len(X)
    sigma = (sum([(x-mean)**2 for x in X])/len(X))**0.5
    return sigma
X = [float(x) for x in input().split(',')]
sigma = std_dev(X)
print(f'{sigma:.2f}')