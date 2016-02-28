
def lcs(x, y):
    # print("x, y", x, y)
    if len(x) == 0 or len(y) == 0: # i.e. if either is empty
        # print("One string is empty")
        return ""
    last_character_in_x = x[len(x) - 1]
    last_character_in_y = y[len(y) - 1]
    sub_problem_x = x[0:len(x) - 1]
    sub_problem_y = y[0:len(y) - 1]
    if last_character_in_x == last_character_in_y: # ie. they end in the same character
        # print("End in same character", last_character_in_x)
        return lcs(sub_problem_x, sub_problem_y) + last_character_in_x
    else:
        first_possibility = lcs(sub_problem_x, y)
        second_possibility = lcs(x, sub_problem_y)
        if len(first_possibility) > len(second_possibility): #return the longest of the two
            return first_possibility
        else:
            return second_possibility


my_x = "BANANA"
my_y = "ATANA"
print("first string", my_x)
print("second string", my_y)
longest_common_subsequence = lcs(my_x, my_y)
print("Longest Common Subsequence", longest_common_subsequence)
