from collections import Counter


def main():
    case_count = int(input())
    for _ in range(case_count):
        amount = int(input())
        prices = [int(price) for price in input().split(maxsplit=amount)]
        c = Counter(prices)
        total = 0
        for price, product_amount in c.items():
            discount_part = (product_amount // 3) * 2 * price
            rest_part = (product_amount % 3) * price
            total += discount_part + rest_part
        print(total)


if __name__ == "__main__":
    main()
