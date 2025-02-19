class Calculator:
    def add(self, num1, num2):
        """Addition operation."""
        return num1 + num2

    def subtract(self, num1, num2):
        """Subtraction operation."""
        return num1 - num2

    def multiply(self, num1, num2):
        """Multiplication operation."""
        return num1 * num2

    def divide(self, num1, num2):
        """
        Division operation.
        
        Args:
            num1: Dividend.
            num2: Divisor.
        
        Returns:
            Result of division.
        
        Raises:
            ZeroDivisionError: If num2 is 0.
        """
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num1 / num2
