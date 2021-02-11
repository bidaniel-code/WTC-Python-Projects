
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters: " ,;?."
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    split_str = (list(filter(lambda x : len(x) > 0, split(' ,;?.', text.lower()))))
    return split_str
    #print(split_str)


def words_longer_than(length, text):
    words = (list(filter(lambda x : len(x) > length, split(' ,;?.', text.lower()))))
    return words
    #print(words)


def words_lengths_map(text):
    words = [len(item) for item in sorted (list(filter(lambda x: len(x) > 0, split(' ,;?.', text.lower()))))]
    length_counter = {item: words.count(item) for item in words}
    return length_counter
    #print(length_counter)
    

def letters_count_map(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_list = "".join(list(filter(lambda x : len(x) > 0, split(' ,;?.', text.lower()))))
    letter_counter = {item: new_list.count(item) for item in alphabet if item in alphabet}
    return letter_counter
    #print(letter_counter)


def most_used_character(text):
    new_list = "".join(list(filter(lambda x : len(x) > 0, split(' ,;?.', text.lower()))))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_counter = {item: new_list.count(item) for item in alphabet if item in alphabet}
    m = max(letter_counter.values())
    max_val = [x for x in letter_counter if letter_counter[x] == m]
    max_val = str(max_val[0])
    if text == '':
        return None 
    else:
        return max_val
    
    
    #return max_val
    #popular_char = reduce(lambda a,b: a if a > b)



if __name__ == '__main__':
    text = 'These are indeed interesting, an obvious understatement, times. What say you?'
    length = 10
    #convert_to_word_list(text)
    #words_longer_than(length, text)
    #words_lengths_map(text)
    #letters_count_map(text)
    print(most_used_character(text))