# =======================================================
# Using for loop
# =======================================================


def fib(n):
    a = 0
    b = 1

    for i in range(n-1):
        a = b
        b = a+b
    return a


print '** for loop ** ', fib(5)


# =======================================================
# Using recursion
# =======================================================


def fibR(num):
    if num == 1 or num == 2:
        return 1
    return fibR(num-1) + fibR(num-2)


print '** for recursion ** ', fibR(5)

# =======================================================
# Using generators
# =======================================================

a, b = 0, 1


def fibGen():
    global a, b
    while True:
        a, b = b, a+b
        yield a


f = fibGen()
f.next()
f.next()
f.next()
f.next()
f.next()
f.next()

print '** for generators ** ', f.next()


# =======================================================
# Using Memoization
# =======================================================

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]


@Memoize
def fibM(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


print '**  Memoization ** ', fibM(10)
