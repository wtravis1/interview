######## Shortener

# Given two strings s, t, determine if string s can be changed into string t
# using the following rule:

# Remove any number of lowercase letters from s (or none at all),
# then capitalize all remaining letters of s.

# Example of the rule:
# s = AAbcD
# Possible outputs using the rule:
# Remove none, capitalize -> AABCD
# Remove c, capitalize -> AABD
# Remove b, capitalize -> AACD
# Remove b and c, capitalize -> AAD

# If it is possible to create the string t by processing s using the rule,
# then the function should return True, otherwise return False.

# Initial Thoughts
# If string t is longer than string s then false
# If string s contains a capital letter that t does not then false
# If string s does not contain a letter that t does then false
#
# to solve, progress through string t starting at the begging say t1 then
# iterate through s trying to find t1 if a capital letter is passed before
# finding t1 then return false, if t1 is found (lowercase or uppercase) continue
# with t2 the the end of s is reached at any point return false


def shortener(s, t):
    tIndex = 0
    for l in s:
        if (tIndex < len(t) and l.lower() == t[tIndex].lower()):
            tIndex += 1
        elif (l.isupper()):
            return False
    if (tIndex == len(t)):
        return True
    return False

    # for i_s in range(len(s)):
    #     found = False
    #     for i_t in range(i_t, len(s)):
    #         if (l.lower() == letter.lower()):
    #             found = True
    #             break
    #         elif (l.isupper()):
    #             return False
    #     if (found == False):
    #         return False


# Test Cases
test_cases = [
    ("daBccd", "ABC", True),
    ("sYOCaaaa", "YOCN", False),
    ("aaaaaa", "AAAAAAA", False),
    ("SVAHHHMVIIDYIcOSHMDUAVJRIBxBZQSUBIVEBHfVTZVSHATUYDJGDRRUBQFHEEEUZLQGXTNKFWUYBAeFKUHSFLZEUINBZYRIXOPYYXAEZZWELUPIEIWGZHEIYIROLQLAVHhMKRDSOQTJYYLTCTSIXIDAnPIHNXENWFFZFJASRZRDAPVYPAViVBLVGRHObnwlcyprcfhdpfjkyvgyzpovsgvlqbhtwrucvszaqinbgeafuswkjrcexvyzq","SVAHHHMVIIDYIOSHMDUAVJRIBBZQSUBIVEBHVTZVSHATUYDJGDRRUBQFHEEEUZLQGXTNKFWUYBAFKUHSFLZEUINBZYRIXOPYYXAEZZWELUPIEIWGZHEIYIROLQLAVHMKRDSOQTJYYLTCTSIXIDAPIHNXENWFFZFJASRZRDAPVYPAVVBLVGRHO", True),
    ("a", "AA", False),("UZJMUCYHpfeoqrqeodznwkxfqvzktyomkrVyzgtorqefcmffauqhufkpptaupcpxguscmsbvolhorxnjrheqhxlgukjmgncwyastmtgnwhrvvfgbhybeicaudklkyrwvghpxbtpyqioouttqqrdhbinvbywkjwjkdiynvultxxxmwxztglbqitxmcgiusfewmsvxchkryzxipbmgrnqhfmlghomfbsKjglimxuobomfwutwfcmklzcphbbfohnaxgbaqbgocghaaizyhlctupndmlhwwlxxvighhjjrctcjBvxtagxbhrbrWwsyiiyebdgyfrlztoycxpjcvmzdvfeYqaxitkfkkxwybydcwsbdiovrqwkwzbgammwslwmdesygopzndedsbdixvi","UZJMUCYH", False)
]

for case in test_cases:
    s, t, output = case
    print(shortener(s, t) == output)
