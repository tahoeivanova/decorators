# декоратор простой
def simple_decorator(f):
    def wrapper():
        print('Код до функции')
        f()
        print('Код после функции')
    return wrapper


# Эту функцию мы передаем в качестве параметра другой функции.
def simple_function():
    print('Я простая функция')
    return 10

# создадим объект функции
f = simple_function
print(f)
print()

simple_function()
print(id(simple_function))

simple_function_decorated = simple_decorator(simple_function)
print(simple_function)
print(hash(simple_function_decorated))
print(hash(simple_decorator(simple_function)))

simple_function_decorated()

