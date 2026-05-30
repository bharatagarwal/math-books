# uv run python code/bradfield/12-revision/02_consecutive_product.py
# CAPSTONE (counting <-> number theory): the product of any k consecutive
# integers is divisible by k!. The slick reason is a COUNTING fact -- the
# quotient is a binomial coefficient, which counts a set, so it's an integer.
from math import factorial, comb

#   m(m+1)...(m+k-1) / k!  =  C(m+k-1, k)   (a count => an integer)
for m in range(1, 60):
    for k in range(1, 12):
        prod = 1
        for i in range(k):
            prod *= (m + i)
        assert prod % factorial(k) == 0            # divisibility...
        assert prod // factorial(k) == comb(m + k - 1, k)  # = C(..)

print("product of k consecutive integers is divisible by k! for all tested m,k")
print("and the quotient is the binomial coefficient C(m+k-1, k)")
