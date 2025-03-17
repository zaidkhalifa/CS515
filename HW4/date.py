class Date:
    """A class for handling dates.
    
    >>> d = Date(2025, 2, 23)
    >>> str(d)
    '02/23/2025'
    >>> d2 = Date(99, 12, 31)
    >>> repr(d2)
    'Date(99, 12, 31)'
    
    >>> d3 = Date(2000, 2, 29)
    >>> d3.is_leap_year()
    True
    >>> d4 = Date(2100, 2, 28)
    >>> d4.is_leap_year()
    False
    
    >>> d5 = Date(2024, 2, 29)
    >>> d5.is_valid()
    True
    >>> d6 = Date(2023, 2, 29)
    >>> d6.is_valid()
    False
    
    >>> d7 = Date(2024, 2, 28)
    >>> d7.tomorrow()
    >>> repr(d7)
    'Date(2024, 2, 29)'
    >>> d8 = Date(2024, 12, 31)
    >>> d8.tomorrow()
    >>> repr(d8)
    'Date(2025, 1, 1)'
    >>> d9 = Date(2024, 2, 29)
    >>> d9.tomorrow()
    >>> repr(d9)
    'Date(2024, 3, 1)'
    >>> d10 = Date(2024, 3, 31)
    >>> d10.tomorrow()
    >>> repr(d10)
    'Date(2024, 4, 1)'
    """
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    def __str__(self):
        return f"{self.month:02d}/{self.day:02d}/{self.year:04d}"
        
    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"
        
    def is_leap_year(self):
        if self.year % 4 != 0:
            return False
        if self.year % 100 != 0:
            return True
        return self.year % 400 == 0
        
    def is_valid(self):
        if self.year == 0 or self.month < 1 or self.month > 12 or self.day < 1:
            return False
            
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() and self.month == 2:
            return self.day <= 29
            
        return self.day <= days_in_month[self.month]
        
    def tomorrow(self):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_in_month[2] = 29
            
        self.day += 1
        if self.day > days_in_month[self.month]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
                days_in_month[2] = 28

if __name__ == "__main__":
    import doctest
    doctest.testmod()