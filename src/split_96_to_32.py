import argparse

# Определение 32-битной маски и максимальных значений для разных битовых диапазонов
MASK_32BIT = 0xFFFFFFFF
MAX_128BIT = (1 << 128) - 1
MAX_96BIT = (1 << 96) - 1
MAX_64BIT = (1 << 64) - 1
MAX_32BIT = (1 << 32) - 1

def split_96_to_32(num):
    # Проверка, чтобы число не превышало 128 бит
    if num > MAX_128BIT:
        raise ValueError("Число больше 128 бит")

    # Разбивка числа на 32-битные блоки
    low = num & MASK_32BIT
    mid = (num >> 32) & MASK_32BIT
    high = (num >> 64) & MASK_32BIT
    fourth = (num >> 96) & MASK_32BIT

    return fourth, high, mid, low

def main():
    # Инициализация парсера аргументов
    parser = argparse.ArgumentParser(description="Разбить 96-битное число на три 32-битных числа.")
    parser.add_argument("num", type=int, help="96-битное число в десятичном представлении")
    args = parser.parse_args()

    try:
        # Вызов функции для разбивки числа и получение результатов
        fourth, high, mid, low = split_96_to_32(args.num)

        # Вывод информации
        print("96-битное число: {}".format(args.num))
        print("\nРазбитие на 32-битные блоки:")
        print("Младшие 32 бита: {}".format(low))
        print("Средние 32 бита: {}".format(mid))
        print("Старшие 32 бита: {}".format(high))
        print("Четвёртые 32 бита: {}".format(fourth))

        print("\nВ шестнадцатеричном представлении:")
        print("Младшие 32 бита в hex: {}".format(hex(low).upper().replace('X', 'x')))
        print("Средние 32 бита в hex: {}".format(hex(mid).upper().replace('X', 'x')))
        print("Старшие 32 бита в hex: {}".format(hex(high).upper().replace('X', 'x')))
        print("Четвёртые 32 бита в hex: {}".format(hex(fourth).upper().replace('X', 'x')))

        max_values = [MAX_32BIT, MAX_64BIT, MAX_96BIT, MAX_128BIT]
        blocks_needed = 0

        for i, max_value in enumerate(max_values):
            if args.num <= max_value:
                blocks_needed = i + 1
                break

        print(f"\nЧисло вмещается в {blocks_needed} блок(а) по 32 бита.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
