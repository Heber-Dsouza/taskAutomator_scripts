class NumericMatch:
    @staticmethod
    def is_in_range(range_min:float|int, range_max:float|int, value:float|int)->bool:
        """
        Checks whether a value is within a numeric range.

        Args:
            range_min (float | int): Minimum range value.
            range_max (float | int): Maximum range value.
            value (float | int): Value to check.

        Returns:
            bool: True if the value is within the range, otherwise False.
        """
        return (value-range_min)*(value-range_max)<=0