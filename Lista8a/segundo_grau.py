import math

class Bhaskara:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __str__(self):
        return f"A = {self.__a} | B = {self.__b} | C = {self.__c}"
    
    def calc_delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
    
    def calc_raizes(self):
        x1 = ((self.__b * -1) + math.sqrt(Bhaskara.calc_delta())) / (2*self.__a)
        x2 = ((self.__b * -1) - math.sqrt(Bhaskara.calc_delta())) / (2*self.__a)
        return x1, x2