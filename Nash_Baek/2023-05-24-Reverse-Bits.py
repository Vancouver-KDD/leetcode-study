# https://peterdrinker.tistory.com/504

class ReverseBits:
    def reverse_bits(self, number: int) -> int:
        result = []
        # while number:
        for _ in range(32):
            result.append(number & 1)
            number >>= 1

        # comprehension expression
        # [expression for element in iterable if condition]

        # generator
        # (expression for element in iterable if condition)

        reversed_number = ''.join(str(element) for element in result)
        return int(reversed_number, 2)


def main():
    reverse_bits = ReverseBits()
    print(reverse_bits.reverse_bits(43261596))

if __name__ == '__main__':
    main()