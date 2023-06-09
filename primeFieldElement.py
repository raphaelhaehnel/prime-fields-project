class PrimeFieldElement:
    """
    This class represents an element 'a' in the field k = F_p, where F_p is the prime field
    """

    def __init__(self, a: int, p: int):
        """
        Generate an element from the prime field k

        Parameters
        ----------
        a : an element in k
        p : a prime number defining the prime field 
        """

        if a >= p or a < 0:
            error = f"Invalid {a} for PrimeField of {p}"
            raise ValueError(error)
        self.a = a
        self.p = p

    def __add__(self, other):
        """
        Add two elements according to the field logic
        """

        # If the other element is a number, we add it to the element
        if isinstance(other, int):
            a = (self.a + other) % self.p
            return self.__class__(a, self.p)

        # If the two elements are belonging to different prime field, throws an error
        if self.p != other.p:
            error = f"Cannot add two numbers in different PrimeFields {self.p} and {other.p}"
            raise TypeError(error)

        # Add the two elements
        a = (self.a + other.a) % self.p

        return self.__class__(a, self.p)

    def __sub__(self, other):
        """
        Substract two elements according to the field logic
        """

        # If the other element is a number, we substract it to the element
        if isinstance(other, int):
            a = (self.a - other) % self.p
            return self.__class__(a, self.p)

        # If the two elements are belonging to different prime field, throws an error
        if self.p != other.p:
            error = f"Cannot subtract two numbers in different PrimeFields {self.p} and {other.p}"
            raise TypeError(error)

        # Substract the two elements
        a = (self.a - other.a) % self.p
        return self.__class__(a, self.p)

    def __mul__(self, other):
        """
        Multiply two elements according to the field logic
        """

        # If the other element is a number, we multiply it to the element
        if isinstance(other, int):
            a = (self.a * other) % self.p
            return self.__class__(a, self.p)

        # If the two elements are belonging to different prime field, throws an error
        if self.p != other.p:
            error = f"Cannot multiply two numbers in different PrimeFields {self.p} and {other.p}"
            raise TypeError(error)

        # Multiply the two elements
        a = (self.a * other.a) % self.p
        return self.__class__(a, self.p)

    def __truediv__(self, other):
        """
        Divide two elements according to the field logic
        """

        # If the other element is a number, we convert it to an PrimeFieldElement object
        if isinstance(other, int):
            if other >= self.p or other < 0:
                error = f"Invalid division for PrimeField of {self.p}: division by {other}"
                raise ValueError(error)
            return self / self.__class__(other, self.p)

        # If the two elements are belonging to different prime field, throws an error
        if self.p != other.p:
            error = f"Cannot divide two numbers in different PrimeFields {self.p} and {other.p}"
            raise TypeError(error)

        if other.a == 0:
            error = f"Cannot divide by zero in PrimeField {self.p}"
            raise ZeroDivisionError(error)

        return self * other.inverse()

    def __pow__(self, other):
        """
        Apply exponent to the elements according to the field logic
        """

        if isinstance(other, PrimeFieldElement):
            exp = other.a
        else:
            exp = other

        if exp == 0:
            return self.__class__(1, self.p)
        if exp < 0:
            # Find the inverse of the element
            inv = self.inverse()
            exp *= -1
            return inv ** exp

        result = (self.a ** exp) % self.p
        return self.__class__(result, self.p)

    def __gcdExtended(self, a, b):
        """
        Function for extended Euclidean Algorithm
        """

        # Base Case
        if a == 0:
            return b, 0, 1

        gcd, x1, y1 = self.__gcdExtended(b % a, a)

        # Update x and y using results of recursive call
        x = y1 - (b//a) * x1
        y = x1

        return gcd, x, y

    def inverse(self):
        """
        Compute the inverse of the object according to the field logic
        """
        gcd, x, y = self.__gcdExtended(self.a, self.p)

        if gcd == self.p:
            error = f"{self.a} does not have an inverse in k"
            raise ValueError(error)

        if gcd == 1:
            return self.__class__(x % self.p, self.p)

        error = f"The Euclidean algorithm didn't work with this element"
        raise ValueError(error)

    def __repr__(self):
        """
        The object is represented by his element as an integer
        """

        return str(self.a)


if __name__ == "__main__":
    a = PrimeFieldElement(a=5, p=7)
    b = PrimeFieldElement(a=2, p=7)
    print("Hello World!")
