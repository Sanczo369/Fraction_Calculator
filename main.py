class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # display Fraction
    def __str__(self):
        return ("{}/{}".format(self.numerator,self.denominator))


