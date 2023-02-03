package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type TestCase struct {
	NumberOfPurchasedItems int
	Prices                 []int
}

func readLine(reader *bufio.Reader) (string, error) {
	input, _, err := reader.ReadLine()
	return string(input), err
}

func prepareTests() []TestCase {
	var tests []TestCase

	reader := bufio.NewReader(os.Stdin)
	casesAmount, _ := readLine(reader)
	casesAmountInt, _ := strconv.Atoi(casesAmount)
	for i := 0; i < casesAmountInt; i++ {
		numberOfPurchasedItems, _ := readLine(reader)
		numberOfPurchasedItemsInt, _ := strconv.Atoi(numberOfPurchasedItems)

		pricesStr, _ := readLine(reader)
		prices := make([]int, numberOfPurchasedItemsInt)
		for j, p := range strings.Split(pricesStr, " ") {
			prices[j], _ = strconv.Atoi(p)
		}

		testCase := TestCase{
			NumberOfPurchasedItems: numberOfPurchasedItemsInt,
			Prices:                 prices,
		}
		tests = append(tests, testCase)
	}

	return tests
}


func calculateDiscount(prices []int) {

	total := 0
	priceCounts := make(map[int]int)
	for _, price := range prices {
		priceCounts[price]++
	}
	for price, productAmount := range priceCounts {
		discount := (productAmount / 3) * 2 * price
		rest := (productAmount % 3) * price
		total = discount + rest
	}
	fmt.Println(total)
}


func main() {
	tests := prepareTests()
	for _, t := range tests {
		calculateDiscount(t.Prices)
	}
}
