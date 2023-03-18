# Fraction Calculator
Programme that calculate simple Equation with Fraction

## Equation:
- Addition (+)
- Subtraction (-)
- Multiplication (x)
- Division (÷)

## Input/Output Specification
### Input
Each line of input will provide the program with one operation (addition/subtraction/multiplication/
division) to perform. Each line will be written in the form:
- integer operator fraction
- fraction operator integer
- fraction operator fraction
where:
- integer is an integer,
- operator is one of the symbols: + - * :
- fraction is written as: integer/integer
- integer, operator, fraction are separated by one space
### Output
The only information the program prints is a fraction or an error message.
The fraction resulting from the operation must be written in an irreducible form. Fraction
format: integer/integer
In case:
- the user enters incorrect data,
- the user enters data in an incorrect format,
- the resulting fraction cannot be written
the program must print the string 'ERROR'.

## Implementation Details
Define a class Fraction representing a fraction, the class must have:
- the __init__ function accepting the numerator and denominator of the fraction,
- its own + operator (using a magic method),
- its own - operator (using a magic method),
- its own * operator (using a magic method),
- its own / operator (using a magic method),
- its own __str__ function returning a string representing the fraction.
All operations on fractions should be performed using objects of this class.
This class should store fractions in an irreducible form.

### EOFError 
Use the exception mechanism to handle EOFError signaling the end of the input data.
