func reverseWords(s string) string {
    	var index int
	var words []string
	var ans string
	flag := false
	s += " "
	for k, v := range s {
		if !flag && v != 32 {
			index = k
			flag = true
		}
		if flag && v == 32 {
			word := s[index:k]
			words = append(words, word)
			flag = false
		}
	}

	for i := len(words) - 1; -1 < i; i-- {
		if i == 0 {
			ans += words[i]
		} else {
			ans += words[i] + " "
		}
	}
	return ans
}
