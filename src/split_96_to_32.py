import argparse

MASK_32BIT = 0xFFFFFFFF  # 32-битная маска

def split_96_to_32(num):
    """
    Разбивает 96-битное число на три 32-битных числа.
    :param num: 96-битное число
    :return: кортеж из трех 32-битных чисел (high, mid, low)
    """
    if num >= (1 << 96):
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
        print("Старшие 32 бита: {}".format(high))
        print("Средние 32 бита: {}".format(mid))
        print("Младшие 32 бита: {}".format(low))
        print("hex")
        print("Старшие 32 бита: {}".format(hex(high)))
        print("Средние 32 бита: {}".format(hex(mid)))
        print("Младшие 32 бита: {}".format(hex(low)))

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
