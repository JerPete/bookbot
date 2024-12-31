def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = word_count(text)
    char_counts = char_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_of_words} words found in the document")
    # Convert the character counts dictionary to a list of dictionaries
    char_list = [{"char": key, "count": value} for key, value in char_counts.items()]
    
    # Sort the list of dictionaries by 'count' in descending order
    char_list.sort(key=lambda x: x["count"], reverse=True)
    
    # Print the sorted character list without the "char" and "count" labels
    for item in char_list:  # Iterate through the sorted list
        print(f"The '{item['char']}' character was found {item['count']} times") 

    print("--- End report ---")


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
        if char.isalpha():  
            if char in char_dic:
                char_dic[char] += 1  
            else:
                char_dic[char] = 1  
    return char_dic 





     
main()