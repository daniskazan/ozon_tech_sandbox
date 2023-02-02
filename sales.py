from collections import Counter
from collections import namedtuple
from typing import List

TestCase = namedtuple("TestCase", ["number_of_purchased_items", "prices"])


def prepare_tests() -> List[TestCase]:
    tests = []
    cases_amount = int(input())
    for _ in range(cases_amount):
        number_of_purchased_items = int(input())
        prices = [int(price) for price in input().split(maxsplit=number_of_purchased_items + 1)]
        test_case = TestCase(number_of_purchased_items, prices)
        tests.append(test_case)
    return tests


def main():
    tests = prepare_tests()
    for t in tests:
        c = Counter(t.prices)  # считаем количество купленных товаров

        total = 0
        for price, product_amount in c.items():
            discount_part = (product_amount // 3) * 2 * price
            rest_part = (product_amount % 3) * price
            total += discount_part + rest_part
        print(total)


if __name__ == "__main__":
    main()
