from ctypes import c_char, pythonapi, py_object
import sys as Система
import os as ОС

from _io import BufferedReader, BufferedWriter, TextIOWrapper

Адреса_памяти_классов = {}

def Добавить_поле(класс, название, значение, функция = True):
    def Получить_память(где):
        if где in Адреса_памяти_классов: return Адреса_памяти_классов[где]
        else:
            адрес = memoryview((c_char * type(где).__sizeof__(где)).from_address(id(где))).cast('c').cast('P')
            Адреса_памяти_классов[где] = адрес
            return адрес

    def Установить_поле(класс, поле, значение):
        смещение_флагов = [*Получить_память(int)].index(int.__flags__)
        флаги = класс.__flags__
        память_класса = Получить_память(класс)
        if Система.version_info[0:2] <= (3, 9): память_класса[смещение_флагов] |= 1 << 9
        elif Система.version_info[0:2] >= (3, 10): память_класса[смещение_флагов] &= ~(1 << 8)
        setattr(класс, поле, значение)
        память_класса[смещение_флагов] = флаги
        pythonapi.PyType_Modified(py_object(класс))

    def Новая_функция(функция, **параметры):
        код = функция.__code__
        копия = type(функция)(
            код.replace(co_consts = код.co_consts + tuple((ключ, значение) for ключ, значение in параметры.items())),
            функция.__globals__,
            name=функция.__name__,
            closure=функция.__closure__
        )
        копия.__defaults__ = функция.__defaults__
        копия.__kwdefaults__ = функция.__kwdefaults__
        копия.__qualname__ = функция.__qualname__
        return копия

    Установить_поле(класс, название, Новая_функция(значение) if функция else значение)

Встроенные_поля = {
    ('str', 'bytes', 'bytearray'): {
        'find': 'Найти',
        'rfind': 'Найти_с_конца',
        'index': 'Положение',
        'rindex': 'Положение_с_конца',
        'replace': 'Заменить',
        'split': 'Разбить',
        'isdigit': 'Из_цифр',
        'isalpha': 'Из_букв',
        'isalnum': 'Из_цифробукв',
        'islower': 'Из_строчных',
        'isupper': 'Из_заглавных',
        'isspace': 'Из_пробелов',
        'istitle': 'Слова_с_заглавных',
        'upper': 'В_заглавные',
        'lower': 'В_строчные',
        'startswith': 'Начинается',
        'endswith': 'Кончается',
        'join': 'Сцепить',
        'capitalize': 'Начать_с_заглавной',
        'center': 'Отцентровать',
        'count': 'Число_вхождений',
        'expandtabs': 'Табуляции_в_пробелы',
        'lstrip': 'Удалить_в_начале',
        'rstrip': 'Удалить_в_конце',
        'strip': 'Удалить_по_бокам',
        'partition': 'Разбить',
        'rpartition': 'Разбить_с_конца',
        'swapcase': 'Обратить_регистр',
        'title': 'Начать_слова_с_заглавных',
        'zfill': 'Дополнить_нулями',
        'ljust': 'Дополнить_справа',
        'rjust': 'Дополнить_слева'
    },
    'str': {
        'format': 'Формат',
        'encode': 'Закодовать'
    },
    ('bytes', 'bytearray'): {
        'decode': 'Раскодовать'
    },
    ('list', 'bytearray'): {
        'append': 'Добавить',
        'clear': 'Очистить',
        'copy': 'Копия',
        'count': 'Число_вхождений',
        'extend': 'Дополнить',
        'index': 'Положение',
        'insert': 'Вставить',
        'pop': 'Вытащить',
        'remove': 'Удалить',
        'reverse': 'Обратить'
    },
    'list': {
        'sort': ( 'Упорядочить', { 'key': 'ключ', 'reverse': 'обратно' } )
    },
    'dict': {
        'clear': 'Очистить',
        'copy': 'Копия',
        'fromkeys': 'Из_ключей',
        'get': 'Получить',
        'items': 'Элементы',
        'keys': 'Ключи',
        'values': 'Значения',
        'pop': 'Вытащить',
        'popitem': 'Вытащить_последнее',
        'setdefault': 'Получить_или_добавить',
        'update': 'Обновить',
        'values': 'Значения'
    },
    'tuple': {
        'index': 'Положение',
        'count': 'Число_вхождений'
    },
    ('set', 'frozenset'): {
        'isdisjoint': 'Не_пересекаются',
        'issubset': 'Подмножество',
        'issuperset': 'Надмножество',
        'union': 'Объединение',
        'intersection': 'Пересечение',
        'difference': 'Разница',
        'symmetric_difference': 'СимметрРазница',
        'copy': 'Копия'
    },
    'set': {
        'update': 'Дополнить',
        'intersection_update': 'Пересечь',
        'difference_update': 'Вычесть',
        'symmetric_difference_update': 'СимметрВычесть',
        'add': 'Добавить',
        'remove': 'Удалить',
        'discard': 'Убрать',
        'pop': 'Вытащить',
        'clear': 'Очистить'
    },
    'int': {
        'bit_length': 'Длина_в_битах',
        'to_bytes': ( 'В_байты', { 'length': 'длина', 'byteorder': 'порядок', 'signed': 'со_знаком' }, { (2, 'byteorder'): { 'МлСт': 'little', 'СтМл': 'big' } } ),
        'from_bytes': ( 'Из_байтов', { 'bytes': 'байты', 'byteorder': 'порядок', 'signed': 'со_знаком' }, { (1, 'byteorder'): { 'МлСт': 'little', 'СтМл': 'big' } } ),
        '.numerator': 'числитель',
        '.denominator': 'знаменатель'
    },
    'float': {
        'is_integer': 'Целое',
        'hex': 'В_шестн',
        'fromhex': 'Из_шестн'
    },
    ('int', 'float'): {
        'as_integer_ratio': 'В_дробь'
    },
    ('int', 'float', 'complex'): {
        '.real': 'действ_часть',
        '.imag': 'мнимая_часть',
        'conjugate': 'Cопряжённое'
    },
    ('BufferedReader', 'BufferedWriter', 'TextIOWrapper'): {
        'read': 'Читать',
        'readline': 'Читать_строку',
        'write': 'Писать',
        'tell': 'Позиция',
        'seek': 'Задать_позицию',
        'truncate': 'Изменить_размер',
        'detach': 'Отделить',
        'close': 'Закрыть',
        '.closed': 'закрыт'
    }
}

