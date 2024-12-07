import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import sys
import os
import re

def main():
    # User decides what they would like to do
    user_input = input("Arithmetic - A, Trigonmetrics - T?, Matrices - M, Graphs - G? ").strip().lower()

    # Switch to dictate what they will do 
    match(user_input):
        case "a":
            input_a = input("Type in the sum format \"x +/- y +- z...\"")
            print(arithmetic(input_a))

        case "t":
            print(trigonometric())

        case "m":
            mat_type = input("Would you like to multiply, add or subtract? ").strip().lower()
            match(mat_type):
                case "add":
                    print(matrix_addition(mat_type))

                case "subtract":
                    print(matrix_addition(mat_type))

                case "multiply":
                    print(matrix_multiplication(mat_type))
        case "g":
            plot_graph()

def arithmetic(sum):
    sumlst = sum.split(" ")
    print(sumlst)

    i=0
    # Handle multiplication first
    while i < len(sumlst) - 1:
        if sumlst[i] == "*":
            multiplication = float(sumlst[i-1]) * float(sumlst[i+1])
            sumlst[i] = multiplication
            
            # Remove the numbers to the right and left of the new number 
            sumlst.pop(i-1)
            sumlst.pop(i)
            print(sumlst)

        i += 1


    i = 0
    number = 0
    while i <= len(sumlst) - 1:

        # Add initial number to the sum
        if i == 0:
            number += float(sumlst[0])

        # Check if we are adding
        elif sumlst[i] == "+":
            number += float((sumlst[i+1]))

        # Check if we are subtracting
        elif sumlst[i] == "-":
            number -= float(sumlst[i+1])
        i += 1

    return number

def trigonometric():
    # Take angle and turn into radians
    angle = int(input("What angle? "))
    angle = np.radians(angle)

    # Process into a trig function and return for printing
    input_t = input("Sin, Cos or tan? ").lower()
    match(input_t):
        case "sin":
            return (round(np.sin(angle), 2))
        case "tan":
            return (round(np.tan(angle), 2))
        case "cos":
            return (round(np.cos(angle), 2))

def matrix_addition(operand):
    # Both matrices must be same size by laws of matrix addition/subtraction
    rows = int(input("How many rows is your matrices? "))
    columns = int(input("How many columns in your matrices? "))
    matrix1 = np.zeros((rows, columns))
    matrix2 = matrix1

    # Get elements for the matrices
    for i in range(rows):
        for j in range(columns):
            matrix1[i][j] = float(input(f"For matrix one please enter element {i+1}, {j+1}: ").strip())
    for i in range(rows):
        for j in range(columns):
            matrix2[i][j] = float(input(f"For matrix two please enter element {i+1}, {j+1}: ").strip())

    # Add or subtract and return the new matrix for printing
    if operand == "add":
        return matrix1 + matrix2
    elif operand == "subtract":
        return matrix1 - matrix2

def matrix_multiplication():
    # Obtain shape of the matrices
    rows1 = int(input("How many rows is matrix 1? "))
    columns1 = int(input("How many columns is matrix 1? "))
    rows2 = int(input("How many rows is matrix 2? "))
    columns2 = int(input("How many columns is matrix 2? "))
    matrix1 = np.zeros((rows1, columns1))
    matrix2 = np.zeros((rows2,columns2))

    # Follow rules of matrix multiplication
    if rows1 != columns2:
        sys.exit("Matrix 1 rows must equal matrix 2's columns")

    # Obtain elements for both of the matrices
    for i in range(rows1):
        for j in range(columns1):
            matrix1[i][j] = float(input(f"For matrix one please enter element {i+1}, {j+1}: ").strip())

    for i in range(rows2):
        for j in range(columns2):
            matrix2[i][j] = float(input(f"For matrix two please enter element {i+1}, {j+1}: ").strip())

    return np.dot(matrix1, matrix2)

def plot_graph():
    # Step 1: Get user input for the mathematical function
    x = sym.symbols("x")
    user_input = input("Enter a function f(x) (e.g., x**2, sin(x), 5*x + 3): ")

    # Make sure user input fits the SymPy syntax
    user_input = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', user_input)

    try:
        # Turn input into a SymPy
        y = sym.sympify(user_input)

        # Change syntax into numpy so we can use it for processing the graph
        f = sym.lambdify(x, y, 'numpy')

        # Obtain x values for the function
        x_vals = np.arange(-10, 10, 0.05)

        # Obtain y values of the function
        y_vals = f(x_vals)

        # Plot the graph onto an xy plane with a grid
        plt.plot(x_vals, y_vals, label=f"f(x) = {user_input}")
        plt.title("User Inputted Graph")
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()

        # If plot.png exists, remove it
        if os.path.exists("plot.png"):
            os.remove("plot.png")

        # Save the new plot.png
        plt.savefig("plot.png")
        print("Plot saved as plot.png")

    # Catch Errors
    except Exception as e:
        print(f"Error: {e}")
        print("Please enter a valid mathematical function.")

main()
