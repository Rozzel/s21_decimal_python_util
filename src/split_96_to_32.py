import argparse

MASK_32BIT = 0xFFFFFFFF  # 32-битная маска
MAX_96BIT = (1 << 96) - 1  # Максимальное 96-битное число

def split_96_to_32(num):
    if num > MAX_96BIT:
        raise ValueError("Число больше 96 бит")

    low = num & MASK_32BIT
    mid = (num >> 32) & MASK_32BIT
    high = (num >> 64) & MASK_32BIT

    return high, mid, low

def main():
    parser = argparse.ArgumentParser(description="Разбить 96-битное число на три 32-битных числа.")
    parser.add_argument("num", type=int, help="96-битное число в десятичном представлении")

    args = parser.parse_args()

    try:
        high, mid, low = split_96_to_32(args.num)

        print("96-битное число: {}".format(args.num))

        print("\nРазбитие на 32-битные блоки:")
        print("Младшие 32 бита: {}".format(low))
        print("Средние 32 бита: {}".format(mid))
        print("Старшие 32 бита: {}".format(high))

        print("\nВ шестнадцатеричном представлении:")
        print("Младшие 32 бита в hex: {}".format(hex(low)))
        print("Средние 32 бита в hex: {}".format(hex(mid)))
        print("Старшие 32 бита в hex: {}".format(hex(high)))

        if args.num == MAX_96BIT:
            print("\nЧисло ровно вмещается в 3 блока по 32 бита.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
