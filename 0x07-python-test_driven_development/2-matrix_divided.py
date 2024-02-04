Test driven
Test driven


0x07-python-test_driven_development/0-add_integer.py


#!/usr/bin/python3


"""Defines an integer addition function."""



def add_integer(a, b=98):

    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:

        TypeError: If either of a or b is a non-integer and non-float.

    """

    if ((not isinstance(a, int) and not isinstance(a, float))):

        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):

        raise TypeError("b must be an integer")

    return (int(a) + int(b))


0x07-python-test_driven_development/2-matrix_divided.py


#!/usr/bin/python3


"""Defines a matrix division function."""



def matrix_divided(matrix, div):

    """Divide all elements of a matrix.

    Args:

        matrix (list): A list of lists of ints or floats.

        div (int/float): The divisor.

    Raises:

        TypeError: If the matrix contains non-numbers.

        TypeError: If the matrix contains rows of different sizes.

        TypeError: If div is not an int or float.

        ZeroDivisionError: If div is 0.

    Returns:

        A new matrix representing the result of the division.

    """

    if (not isinstance(matrix, list) or matrix == [] or

            not all(isinstance(row, list) for row in matrix) or

            not all((isinstance(ele, int) or isinstance(ele, float))

                    for ele in [num for row in matrix for num in row])):

        raise TypeError("matrix must be a matrix (list of lists) of "

                        "integers/floats")


    if not all(len(row) == len(matrix[0]) for row in matrix):

        raise TypeError("Each row of the matrix must have the same size")


    if not isinstance(div, int) and not isinstance(div, float):

        raise TypeError("div must be a number")


    if div == 0:

        raise ZeroDivisionError("division by zero")


    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
