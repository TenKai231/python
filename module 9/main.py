# class Kalkulator:
#     # kalkulator tambaha kurang
#     def __init__(self, _i):
#         self.i = _i

#     def tambah(self, _i):
#         return self.i + _i

#     def kurang(self, _i):
#         return self.i - _i


class DividenByZeroError(Exception):
    def __init__(self, message = "Tidak bisa membagi dengan nol"):
        self.message = message
        super().__init__(self.message)

def divide_numbers(a, b):
    if b == 0:
        raise DividenByZeroError("Cannot divide by zero")
    return a / b

try:
    result  = divide_numbers(10, 0)
except DividenByZeroError as e:    
    print(f"Error: {e}")


