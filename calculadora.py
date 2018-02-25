#!/usr/bin/python3

import sys

"""
____________________________ SumadorApp.py ____________________________

   Make a Python script that works as a web app and sums two numbers.
   operations (sum, substraction, multiplication and division).

   Don't forget to catch all possible exceptions
________________________________________________________________________

Author: Ainhoa Garcia-Ruiz Fuentes.       Date: 24/01/2018
Course: Servicios y Aplicaciones en Redes de Ordenadores.

"""

sumList = ["suma", "mas", "sum", "add", "+"]
subList = ["resta", "menos", "minus", "sub", "-"]
mulList = ["mul", "multiplica", "multiply", "*"]
divList = ["div", "divide", "/"]

# Get the parameters.
class Calculadora:

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def suma(self):
        return (self.s1 + self.s2);

    def substract(self):
        return (self.s1 - self.s2);

    def multiply(self):
        return (self.s1 * self.s2);

    def divide(self):
        try:
            return (self.s1 / self.s2);
        except ZeroDivisionError:
            print("[ERROR:] Zero division attempt!")

if __name__ == "__main__":

    if (len(sys.argv) == 4):
        op = sys.argv[1]
        try:
            c = Calculadora(float(sys.argv[2]), float(sys.argv[3]))

        except ValueError:
            print("[ERROR: ] Operands must be numbers.")
            exit()

    else:
        print("[USAGE: ] python calculadora.py <operation> <operand1> <operand2>")
        exit()

    # Compute the operation.
    if op in sumList:
        result = c.suma()
        opSym = "+"
    elif op in subList:
        result = c.substract()
        opSym = "-"
    elif op in mulList:
        result = c.multiply()
        opSym = "*"
    elif op in divList:
        result = c.divide()
        opSym = "/"
    else:
        print("[ERROR: ] Operation not included.")
        exit()

    # Display result.
    print('[RESULT: ] ' + str(c.s1) + ' ' + opSym + ' ' + str(c.s2) +
          ' = ' + str(result))
    exit()
