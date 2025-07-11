<img src="https://raw.githubusercontent.com/russkiy/rupython/refs/heads/main/Логотип.png" width=200 align=right /> Русская версия языка Python, реализованная в виде транслятора кода в код Python.

Русский Питон почти полностью идентичен оригинальному языку с англоязычной лексической базой, основное отличие заключается в использовании русских названий для именования сущностей в коде. Данный инструмент создан для достижения двух целей:

* Повышение производительности труда работников, выполняющих задачи автоматизации процессов и формализации алгоритмов, за счёт применения лексики на родном им языке, что априори повышает усвоение и читаемость кода.
* Упрощение освоения навыков алгоритмизации и составления компьютерных программ учащимися путём устранения искусственного препятствия в виде необходимости оперировать лексикой иностранного языка.

Когда-то, в эпоху, когда железо и разум сливались в первых советских вычислительных машинах, русские ЯП были не просто инструментом — они были голосом нации, стремящейся к технологическому величию. В цехах заводов, на полигонах оборонных предприятий и в тиши академических кабинетов инструкции программного кода звучали на русском языке, воплощая мощь отечественной промышленности и науки. Сегодня, когда цифровой мир задаёт ритм жизни, возрождение русских ЯП становится не просто возможностью, но и необходимостью — способом вернуть себе право творить технологии на родном языке.

Алгоритмические языки на русской лексической базе повышают производительность труда разработчиков, поскольку работа на знакомом языке не требует от них приложения ненужных умственных усилий для переключения на иностранный язык, чем снижается когнитивная нагрузка, улучшается читаемость и качество создаваемого кода и повышается эффективность коммуникации в команде. Русский код априори является более понятным и воспринимаемым интуитивно в контексте культурных и языковых особенностей русских людей, снижая порог вхождения и устраняя искусственный барьер в виде необходимости овладения иностранным языком на уровне, достаточном для беглого чтения кода.

Приложения на Русском Питоне могут использовать все возможности оригинального Python, включая всё богатство подключаемых пакетов и библиотек. Код может быть написан на обоих вариантах языка. Технически инструмент представляет собой сочетание собственно транслятора кода Русского Питона в оригинальный Python с модулем, модифицирующим встроенные объекты, а также обёртками над модулями стандартной библиотеки.

### Установка

Транслятор устанавливается как пакет соответствующей командой:

`pip install rupython`

Если "pip" выдаёт ошибку "externally-managed-environment" (под некоторыми версиями ОС Linux), то установка производится следущей командой:

`pip install rupython --break-system-packages`

Код модулей Русского Питона размещается в файлах с расширением **.крп**. Для интеграции в операционную систему необходимо ассоциировать эти файлы с транслятором. Для автоматической установки ассоциации выполните командный файл "FA_Windows.bat" или "FA_Linux.sh" в зависимости от операционной системы, размещённый вместе с исходным кодом.

Исходный код размещён тут: https://github.com/russkiy/rupython

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
кв_ч = (сч ** 2 для сч из Ряд(1, 10))
```

##### Класс
```
Класс Пример(Другой_класс):
	Функция __Подготовка__(экземпляр, перем = 0):
		экземпляр.зн = перем

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

##### Обработка исключений
```
Попробовать:
	ч = Цел(строка)
Перехватив ОшибкаЗначения:
	Вывести('Ошибка.')
Иначе: Вывести('Сработало.')
Завершив: Вывести('Выполнено.')

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
Используя Открыть('Файл.дан', 'r') как файл:
	Пока стр := файл.Читать_строку():
		Вывести(стр.Удалить_по_бокам())
```

##### Проверка условия
```
Функция Разделить(x, y):
	Проверить y != 0, 'Деление на 0.'
	Вернуть x / y
```

---

### Встроенные функции и обёртки

###### `АбсЗнач(x)`
Возвращает модуль (абсолютное значение) числа `x`.

###### `АсПеребиратель(асинхр_перебираемое)`
Создаёт асинхронный перебиратель из асинхронно перебираемого объекта.

###### `Все(перебираемое)`
Возвращает `Да`, если все элементы перебираемого истинны, иначе `Нет`.

