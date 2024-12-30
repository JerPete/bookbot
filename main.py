def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = word_count(text)
    print(f"{num_of_words} words found in the document")
    print(char_count(text))
    

def word_count(text):
     words = text.split()
     return len(words)
     

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def char_count(text):
    char_dic = {}
    text = text.lower()
    for char in text:
        if char in char_dic:
            char_dic[char] +=1
        else:
            char_dic[char] = 1
    return char_dic



     
main()