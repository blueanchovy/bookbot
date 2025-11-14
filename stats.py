
def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        return num_words

def get_char_occurence(filepath, include_whitespace=True):
    counts = {}
    with open(filepath, encoding="utf-8-sig") as f:
        file_contents = f.read()

    for ch in file_contents:
            if not include_whitespace and ch.isspace():
                 continue
            ch = ch.lower()
            counts[ch] = counts.get(ch, 0) + 1   
    return counts

def get_sorted_dicts(dict):
    dict_list = []
    for pair in dict:
        dict_list.append({"char": pair, "num": dict[pair]})
    dict_list.sort(key=lambda x: x["num"], reverse=True)
    return dict_list