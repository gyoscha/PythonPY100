def func_(str_):
    list_words = str_.split()
    print(list_words)
    max_words = []
    max_len = max(len(value) for value in list_words)
    for value in list_words:
        if len(value) == max_len:
            max_words.append(value)
    return max_words


if __name__ == "__main__":
    # Write your solution here
    str_words = 'В случае, когда самых длинных""" слов может быть несколько, вернуть их списком'
    print(func_(str_words))
