def words_in_string(text):
    return len(text.split())

def num_of_chars_in_string(text):
    final_dict = {}
    for char in text:
        low = char.lower()
        if low in final_dict:
            final_dict[low] += 1
        else:
            final_dict[low] = 1
    return final_dict

def sort_on(d):
    return d["num"]

def sort_list(letter_count_dict):
    sorted_list = []
    for ch in letter_count_dict:
        sorted_list.append({"char": ch, "num": letter_count_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on) 
    return sorted_list
    