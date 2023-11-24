import re
import doctest

regex = r'^(?=[A-Za-z\d^$%@#&*])(?=.{8,})(?=(?:.*[a-z].*){2,})(?=.+\d)(?=[^,.!?]*$).*([\^$%@#&*]).*(?!\1)([\^$%@#&*]).*(?!\1)(?!\2)([\^$%@#&*]).*$'

def check_password(password) :
    """
    Функция, проверяющая корректность введенного пароля

    Args:
    -password: str - пароль

    Returns:
    bool: корректен или некорректен введеный пароль

    Doctests:
    >>> check_password('rtG&3FG#Tr^e')
    True
    >>> check_password('a^A1@*@1Aa')
    True
    >>> check_password('oF^a1D@y5%e6')
    True
    >>> check_password('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True
    >>> check_password('пароль')
    False
    >>> check_password('password')
    False
    >>> check_password('qwerty')
    False
    >>> check_password('lOngPa$$W0Rd')
    False
    >>> check_password('пбPaaSS#%*W0rD') #проверка на буквы не латинского алфавита нижнего регистра
    False
    >>> check_password('ПБPaaSS#%*W0rD') #проверка на буквы не латинского алфавита верхнего регистра
    False
    >>> check_password('aS#%*0r') #проверка на длину пароля
    False
    >>> check_password('PSS#%*W0D') #проверка на наличие 2х и больше символов нижнего регистра латинского алфавита
    False
    >>> check_password('PaSS#%*W0D') #проверка на наличие 2х и больше символов нижнего регистра латинского алфавита
    False
    >>> check_password('PaaSS#%*WrD') #проверка на наличие цифр
    False
    >>> check_password('PaaSS#%W0rD') #проверка на количество специальных символов
    False
    >>> check_password('PaaSS##&W0rD') #проверка на различие специальных символов
    False
    >>> check_password('PaaSS#*&W0rD!') #проверка на наличие запрещенных символов
    False

    """
    if re.match(regex, password):
        return True
    else:
        return False

doctest.testmod(verbose=True)
