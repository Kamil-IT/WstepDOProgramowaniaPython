import math


class LogExp:

    def __init__(self, a):
        self.a = a

    def logAX(self, x):
        return math.log(x, self.a)

    def log10X(self, x):
        return math.log10(x)

    def ax(self, x):
        return self.a*x

    def logaAX(self, x):
        return math.log(x, self.ax(x))


logExp = LogExp(2)

print(logExp.log10X(10))
print(logExp.logAX(8))
print(logExp.ax(10))
print(logExp.logaAX(10))




