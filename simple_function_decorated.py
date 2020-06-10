import time
import requests
from bs4 import BeautifulSoup
import logging


# logger = logging.getLogger(__name__)


# logging.basicConfig(filename='example.log', format='%(asctime)s --- %(levelname)s --- %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='a', level=logging.DEBUG)
# logging.debug('This message should go to the logged file')
# logging.info('So should this')
# logging.warning('And this, too')

# самый простой декоратор
def show_info(f):
    def wrapper(*args, **kwargs):
        print('Код до функции!')
        f(*args, **kwargs)
        print('Код после функции!')
    return wrapper


@show_info
def simple_function():
    print('Я простая функция!')

simple_function()

# simple_function_decorated = show_info(simple_function)
# simple_function_decorated()





# декоратор, который принимает на вход параметры

# декоратор, который выводи типы
# мы не знаем, какие параметры у f, поэтому используем *args, **kwargs
def show_type(f):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(f.__name__)

        print('Тип 1-ой параметра', type(args[0]))
        print(f(*args, **kwargs))
        print('Тип 1-ого параметра!', type(args[1]))
        print(logger)
    return wrapper
@show_info
@show_type
def my_add(a,b):

    return a + b

my_add(100, 1)

def show_time(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f'URL: {args[0]}')

        print(f(*args, **kwargs))
        finish_time = time.time()
        dif_time = finish_time - start_time
        print(f'Время выполнения функции: {dif_time}')
    return wrapper

@show_time
def requests_example(url):
    web_page = requests.get(url)
    soup = BeautifulSoup(web_page.text, 'html.parser')
    parsed_text = soup.title.text

    return parsed_text


URL = 'https://github.com/MachineLearningIsEasy/python_lesson_8/blob/master/decorators_example.py'
print('Запрос')
requests_example(URL)

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')