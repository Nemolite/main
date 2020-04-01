
class Square:
 
    @staticmethod
    def get_squares(a, b):
        return a*a, b*b
 
print(Square.get_squares(3, 5))

tmp = Square.get_squares(3, 5)

print(tmp) 
print(type(tmp))