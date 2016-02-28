# 17.15 Longest Word


def longest_word(words): # O(N)
    candidates = []
    memo = {}
    for word in words:
        # print("--- WORD: ", word)
        subwords = sub_words(word, memo)
        for subword in subwords:
            if subword in words:
                candidates.append(word)
                break  # escape this for-loop
    # return longest candidate word
    return longest_candidate(candidates)


def sub_words(word, memo): # O(N^2)
    # print(word)
    if memo.get(word) is not None:
        # print("Used memo for word:", word)
        return memo.get(word)
    if len(word) <= 1:
        return []
    subwords = []
    init_word = word[1:]
    tail_word = word[:-1]
    subwords.append(init_word)
    subwords.append(tail_word)
    #if init_word not in words:
        #words.append(init_word)
    sub_problem_init_result = sub_words(init_word, memo)
    subwords.extend(sub_problem_init_result)
    #if tail_word not in words:
        #words.append(tail_word)
    sub_problem_tail_result = sub_words(tail_word, memo)
    subwords.extend(sub_problem_tail_result)
    subwords = list(set(subwords))
    memo.update({word: subwords})
    return subwords


def longest_candidate(candidates): # O(N)
    longest_word_so_far = ""
    for candidate in candidates:
        if len(candidate) > len(longest_word_so_far):
            longest_word_so_far = candidate
    return longest_word_so_far


# print(sub_words("cat", {}))

input_words = ["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]
print(input_words)
result = longest_word(input_words)
print("Answer:", result)