###### `Любое(перебираемое)`
Возвращает `Да`, если хотя бы один элемент перебираемого истинный.

###### `АсСледущий(асинхр_перебиратель[, по_умолчанию])`
Возвращает следующий элемент асинхронного перебирателя. Если элементы закончились и задан `по_умолчанию`, возвращает его.

###### `В7битовСимв(объект)`
Возвращает строковое представление объекта из 7-битовых символов, экрануя остальные.

###### `Двоич(x)`
Преобразует целое число `x` в строку его двоичного представления.

###### `Логич(объект = Нет)`
Возвращает `Да`, если объект логически истинный, иначе `Нет`.

###### `Останов(*ПА, **ИА)`
Запускает отладчик в текущей точке выполнения.

###### `БайтМассив([источник = ''[, кодование[, при_ошибках]]])`
Создаёт изменяемый массив байтов. При передаче строки — кодует её.

###### `Байты([источник = ''[, кодование[, при_ошибках]]])`
Создаёт неизменяемую последовательность байтов.

###### `Вызываемое(объект)`
Проверяет, можно ли объект вызвать как функцию.

###### `Код_в_знак(i)`
Возвращает многобайтовый символ по его числовому коду.

###### `@Метод_класса`
Обёртка (декоратор), делающая функцию методом класса (первый аргумент — сам класс).

###### `Собрать_код(исходник, название_файла, режим, флаги = 0, не_наследовать = Нет, оптимизация = -1)`
Компилирует строку в объект кода.

###### `Компл(число = 0 | строка | действ_часть = 0, мнимая_часть = 0)`
Создаёт комплексное число из строки, числа или пары вещественных частей.

###### `Удалить_поле(объект, название)`
Удаляет атрибут объекта по названию.

###### `Словарь([отображение | перебираемое], **ИА)`
Создаёт словарь. Принимает пары ключ-значение, отображение или именованные аргументы.

###### `Содержимое([объект])`
Возвращает список доступных атрибутов объекта.

###### `ДелОст(a, b)`
Возвращает кортеж `(a // b, a % b)` — целая часть и остаток от деления.

###### `Перечислить(перебираемое, начало = 0)`
Возвращает пары `(индекс, элемент)` с начала `начало`.

###### `ВычВыр(исходник, общие_сущности = Пусто, местные_сущности = Пусто)`
Вычисляет выражение из строки и возвращает результат.

###### `ВыпКод(исходник, общие_сущности = Пусто, местные_сущности = Пусто, замыкание = Пусто)`
Выполняет код из строки. Не возвращает результат.

###### `Фильтр(функция, перебираемое)`
Фильтрует элементы, для которых функция возвращает `Да`.

###### `Вещ(число = 0.0 | строка)`
Преобразует аргумент в число с плавающей запятой.

###### `Формат(значение, описание = '')`
Форматует значение по шаблону.

###### `НеизмМнож(перебираемое = Множ())`
Создаёт неизменяемое множество.

###### `Получить_поле(объект, название[, по_умолчанию])`
Возвращает атрибут объекта. Если не существует — возвращает `по_умолчанию`, если задано.

###### `Общие_сущности()`
Возвращает глобальные переменные текущего контекста.

###### `Имеет_поле(объект, название)`
Проверяет наличие атрибута у объекта.

###### `Хэш(объект)`
Возвращает хэш-значение объекта.

###### `Справка([запрос])`
Выводит встроенную справку.

###### `Шестн(x)`
Преобразует число `x` в строку его шестнадцатеричного представления.

###### `Идент(объект)`
Возвращает уникальный идентификатор объекта.

###### `Принять(сообщение)`
Читает строку с клавиатуры. Показывает `сообщение`, если задано.

###### `Цел(число = 0 | строка, основание = 10)`
Преобразует в целое число. Для строки можно указать основание.

###### `Экземпляр(объект, класс)`
Проверяет, является ли объект экземпляром класса.

###### `Подкласс(класс, надкласс)`
Проверяет, является ли `класс` подклассом `надкласс`.

###### `Перебиратель(объект[, исключение])`
Возвращает перебиратель (итератор) по объекту.

###### `Длина(s)`
Возвращает количество элементов в последовательности или коллекции.

