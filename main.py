class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # display Fraction
    def __str__(self):
        self.simplyfy()
        return "{}/{}".format(self.numerator, self.denominator)

    # simplyfy Fraction
    def simplyfy(self):
        min_val = min(self.numerator, self.denominator)
        for divisor in range(2, min_val + 1):
            if (self.numerator % divisor == 0) and (self.denominator % divisor == 0):
                self.numerator = int(self.numerator / divisor)
                self.denominator = int(self.denominator / divisor)
                return self.simplyfy()
        return self.numerator, self.denominator

    # Addition (magic methods __add__())
    def __add__(self, number2):
        if self.denominator != number2.denominator:
            result_n = self.numerator * number2.denominator + number2.numerator * self.denominator
            result_d = self.denominator * number2.denominator
            return Fraction(result_n, result_d)
        else:
            result_n = self.numerator + number2.numerator
            result_d = self.denominator
            return Fraction(int(result_n), int(result_d))

    # Subtraction (magic methods __sub__())
    def __sub__(self, number2):
        if self.denominator != number2.denominator:
            result_n = self.numerator * number2.denominator - number2.numerator * self.denominator
            result_d = self.denominator * number2.denominator
            return Fraction(result_n, result_d)
        else:
            result_n = self.numerator - number2.licznik
            result_d = self.denominator
            return Fraction(int(result_n), int(result_d))

    # Multiplication (magic methods __mul__())
    def __mul__(self, number2):
        result_n = self.numerator * number2.numerator
        result_d = self.denominator * number2.denominator
        return Fraction(int(result_n), int(result_d))

    # Division (magic methods __truediv__())
    def __truediv__(self, number2):
        result_n = self.numerator * number2.denominator
        result_d = self.denominator * number2.numerator
        return Fraction(int(result_n), int(result_d))
