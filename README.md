# s21_decimal_python_util

## split_96_to_32

### Пример: 79228162514264337593543950330
- Сonsole
```bash
python3 split_96_to_32.py 79228162514264337593543950330
```
- Result
```bash
96-битное число: 79228162514264337593543950330

Разбитие на 32-битные блоки:
Младшие 32 бита: 4294967290
Средние 32 бита: 4294967295
Старшие 32 бита: 4294967295
Четвёртые 32 бита: 0

В шестнадцатеричном представлении:
Младшие 32 бита в hex: 0xFFFFFFFA
Средние 32 бита в hex: 0xFFFFFFFF
Старшие 32 бита в hex: 0xFFFFFFFF
Четвёртые 32 бита в hex: 0x0

Число вмещается в 3 блок(а) по 32 бита.
```

### Пример: 79228162514264337593543950335
- Сonsole
```bash
python3 split_96_to_32.py 79228162514264337593543950335
```
- Result
```bash
96-битное число: 79228162514264337593543950335

Разбитие на 32-битные блоки:
Младшие 32 бита: 4294967295
Средние 32 бита: 4294967295
Старшие 32 бита: 4294967295
Четвёртые 32 бита: 0

В шестнадцатеричном представлении:
Младшие 32 бита в hex: 0xFFFFFFFF
Средние 32 бита в hex: 0xFFFFFFFF
Старшие 32 бита в hex: 0xFFFFFFFF
Четвёртые 32 бита в hex: 0x0

Число вмещается в 3 блок(а) по 32 бита.
```

### Пример: 79228162514264337593543950335534534
- Сonsole
```bash
python3 split_96_to_32.py 79228162514264337593543950335534534
```
- Result
```bash
96-битное число: 79228162514264337593543950335534534

Разбитие на 32-битные блоки:
Младшие 32 бита: 4294501830
Средние 32 бита: 4294967295
Старшие 32 бита: 4294967295
Четвёртые 32 бита: 999999

В шестнадцатеричном представлении:
Младшие 32 бита в hex: 0xFFF8E5C6
Средние 32 бита в hex: 0xFFFFFFFF
Старшие 32 бита в hex: 0xFFFFFFFF
Четвёртые 32 бита в hex: 0xF423F

Число вмещается в 4 блок(а) по 32 бита.
```