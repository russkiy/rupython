Русская версия языка Python, реализованная в виде транслятора кода в код Python.

Русский Питон почти полностью идентичен оригинальному языку с англоязычной лексической базой, основное отличие заключается в использовании русских названий для именования сущностей в коде. Данный инструмент создан для достижения двух целей:

* Повышение производительности труда работников, выполняющих задачи автоматизации процессов и формализации алгоритмов, за счёт применения лексики на родном им языке, что априори повышает усвоение и читаемость кода.
* Упрощение освоения навыков алгоритмизации и составления компьютерных программ учащимися путём устранения искусственного препятствия в виде необходимости оперировать лексикой иностранного языка.

Приложения на Русском Питоне могут использовать все возможности оригинального Python, включая всё богатство подключаемых пакетов и библиотек. Код может быть написан на обоих вариантах языка.

### Установка

Транслятор устанавливается как пакет соответствующей командой:

`pip install rupython`

Если "pip" выдаёт ошибку "externally-managed-environment" (под некоторыми версиями ОС Linux), то установка производится следущей командой:

`pip install rupython --break-system-packages`

Код модулей Русского Питона размещается в файлах с расширением **.крп**. Для интеграции в операционную систему необходимо ассоциировать эти файлы с транслятором. Например, для ОС Windows это выполняется следующими консольными командами:

```
assoc .крп = "Код на Русском Питоне"
ftype "Код на Русском Питоне"=py -m rupython "%%1" %%*
```

### Примеры кода

```
Функция НОД(*числа):
	f = фун a, b: a если b == 0 иначе f(b, a % b)
	Вернуть Свёртка(фун a, b: f(a, b), числа)

Функция НОК(*числа):
	числа = Множ(числа)
	n = n_ = Макс(числа)
	числа.Удалить(n)
	Пока Любое(n % m для m в числа): n += n_
	Вернуть n
```

```
Функция Дата_Пасхи(год, нов_ст = Пусто):
	д = (год % 19 * 19 + 15) % 30
	д += (год % 4 * 2 + год % 7 * 4 + 6 * д + 6) % 7
	нов_ст = Да если нов_ст это Пусто и год >= 1918 иначе нов_ст
	Если не нов_ст:
		Если д > 9: Вернуть Строка(д - 9) + ' апреля'
		Иначе: Вернуть Строка(22 + д) + ' марта'
	Иначе:
		п = год // 100 - год // 400 - 2
		Если д > 39 - п: Вернуть Строка(д - 39 + п) + ' мая'
		Иначе: Вернуть Строка(д - 9 + п) + ' апреля'
```

### Обзор особенностей языка

##### Основные встроенные типы данных:

* Числовые: ```Цел```, ```Вещ```, ```Компл```.
* Логический: ```Логич``` – значения ```Да``` и ```Нет```.
* Неопределённое значение: ```Пусто``` (пустое значение, или ничего).
* Строковый (текстовый): ```Строка```.
* Последовательности: ```Список```, ```Кортеж```, ```Ряд``` (диапазон).
* Ассоциативный массив: ```Словарь```.
* Множества: ```Множ``` и ```НеизмМнож```.
* Байтовые: ```Байты``` и ```БайтМассив```.

Далее представлены примеры кода, демонстрирующие использование наиболее важных языковых конструкций.

##### Условие:
```
Если x > 0:
	зн = 1
АЕсли x < 0:
	зн = -1
Иначе:
	зн = 0
```

##### Цикл перебора:
```
Для перем из Ряд(10):
	Вывести(перем)
```

##### Цикл с предусловием:
```
Пока x < знач:
	x += y
	Если x == z: Продолжить
```

##### Цикл с послеусловием:
```
Повторять:
	x *= z
	Если x >= y: Прервать
До x > знач
```

##### Цикл со счётчиком:
```
Цикл i = 0 : i < 10 : i += 1:
	Вывести(i)
```

##### Импорт:
```
Из Пакет_1 подключить Модуль_1, Модуль_2
Подключить Модуль_3 как М3
```

##### Логические операции:
```
v = не x и (y или z)
u = w в сп1 и w не в сп2
k = l это m и m это не n
```

##### Функция:
```
Функция F(a, b):
	Если a == b: Вернуть Да
	Иначе: Вернуть Нет
```

```
Функция Пример(парам):
	Для сч из Ряд(парам):
		Если парам[сч] == 0: Возврат
```

##### Генераторы
```
Функция Фиб(n):
    a, b = 0, 1
    Для _ из Ряд(n):
        Выдать a
        a, b = b, a + b
```
```
кв_ч = (сч ** 2 для сч в Ряд(1, 10))
```

##### Класс
```
Класс Пример(Другой_класс):
	Функция __Подготовка__(здесь, перем = 0):
		здесь.зн = перем

Объект = Пример(1)
```

##### Значение по условию
```
перем = 0 если x == зн иначе 1
```

##### Пропуск действия и удаление переменной
```
Если x == 1: Пропустить
Иначе: Удалить y
```

##### Краткое условие
```
перем = 1 если x > 0 иначе 0
```

##### Пропуск действия и удаление переменной
```
Если x == 1: Пропустить
Иначе: Удалить y
```

