def main():
    case_count = int(input())
    for _ in range(case_count):
        a, b = map(int, input().split())
        print(a + b)


if __name__ == "__main__":
    main()
