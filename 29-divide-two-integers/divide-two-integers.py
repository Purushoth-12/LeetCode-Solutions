class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define 32-bit signed integer boundaries
        MAX_INT = 2147483647   # 2^31 - 1
        MIN_INT = -2147483648  # -2^31

        # Handle edge case for overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive numbers using absolute values
        # (Using long conversion or checks to prevent python overflow issues with MIN_INT)
        abs_dividend = -dividend if dividend < 0 else dividend
        abs_divisor = -divisor if divisor < 0 else divisor

        quotient = 0

        # Subtract shifted divisors from the dividend
        while abs_dividend >= abs_divisor:
            temp_divisor, multiple = abs_divisor, 1
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            abs_dividend -= temp_divisor
            quotient += multiple

        return -quotient if negative else quotient