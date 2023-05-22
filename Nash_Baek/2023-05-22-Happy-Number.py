# https://peterdrinker.tistory.com/497

class HappyNumber:
    def is_happy_number(self, number: int) -> bool:
        seen = set()
        while number != 1:
            digits = str(number)
            number = sum(int(digit) ** 2 for digit in digits)

            if number in seen:
                return False
            seen.add(number)
        return True

happy_number = HappyNumber()
print(happy_number.is_happy_number(19))