##### Безымянная (λ) функция
```
В_квадрат = фун x: x ** 2
```

##### Обработка исключений:
```
Попробовать:
	ч = Цел(строка)
ПриИсключении ОшибкаЗначения:
	Вывести('Ошибка.')
Иначе: Вывести('Сработало.')
ВКонце: Вывести('Выполнено.')

Если Тип(x) != Стр:
	Бросить ОшибкаЗначения
```

##### Области видимости
```
x = 0

Функция Внешняя():
	y = 1
	Функция Внутренняя():
		Общее x
		НеМестное y
		x = y
	Внутренняя()
```

##### Проверка существования переменной:
```
Если $Переменная?: Вывести('Существует.')
```

##### Обёртка (декоратор) функции
```
Функция Обёртка(Ф):
    Функция ФО():
        Вывести('1')
        Ф()
    Вернуть ФО

@Обёртка
Функция Проверка(): Вывести('2')
```

##### Конструкция выбора
```
Выбрать x:
	При 1: зн = '+'
	При -1: зн = '-'
	При _: зн = '0'
```

##### Контекстный менеджер
```
ВКонтексте Открыть('Файл.дан', 'r') как файл:
	Пока стр := файл.Читать_строку():
		Вывести(стр.Удалить_по_бокам())
```

##### Проверка условия
```
Функция Разделить(x, y):
	Проверить y != 0, 'Деление на 0.'
	Вернуть x / y
```

### Встроенные функции и обёртки
```
АбсЗнач(x)
АсПеребиратель(асинхр_перебираемое)
Все(перебираемое)
Любое(перебираемое)
АсСледущий(асинхр_перебиратель[, по_умолчанию])
В7битовСимв(объект)
Двоич(x)
Логич(объект = Нет)
Останов(*ПА, **ИА)
БайтМассив([источник = ''[, кодование[, при_ошибках]]])
Байты([источник = ''[, кодование[, при_ошибках]]])
Вызываемое(объект)
Код_в_знак(i)
@Метод_класса
Собрать_код(исходник, название_файла, режим, флаги = 0, не_наследовать = Нет, оптимизация = -1)
Компл(число = 0 | строка | действ_часть = 0, мнимая_часть = 0)
Удалить_поле(объект, название)
Словарь([отображение | перебираемое], **ИА)
Содержимое([объект])
ДелОст(a, b)
Перечислить(перебираемое, начало = 0)
ВычВыр(исходник, общие_сущности = Пусто, местные_сущности = Пусто)
ВыпКод(исходник, общие_сущности = Пусто, местные_сущности = Пусто, замыкание = Пусто)
Фильтр(функция, перебираемое)
Вещ(число = 0.0 | строка)
Формат(значение, описание = '')
НеизмМнож(перебираемое = Множ())
Получить_поле(объект, название[, по_умолчанию])
Общие_сущности()
Имеет_поле(объект, название)
Хэш(объект)
Справка([запрос])
Шестн(x)
Идент(объект)
Принять(сообщение)
Цел(число = 0 | строка, основание = 10)
Экземпляр(объект, класс)
Подкласс(класс, надкласс)
Перебиратель(объект[, исключение])
Длина(s) | Размер(s)
Список([перебираемое])
Местные_сущности()
Отображение(функция, перебираемое, *перебираемые)
Макс((перебираемое[, если_пусто] | аргумент_1, аргумент_2, * аргументы), ф_сравнения = Пусто)
Память(объект)
Мин((перебираемое[, если_пусто] | аргумент_1, аргумент_2, * аргументы), ф_сравнения = Пусто)
Следующий(перебиратель[, по_умолчанию])
Объект()
Восьм(x)
Открыть(название, режим = 'r', буферизация = -1, кодование = Пусто, при_ошибках = Пусто, новая_строка = Пусто, закрыть_описатель = Да, открыватель = Пусто)
Знак_в_код(c)
Степень(основание, показатель, модуль = Пусто)
Вывести(*объекты, разделитель = ' ', в_конце = '\n', файл = Пусто, немедленно = Нет)
[@]Свойство(ф_получения = Пусто, ф_установки = Пусто, ф_удаления = Пусто, документация = Пусто)
Ряд(длина | нач, кон, шаг = 1)
Представление(объект)
Обратить(последовательность)
Округлить(число, разрядов = Пусто)
Множ([перебираемое])
Установить_поле(объект, название, значение)
Срез(длина | нач, кон, шаг = 1)
Упорядочить(перебираемое, ф_сравнения, наоборот)
[@]Статический_метод(функция)
Строка(объект[, кодование = 'utf-8', при_ошибках = 'strict')
Сумма(перебираемое[, начало = 0])
Надкласс([тип, порядок_поиска = Пусто])
Кортеж([перебираемое])
Тип(объект | название, надклассы, поля, **ключевые_слова)
Поля([объект])
Упаковать(*перебираемые, проверить_длины = Нет)
Свёртка(функция, перебираемое, нач_знач = Пусто)
@Метод_получения
@Метод_установки
@Метод_удаления
__Подключить__(название, общие_сущности = Пусто, местные_сущности = Пусто, по_списку = 0, уровень = 0)
```
