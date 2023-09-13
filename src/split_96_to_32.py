import argparse

def split_96_to_32(num):
    low = num & 0xFFFFFFFF
    mid = (num >> 32) & 0xFFFFFFFF
    high = (num >> 64) & 0xFFFFFFFF

    return high, mid, low

def main():
    parser = argparse.ArgumentParser(description="Разбить 96-битное число на три 32-битных числа.")
    parser.add_argument("num", type=int, help="96-битное число в десятичном представлении")

    args = parser.parse_args()

    num_96bit = args.num

    high, mid, low = split_96_to_32(num_96bit)
    print("96-битное число: {}".format(num_96bit))
    print("Старшие 32 бита: {}".format(high))
    print("Средние 32 бита: {}".format(mid))
    print("Младшие 32 бита: {}".format(low))
    print("hex")
    print("Старшие 32 бита: {}".format(hex(high)))
    print("Средние 32 бита: {}".format(hex(mid)))
    print("Младшие 32 бита: {}".format(hex(low)))

if __name__ == "__main__":
    main()
