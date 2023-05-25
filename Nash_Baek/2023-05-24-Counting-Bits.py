# https://peterdrinker.tistory.com/503

class CountingBits:
    
    # Not used for this problem
    def convert_dec_to_bin(self, number: int) -> list[int]:
        result = []
        while number:
            result.append(number & 1)
            number >>= 1
        return result[::-1]
    
    def count_number_of_1bits(self, number: int) -> int:
        count = 0
        while number:
            count += number & 1
            number >>= 1
        return count
    
    def count_bits(self, number) -> list[int]:
        result = list(map(self.count_number_of_1bits, range(number + 1)))
        return result


def main():
    counting_bits = CountingBits()
    print(counting_bits.count_bits(2))
    print(counting_bits.count_bits(5))


if __name__ == '__main__':
    main()