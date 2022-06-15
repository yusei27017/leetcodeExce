func evalRPN(tokens []string) int {
	var tokenStack []int
	var num int
	var res int
	for _, token := range tokens {
		if token == "+" || token == "-" || token == "*" || token == "/" {
			switch token {
			case "+":
				res = tokenStack[len(tokenStack)-2] + tokenStack[len(tokenStack)-1]

			case "-":
				res = tokenStack[len(tokenStack)-2] - tokenStack[len(tokenStack)-1]

			case "*":
				res = tokenStack[len(tokenStack)-2] * tokenStack[len(tokenStack)-1]

			case "/":
				res = tokenStack[len(tokenStack)-2] / tokenStack[len(tokenStack)-1]

			}
			tokenStack = tokenStack[:len(tokenStack)-2]
			tokenStack = append(tokenStack, res)
		} else {
			num, _ = strconv.Atoi(token)
			tokenStack = append(tokenStack, num)
		}
	}
	return tokenStack[0]
}
