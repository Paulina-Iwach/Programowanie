import math
import random
import numpy


class Vector:
    """
    Class to defining vectors and for doing basic vector operations.
    """

    def __init__(self, n=3):
        """
        Create n size vector and fill in with none value.
        :param n: Vector dimension.
        """
        if n <= 0:
            raise ValueError("Vector must have at least one coordinate")
        else:
            self.n = n
            self.vector = [None] * n

    def random_values(self):
        """
        Function fills the vector with random numbers.
        """
        for i in range(0, self.n):
            self.vector[i] = (random.randint(-100, 100))

    def from_list(self, array):
        """
        Function creates a vector from the numbers given in the list.
        List must be the same length as the vector dimension.
        :param array: List of numbers.
        """
        if len(array) != self.n:
            raise ValueError("The number of coordinates must be the same as the dimension of the vector.")
        else:
            for i in range(0, self.n):
                self.vector[i] = array[i]

    def __str__(self):
        """
        Function convert vector representation to human-readable string.
        :return: Text(human-readable string) representation of the vector.
        """
        return str(self.vector)

    def __add__(self, other):
        """
        The operator sum overloaded.
        The operator adds two vectors, self and other.
        Vectors must have the same dimension.
        :param other: Vector to add.
        :return: Sum of two vectors.
        """
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must have same dimensions.")
        else:
            vec_sum = []
            for i in range(0, self.n):
                vec_sum.append(self.vector[i] + other.vector[i])

            added = Vector(self.n)
            added.from_list(vec_sum)
            return added

    def __sub__(self, other):
        """
        The operator subtraction overloaded.
        Operator subtracts two vectors, other from self.
        Vectors must have the same dimension.
        :param other: Vector to subtract.
        :return: Difference between two vectors.
        """
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must have same dimensions.")
        else:
            vec_diff = []
            for i in range(0, self.n):
                vec_diff.append(self.vector[i] - other.vector[i])

            difference = Vector(self.n)
            difference.from_list(vec_diff)
            return difference

    def __rmul__(self, other):
        """
        The operator multiplication overloaded.
        Operator multiplies two vectors, other and self.
        :param other: Vector that is multiplied with self.
        :return: Result of the vectors multiplication.
        """
        vec_mul = []
        for i in range(0, self.n):
            vec_mul.append(self.vector[i] * other)

        mult = Vector(self.n)
        mult.from_list(vec_mul)
        return mult

    def __mul__(self, other):
        """
        The operator multiplication overloaded.
        Operator multiplies two vectors, other and self.
        :param other: Vector that is multiplied with self.
        :return: Result of the vectors multiplication.
        """
        vec_mul = []
        for i in range(0, self.n):
            vec_mul.append(other * self.vector[i])

        mult = Vector(self.n)
        mult.from_list(vec_mul)
        return mult

    def vec_len(self):
        """
        Function counts length of the vector.
        Vector cannot be an empty object.
        :return: Length of the vector.
        """
        if None in self.vector:
            raise ValueError("Empty object")
        else:
            square = []
            for i in range(0, self.n):
                square.append(self.vector[i] ** 2)
            v_len = math.sqrt(sum(square))
            return v_len

    def elem_sum(self):
        """
        Function adds all elements of a vector.
        :return: Sum of vector elements. For an empty vector, function returns 0.
        """
        el_sum = 0
        if None in self.vector:
            return el_sum
        else:
            return sum(self.vector)

    def scalar_prod(self, other):
        """
        Function computes scalar product of two vectors.
        Vectors must have same dimensions.
        :param other: Vector to compute the scalar product with self.
        :return: Scalar product of vectors. For an empty vector, function returns 0.
        """
        if None in self.vector or None in other.vector:
            return 0
        elif self.n != other.n:
            raise ValueError("Vectors must have same dimensions.")
        else:
            s_prod = numpy.dot(self.vector, other.vector)
            return s_prod

    def __getitem__(self, item):
        """
        Operator that gives access to particular vector elements.
        :param item: Number of place in vector we want to access.
        :return: Element value at the particular number of place in vector.
        """
        if type(item) is int:
            return self.vector[item]

        else:
            raise ValueError("Data type must be int.")

    def __contains__(self, item):
        """
        Operator that checks if particular element belongs to vector.
        :param item: Element we want to check if it belongs to vector.
        :return: True if element belongs to vector and False if not.
        """
        if type(item) is int or type(item) is float:
            if item in self.vector:
                return True
            else:
                return False
        else:
            raise ValueError("Data type must be numeric.")
