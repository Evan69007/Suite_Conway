# def decoupeChaine(string):
# 	char = string[0]
# 	resultStr = "" + char
	
# 	for i in range(1, len(string)):
# 		if string[i] != char:
# 			resultStr += " "
# 			char = string[i]
# 		resultStr += string[i]
	
# 	return (resultStr)


# print(decoupeChaine("aabbbca"))

def decritChaine(string):
	resultStr = ""
	i = 0
	while i < len(string):
		char = string[i]
		nb_char = 1
		i += 1
		while(i < len(string) and string[i] == char):
			nb_char += 1
			i += 1
		resultStr += (str(nb_char) + char)
	return (resultStr)

# print(decritChaine("aaabbc"))


def suiteConway(char, n):
	if (n <= 0):
		return
	print(char)
	return (suiteConway(decritChaine(char), n - 1))

suiteConway('a', 7)