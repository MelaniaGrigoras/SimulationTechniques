from numpy import random, log, mean, std
from math import sqrt
import random as random2

def media(U):
    return (sum(U) / len(U))

def dispersia(U):
    U_square = []

    for u in U:
        U_square.append(u * u)

    return ( (sum(U_square) / len(U)) - media(U) ** 2)



print("#########  Central Limit Theorem  #########")

U = random.uniform(0, 1, 100)

# Mean
mu = media(U)

# Standard deviation
sd = dispersia(U)

for n in [5, 20, 50, 80]:
    X = random2.sample(list(U), n)
    # Mx = M si Sx = S / sqrt(n)
    print("n = ", n, "mean =", mu, "and std =", dispersia(X) / sqrt(n))
    print("n = ", n, "mean =", media(X), "and std =", dispersia(X), "\n")

print("n = ", len(U), "mean =", mu, "and std =", sd)


print("\n#########  Polar method  #########")
def polarMethod():
    while True:

        U1 = random.uniform(0, 1)
        U2 = random.uniform(0, 1)

        V1 = 2 * U1 - 1
        V2 = 2 * U2 - 1

        if ( V1 ** 2 +  V2 ** 2) < 1:
            S = V1 ** 2 +  V2 ** 2

            Z1 = V1 * sqrt(-2 * log(S) / S)
            Z2 = V2 * sqrt(-2 * log(S) / S)

            return [Z1, Z2]

# Z1, Z2 =  polarMethod()

# Verify the results by applying the method on a sample
sample = [x for _ in range(10000) for x in polarMethod()]

# Determine the mean and standard deviation of the sample
print("X ~ N(0, 1)")
# print("Mean =", mean(sample), "and std =", std(sample))
print("Mean =", media(sample), "and std =", dispersia(sample), "\n")

# Determine Y ~ N(2.5, 5), Y = 2.5 + 5 * X
print("Y ~ N(2.5, 5)")
# print("Mean =", 2.5 + mean(sample), "and std =", 5 * std(sample))
print("Mean =", 2.5 + media(sample), "and std =", 5 * dispersia(sample))


# Geometric variable

def Bernoulli(p):
    q = 1 - p
    U = random.uniform(0, 1)
    if U <= q:
        Z = 0
    else:
        Z = 1

    return Z

# Metoda pascal cu k = 1
print("\n#########  Pascal method  #########")

p = 0.7
q = 1 - p

def pascalMethod(k, p, j = 0, X = 0):
    while j != k:
        Y = Bernoulli(p)

        if Y == 0:
            X = X + 1
        else:
            j = j+1

    return X


sample1 = [pascalMethod(1, p) for _ in range(100000)]
print("Mean =", q / p, "and std =", q / p ** 2)
# print("Mean =", mean(sample1), "and std =", std(sample1))
print("Mean =", media(sample1), "and std =", dispersia(sample1))


print("\n#########  Inverse method  #########")

def inverseMethod(p):
    q = 1 - p
    U = random.uniform(0, 1)

    # print(U, log(U))
    # print(q, log(q))
    # print( log(U) / log(q), int(log(U) / log(q)))
    X = int(log(U) / log(q)) - 1

    return X

sample2 = [inverseMethod(p) for _ in range(100000)]
# print("Mean =", mean(sample2), "and std =", std(sample2))
print("Mean =", media(sample2), "and std =", dispersia(sample2))