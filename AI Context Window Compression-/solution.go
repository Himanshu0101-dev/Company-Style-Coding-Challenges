package main

import "fmt"

func maxImportance(tokens []int, importance []int, K int) int {
	n := len(tokens)

	dp := make([]int, K+1)

	for i := 0; i < n; i++ {
		for j := K; j >= tokens[i]; j-- {
			candidate := dp[j-tokens[i]] + importance[i]
			if candidate > dp[j] {
				dp[j] = candidate
			}
		}
	}

	return dp[K]
}

func main() {
	tokens := []int{50, 40, 60, 30}
	importance := []int{100, 60, 120, 50}
	K := 100

	fmt.Println(maxImportance(tokens, importance, K))
}
