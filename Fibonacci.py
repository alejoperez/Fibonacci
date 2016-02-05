__author__ = "Alejandro Perez"

class Fibonacci:
    def fibonacci(sefl,n):
        numberOne, numberTwo = 0, 1
        for i in range(0, n):
            numberOne, numberTwo = numberTwo, numberOne + numberTwo
        return numberOne

    def startFibonacci(self):
        n = int(input("Digita el número de iteraciones: "))
        for i in range(0,n):
            print( "F(" + str(i) + ") = " + str(self.fibonacci(i)))


print(Fibonacci().startFibonacci())