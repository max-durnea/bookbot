
def count_words(text):
    words=text.split()
    return len(words)

def read_file(file_name):
    with open(file_name) as f:
            file_contents = f.read()
    return file_contents

def count_characters(text):
    lowered_text=text.lower()
    characters_dict={}
    for char in lowered_text:
        if(not char.isalpha()):
            continue
        if(char not in characters_dict):
            characters_dict.update({char:1})
        else:
            characters_dict[char]+=1
    sum=0
    for char in characters_dict:
        sum+=characters_dict[char]
    characters_dict=sorted(characters_dict.items(),key=lambda x:x[1],reverse=True)
    return sum, characters_dict


def main():
    file_path="books/frankenstein.txt"
    book_name="Frankenstein"
    print(f"--- Begin report of {file_path} ---\n")
    try:
        file_contents=read_file(file_path)
        word_count=count_words(file_contents)
        char_count,characters_dict=count_characters(file_contents)
        
        print(f"Title: {book_name}\n")
        print(f"The book contains {word_count} words")
        print(f"The book contains {char_count} characters\n")
        for char,count in characters_dict:
            if(char == '\n'):
                print(f"The \\n was found  {count} times")
            else:
                print(f"The \'{char}\' was found {count} times")
        print("\n--- End Report ---")
    except FileNotFoundError as e:
        print("File is not found")
main()