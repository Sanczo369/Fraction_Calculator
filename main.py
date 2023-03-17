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


def main():
    while True:
        try:
            equation = input()
            equationTab = equation.split()
            if len(equationTab) == 3:
                number1 = equationTab[0].split("/")
                if len(number1) == 1:
                    number1.append('1')
                number2 = equationTab[2].split("/")
                if len(number2) == 1:
                    number2.append('1')
                if int(number1[1]) != 0 and int(number2[1]) != 0:
                    number1 = Fraction(int(number1[0]), int(number1[1]))
                    number2 = Fraction(int(number2[0]), int(number2[1]))
                    if equationTab[1] == "+":
                        print(number1 + number2)
                    elif equationTab[1] == "-":
                        print(number1 - number2)
                    elif equationTab[1] == "*":
                        print(number1 * number2)
                    elif equationTab[1] == ":":
                        print(number1 / number2)
                    else:
                        print('ERROR')
                else:
                    print('ERROR')
            else:
                print('ERROR')
        except EOFError:
            break


if __name__ == '__main__':
    main()
