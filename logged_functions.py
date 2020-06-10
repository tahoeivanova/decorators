import logging
import logging.config

# logging.config.fileConfig('logging.conf')



# декоратор, который записывает лог функции
def func_logger_decorator(f):
    def wrapper(*args, **kwargs):

        # create logger with confif
        # logger = logging.getLogger('simpleExample')

        # create logger
        func_name = f.__name__
        logger = logging.getLogger(func_name)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        '''
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        '''
        # create file handler

        ch = logging.FileHandler(f'{func_name}.log', mode='a')
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger

        logger.addHandler(ch)

        logger.info(f'Вызвана функция {f.__name__}')
        result = f(*args, **kwargs)
        logger.info(f'Результат функции: {result}')
        # return f
    return wrapper

@func_logger_decorator
def my_mult(a,b):
    return a*b


if __name__ == '__main__':
    my_mult(1,45)

