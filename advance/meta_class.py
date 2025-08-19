class UpperCaseMeta(type):
    def __new__(cls, name, bases, attrs):
        uppercase_attrs = {k.upper(): v for k, v in attrs.items()}
        return super().__new__(cls, name, bases, uppercase_attrs)
    
class MyClass(metaclass=UpperCaseMeta):
    def my_method(self):
        return "This is a method in MyClass"

# Example usage
if __name__ == "__main__":
    obj = MyClass()
    print(obj.MY_METHOD())  # Should print: This is a method in MyClass    