for классы, таблица in Встроенные_поля.items():
    if type(классы) != tuple: классы = [классы]
    for класс in классы:
        for название, замена in таблица.items():
            if type(замена) == tuple:
                замещающая_функция = 'def __' + класс + '_' + название + '__(*ПА, **ИА):\n'
                for н, з in замена[1].items():
                    замещающая_функция += '    if "' + з + '" in ИА: ИА["' + н + '"] = ИА.pop("' + з + '")\n'
                if len(замена) > 2:
                    for зам_арг, знач_зам in замена[2].items():
                        if зам_арг[0] != -1:
                            замещающая_функция += '    if len(ПА) > ' + str(зам_арг[0]) + ' and ПА[' + str(зам_арг[0]) + '] in ' + str(list(знач_зам.keys())) + ':\n'
                            замещающая_функция += '        ПА = ПА[:' + str(зам_арг[0]) + '] + tuple([' + str(знач_зам) + '[ПА[' + str(зам_арг[0]) + ']]]) + ПА[' + str(зам_арг[0] + 1) + ':]\n'
                        if зам_арг[1] != '':
                            замещающая_функция += '    if "' + зам_арг[1] + '" in ИА.keys() and ИА["' + зам_арг[1] + '"] in ' + str(list(знач_зам.keys())) + ':\n'
                            замещающая_функция += '        ИА["' + зам_арг[1] + '"] = ' + str(знач_зам) + '[ИА["' + зам_арг[1] + '"]]\n'
                замещающая_функция += '    return ' + класс + '.' + название + '(*ПА, **ИА)'
                exec(замещающая_функция)
                exec("Добавить_поле(" + класс + ", '" + замена[0] + "', __" + класс + "_" + название + "__)")
                exec('del __' + класс + '_' + название + '__')
            else:
                if название[0] == '.':
                    eval("Добавить_поле(" + класс + ", '" + замена + "', " + класс + название + ", False)")
                else:
                    eval("Добавить_поле(" + класс + ", '" + замена + "', lambda *ПА, **ИА: " + класс + "." + название + "(*ПА, **ИА))")

Система.path.insert(0, ОС.path.dirname(__file__) + '/Модули')

Обёртка__Вещ_в_стр = lambda здесь: Вещ_в_стр(здесь).replace('.', ',').replace('inf', 'Бскн')
Вещ_в_стр = float.__str__
Добавить_поле(float, '__str__', Обёртка__Вещ_в_стр)

Обёртка__Логич_в_стр = lambda здесь: Логич_в_стр(здесь).replace('True', 'Да').replace('False', 'Нет')
Логич_в_стр = bool.__str__
Добавить_поле(bool, '__str__', Обёртка__Логич_в_стр)

Обёртка__Пусто_в_стр = lambda здесь: Пусто_в_стр(здесь).replace('None', 'Пусто')
Пусто_в_стр = type(None).__str__
Добавить_поле(type(None), '__str__', Обёртка__Пусто_в_стр)

def Проверить_существование(код, местн, общ):
    try: eval(код, местн, общ)
    except Exception as ошибка:
        if type(ошибка) in (NameError, KeyError, AttributeError):
            print(ошибка)
            return False
        else: raise ошибка
    return True

def Заменить_ключи_в_словаре(словарь, замены):
    новый = {}
    for н, з in словарь.items():
        новый.setdefault(замены[н] if н in замены.keys() else н, з)
    return новый

def Свёртка(функция, перебираемое, нач_знач = None):
    рез = нач_знач if нач_знач else перебираемое[0]
    for эл in перебираемое: рез = функция(рез, эл)
    return рез

__builtins__.update(
    __Проверить_существование__ = Проверить_существование,
    Свёртка = Свёртка
)
