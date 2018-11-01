import Math


def rSigma(num):
    if num >= 1:
        intNum = Math.trunc(num)
        return intNum + rSigma(num-1)


print rSigma(5)
