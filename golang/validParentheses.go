func isValid(s string) bool {
	var tokenStack []int32

	for _, token := range s {
		if token == 123 || token == 91 || token == 40 {
			tokenStack = append(tokenStack, token)
        } else if len(tokenStack) == 0 {
			return false
		} else {
			if tokenStack[len(tokenStack)-1] == 40 && token != 41 {
				return false
			}
			if tokenStack[len(tokenStack)-1] == 91 && token != 93 {
				return false
			}
			if tokenStack[len(tokenStack)-1] == 123 && token != 125 {
				return false
			}
			tokenStack = tokenStack[:len(tokenStack)-1]
		}
	}
	if len(tokenStack) == 0 {
		return true
	} else {
		return false
	}
}
