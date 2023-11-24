import re
import doctest

# день.месяц.год (14.09.2022, 5.02.1995, 01.4.2012)
pattern1 = r'\b\d{1,2}\.\d{1,2}\.\d{4}\b'

# день/месяц/год (14/09/2022, 5/02/1995, 01/4/2012)
pattern2 = r'\b\d{1,2}/\d{1,2}/\d{4}\b'

# день-месяц-год (14-09-2022, 5-02-1995, 01-4-2012)
pattern3 = r'\b\d{1,2}-\d{1,2}-\d{4}\b'

# год.месяц.день (2022.09.14, 1995.02.5, 2012.4.01)
pattern4 = r'\b\d{4}\.\d{1,2}\.\d{1,2}\b'

# год/месяц/день (2022/09/14, 1995/02/5, 2012/4/01)
pattern5 = r'\b\d{4}/\d{1,2}/\d{1,2}\b'

# год-месяц-день (2022-09-14, 1995-02-5, 2012-4-01)
pattern6 = r'\b\d{4}-\d{1,2}-\d{1,2}\b'

# день месяц_rus год (14 сентября 2022, 5 февраля 1995, 01 апреля 2012)
pattern7 = r'\d{1,2}+\s\[а-я]+\s\d{4}'

# Месяц_eng день, год (September 14, 2022, February 5, 1995, April 01, 2012)
pattern8 = r'\b\[a-zA-z]+\s\d{1,2},\s\d{4}\b'

# Мес_eng день, год (Sep 14, 2022, Feb 5, 1995, Apr 01, 2012)
pattern9 = r'\b\[a-zA-Z]{3}\s\d{1,2},\s\d{4}\b'

# год, Месяц_eng день (2022, September 14, 1995, February 5, 2012, April 01)
pattern10 = r'\b\d{4},\s\[a-zA-Z]+\s\d{1,2}\b'

# год, Мес_eng день (2022, Sep 14, 1995, Feb 5, 2012, Apr 01)
pattern11 = r'\b\d{4},\s\[a-zA-Z]{3}\s\d{1,2}\b'
def check_date(date):
    """
    Функция, проверяющая корректность введенной даты

    Args:
    -password: str - дата

    Returns:
    bool: корректна или некорректна введеная дата

    Doctests:
    >>> check_date('20 января 1806')
    True
    >>> check_date('1924, July 25')
    True
    >>> check_date('26/09/1635')
    True
    >>> check_date('3.1.1506')
    True
    >>> check_date('25.08-1002')
    False
    >>> check_date('декабря 19, 1838')
    False
    >>> check_date('8.20.1973')
    False
    >>> check_date('Jun 7, -1563')
    False
    >>> check_date('31 февраля 2023')
    False
    >>> check_date('31 июня 2015')
    False
    """

    if (re.match(pattern1, date) or
            re.match(pattern2, date) or
            re.match(pattern3, date) or
            re.match(pattern4, date) or
            re.match(pattern5, date) or
            re.match(pattern6, date) or
            re.match(pattern7, date) or
            re.match(pattern8, date) or
            re.match(pattern9, date) or
            re.match(pattern10, date) or
            re.match(pattern11, date)):

        return True
    else:
        return False


doctest.testmod(verbose=True)


