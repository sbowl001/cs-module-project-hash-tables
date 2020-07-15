

cache = {}

def word_count(s):
    # Your code here

 
    lowercased_words = s.lower()

    
    for words in lowercased_words.split():
        print(words)
        if words.isalpha:
            if words not in cache: 
                cache[words] = 1
            else: 
                cache[words] += 1

    # for character in s: 
    #     if character.isalpha():
    #         for words in lowercased_words.split():
    #             print(words)
    #             if words not in cache: 
    #                 cache[words] = 1
    #             else: 
    #                 cache[words] += 1
    return cache 

        


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))