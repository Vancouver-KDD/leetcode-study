class OneBits:
    def hamming_weight(self, number: int) -> int:
        count = 0
        while number:
            count += number & 1
            number >>= 1
        return count

def main():
    one_bits = OneBits()
    print(one_bits.hamming_weight(5))

if __name__ == '__main__':
    main()