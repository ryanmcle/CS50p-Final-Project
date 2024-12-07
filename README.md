# Graph Builder and Calculator
#### Video Demo:  <https://youtu.be/p3nvx03wYuk>
#### Description:
This was my introductory project to gain insight into MatPlotLib, Regular Expressions, Numpy and SymPy. It is a calculator which can do matrix algebra as well as plot and save graphs into the folder, it only keeps one graph in the folder at a time so it will delete past graphs once a new one has been produced.

The first function in the Project is the Main function, this handles the majority of the user input and includes a switch in order to process what the user would like to do with the program. It has 4 options initally, Arithmetics with an input of A, Trigonmetric with an input of T, Matrices with an input of M or Graphs with an input of G. The function then will ask other question if using matrices such as addition or multiplication.

The program then proceeds to have the arithmetic() function it takes the parameter sum which is a user inputted String and splits it between the white space. It then goes through processes on newly made list in order to compute the sum. The first while loop is used for multiplication as by the rules of BODMAS this must be done first, It locates the multiplication symbols in the sum and then multiplies the 2 numbers next to it together, it then updates the current iteration in the list (*) to the product of the 2 numbers next to it and removes the 2 numbers next to it. I then used a second while loop which goes through the list just adding and subtracting the numbers, pretty simple code here.

My third function is a trigonmetric function, this one is also fairly symbol thanks to NumPy being very useful and providing the trig function pre-made. It receives the parameter angle and then converts it to radians, put the angle through whichever trig function you would like to use and returns that value.

I then have a matrix addition function, in this function it asks for the size of the matrix once, as by the laws of matrix addition they must be the same. It then takes an input for every entry in each position of the NumPy array and sums the 2 arrays together.

The matrix multiplication function takes in 2 matrix again, making sure the 2nd matrix has the same number of rows as the first matrix has columns to ensure they can be mulitplied together, it then mulitplies them using np.dot()

The final function is plot_graph() this function asks for a user input of an f(x) function and filters through it with a regular expression to ensure it fits SymPys syntax, using re.sub to update it if required. Then the function lambdifies the SymPy function for plotting and saves it to the folder, deleting the old graph and taking its place.
