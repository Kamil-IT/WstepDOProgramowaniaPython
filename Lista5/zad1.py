import math


class LogExp:
    a = 0.0

    def __init__(self, a):
        self.a = a

    def log10X(self, x):
        return math.log10(x)

    def logAX(self, x):
        return math.log(x, self.a)


logExp = LogExp(2)

print(logExp.log10X(10))
print(logExp.logAX(8))
