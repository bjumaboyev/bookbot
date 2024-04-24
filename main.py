def read_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    d = {}
    
    for i in text:
        low = i.lower()
        if low not in d:
            d[low] = 1
        else:
            d[low] += 1
    return d

def sort_on(d):
    return d["num"]

def sort_dict(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    num_words = word_count(text)
    char_dict = count_letters(text)
    sorted_list = sort_dict(char_dict)
    
    print("--- Begin report of books/frankstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    for i in sorted_list:
        if not i['char'].isalpha(): continue
        print(f"The '{i['char']}' character was found {i["num"]} times")
    
    print("--- End report ---")

main() 