###### `Список([перебираемое])`
Создаёт список из перебираемого объекта или пустой список.

###### `Местные_сущности()`
Возвращает словарь локальных переменных в текущем контексте.

###### `Отображение(функция, перебираемое, *перебираемые)`
Применяет `функцию` к каждому набору элементов из `перебираемых`.

###### `Макс((перебираемое[, если_пусто] | аргумент_1, аргумент_2, *аргументы), ф_сравнения = Пусто)`
Возвращает наибольшее значение. Можно передавать последовательность **или** несколько аргументов.

###### `Память(объект)`
Возвращает представление объекта на уровне байтов.

###### `Мин((перебираемое[, если_пусто] | аргумент_1, аргумент_2, *аргументы), ф_сравнения = Пусто)`
Возвращает наименьшее значение. Можно передавать последовательность **или** несколько аргументов.

###### `Следующий(перебиратель[, по_умолчанию])`
Возвращает следующий элемент из перебирателя. Если элементов больше нет и задан `по_умолчанию`, возвращает его.

###### `Объект()`
Базовый класс для всех объектов.

###### `Восьм(x)`
Преобразует целое число `x` в строку его восьмеричного представления.

###### `Открыть(название, режим = 'r', буферизация = -1, кодование = Пусто, при_ошибках = Пусто, новая_строка = Пусто, закрыть_описатель = Да, открыватель = Пусто)`
Открывает файл и возвращает файловый объект.

###### `Знак_в_код(c)`
Возвращает многобайтовый код символа `c`.

###### `Степень(основание, показатель, модуль = Пусто)`
Возводит число в степень с возможностью указать модуль (`a ** b % m`).

###### `Вывести(*объекты, разделитель = ' ', в_конце = '\n', файл = Пусто, немедленно = Нет)`
Выводит значения на экран или в файл, с настройкой форматирования.

###### `[@]Свойство(ф_получения = Пусто, ф_установки = Пусто, ф_удаления = Пусто, документация = Пусто)`
Создаёт объект свойства. Может использоваться как обёртка (декоратор).

###### `Ряд(длина | нач, кон, шаг = 1)`
Создаёт диапазон целых чисел.

###### `Представление(объект)`
Возвращает строковое представление объекта.

###### `Обратить(последовательность)`
Возвращает обратный перебиратель (итератор).

###### `Округлить(число, разрядов = Пусто)`
Округляет число до ближайшего значения с возможностью указать число знаков.

###### `Множ([перебираемое])`
Создаёт множество (уникальные элементы без порядка).

###### `Установить_поле(объект, название, значение)`
Устанавливает значение атрибута по названию.

###### `Срез(длина | нач, кон, шаг = 1)`
Создаёт срез для применения к последовательностям.

###### `Упорядочить(перебираемое, ф_сравнения, наоборот)`
Возвращает отсортованный список. Возможно сортование по ключу и в обратном порядке.

###### `[@]Статический_метод(функция)`
Обёртка, превращающая функцию в статический метод класса.

###### `Строка(объект[, кодование = 'utf-8', при_ошибках = 'strict')`
Преобразует объект в строку. Если объект байтовый — оборачивает его.

###### `Сумма(перебираемое[, начало = 0])`
Возвращает сумму элементов. Можно указать начальное значение.

###### `Надкласс([тип, порядок_поиска = Пусто])`
Возвращает объект, предоставляющий доступ к родительскому классу.

###### `Кортеж([перебираемое])`
Создаёт кортеж (неизменяемую последовательность) из перебираемого объекта или пустой.

###### `Тип(объект | название, надклассы, поля, **ключевые_слова)`
Возвращает тип объекта или создаёт новый.

###### `Поля([объект])`
Возвращает словарь атрибутов объекта.

###### `Упаковать(*перебираемые, проверить_длины = Нет)`
Объединяет элементы из нескольких источников.

###### `Свёртка(функция, перебираемое, нач_знач = Пусто)`
Пошагово сворачивает элементы, применяя функцию: ((a, b) -> c).

###### `@Метод_получения`
Обёртка получения значения для свойства.

###### `@Метод_установки`
Обёртка установки значения для свойства.

###### `@Метод_удаления`
Обёртка удаления значения для свойства.

