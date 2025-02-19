import math
from calculator import Calculator  # Import the Calculator class

class ScientificCalculator(Calculator):
    def sin(self, angle):
        """
        Calculate sine of an angle in radians.
        
        Args:
            angle: Angle in radians.
        
        Returns:
            Sine of the angle.
        """
        return math.sin(angle)

    def cos(self, angle):
        """
        Calculate cosine of an angle in radians.
        
        Args:
            angle: Angle in radians.
        
        Returns:
            Cosine of the angle.
        """
        return math.cos(angle)

    def tan(self, angle):
        """
        Calculate tangent of an angle in radians.
        
        Args:
            angle: Angle in radians.
        
        Returns:
            Tangent of the angle.
        """
        return math.tan(angle)

