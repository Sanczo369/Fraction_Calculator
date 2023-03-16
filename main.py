class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # display Fraction
    def __str__(self):
        self.simplyfy()
        return ("{}/{}".format(self.numerator,self.denominator))

    # simplyfy Fraction
    def simplyfy(self):
        min_val = min(self.numerator, self.denominator)
        for divisor in range(2, min_val + 1):
            if (self.numerator % divisor == 0) and (self.denominator % divisor == 0):
                self.numerator = int(self.numerator / divisor)
                self.denominator = int(self.denominator / divisor)
                return self.simplyfy()
        return (self.numerator, self.denominator)