###### `__Подключить__(название, общие_сущности = Пусто, местные_сущности = Пусто, по_списку = 0, уровень = 0)`
Внутренняя функция импорта.

---

### Встроенные методы и свойства

##### Строки (`Строка`)
Методы:

- `Найти(подстрока)`
- `Найти_с_конца(подстрока)`
- `Положение(подстрока)`
- `Положение_с_конца(подстрока)`
- `Заменить(старое, новое)`
- `Разбить(разделитель)`
- `Сцепить(список_строк)`
- `В_заглавные()`
- `В_строчные()`
- `Из_заглавных()`
- `Из_строчных()`
- `Из_цифр()`
- `Из_букв()`
- `Из_цифробукв()`
- `Из_пробелов()`
- `Слова_с_заглавных()`
- `Начинается(подстрока)`
- `Кончается(подстрока)`
- `Начать_с_заглавной()`
- `Отцентровать(ширина)`
- `Число_вхождений(подстрока)`
- `Табуляции_в_пробелы()`
- `Удалить_в_начале()`
- `Удалить_в_конце()`
- `Удалить_по_бокам()`
- `Разбить()` / `Разбить_с_конца()`
- `Обратить_регистр()`
- `Начать_слова_с_заглавных()`
- `Дополнить_нулями(ширина)`
- `Дополнить_справа(ширина)`
- `Дополнить_слева(ширина)`
- `Формат(...)` *(через ключевые аргументы)*

##### Списки (`Список`)
Методы:

- `Добавить(значение)`
- `Очистить()`
- `Копия()`
- `Число_вхождений(значение)`
- `Дополнить(последовательность)`
- `Положение(значение)`
- `Вставить(позиция, значение)`
- `Вытащить([позиция])`
- `Удалить(значение)`
- `Обратить()`
- `Упорядочить(ключ = ..., обратно = Да|Нет)`

---

##### Словари (`Словарь`)
Методы:

- `Очистить()`
- `Копия()`
- `Из_ключей(ключи[, значение])`
- `Получить(ключ[, по_умолчанию])`
- `Элементы()` — пары `(ключ, значение)`
- `Ключи()` — список ключей
- `Значения()` — список значений
- `Вытащить(ключ[, по_умолчанию])`
- `Вытащить_последнее()`
- `Получить_или_добавить(ключ[, значение])`
- `Обновить(другой_словарь)`

##### Кортежи (`Кортеж`)
Методы:

- `Положение(значение)`
- `Число_вхождений(значение)`

##### Множества (`Множ`, `НеизмМнож`)
Методы:

- `Не_пересекаются(другое)`
- `Подмножество(другое)`
- `Надмножество(другое)`
- `Объединение(...)`
- `Пересечение(...)`
- `Разница(...)`
- `СимметрРазница(...)`
- `Копия()`

Дополнительно для `Множ`:

- `Дополнить(...)`
- `Пересечь(...)`
- `Вычесть(...)`
- `СимметрВычесть(...)`
- `Добавить(значение)`
- `Удалить(значение)`
- `Убрать(значение)`
- `Вытащить()`
- `Очистить()`

##### Целые числа (`Цел`)
Методы:

- `Длина_в_битах()`
- `В_байты(длина, порядок = 'МлСт'|'СтМл', со_знаком = Да|Нет)`
- `Из_байтов(байты, порядок = 'МлСт'|'СтМл', со_знаком = Да|Нет)`

Свойства:

- `числитель`
- `знаменатель`

##### Вещественные (`Вещ`)
Методы:

- `Целое()` — возвращает `Да`, если число целое
- `В_шестн()` / `Из_шестн(строка)`
- `В_дробь()` — возвращает `(числитель, знаменатель)`

##### Комплексные (`Компл`)
Методы:

- `Cопряжённое()`

Свойства:

- `действ_часть`
- `мнимая_часть`

##### Потоки
Методы:

- `Читать([размер])`
- `Читать_строку()`
- `Писать(данные)`
- `Позиция()` / `Задать_позицию(позиция)`
- `Изменить_размер(размер)`
- `Отделить()` — для текстовых обёрток
- `Закрыть()`

Свойства:

- `закрыт`
