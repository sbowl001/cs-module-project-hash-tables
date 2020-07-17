def no_dups(s):
    # Your code here
    cache = {}
    formatted_string = [] 


    for word in s.split():
        if word not in cache:
            cache[word] = 1 
            formatted_string.append(word)
    return " ".join(formatted_string)
    



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))