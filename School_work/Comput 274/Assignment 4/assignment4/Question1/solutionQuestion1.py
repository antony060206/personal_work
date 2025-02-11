# Name: Antony Feng
# ccid: zfeng8
# studentId: 1802829
# operating system: windows 11
# python version: 3.12
from pandas import value_counts


def analyze_character_frequencies(text):

    dictionary = {}

    sentence_list = text.lower().split() # add text into dictionary based on restrictions
    for word in sentence_list:
        for char in word:
            if char.isalpha():
                dictionary[char] = 1 + dictionary.get(char, 0)

    keys_list = list(dictionary.keys())

    #First bubble sort to sort the values of the keys
    for n in range(len(keys_list)):
        swapped = False

        for x in range(0, len(keys_list)-1-n):
            if dictionary.get(keys_list[x]) < dictionary.get(keys_list[x+1]):
                keys_list[x], keys_list[x+1] = keys_list[x+1], keys_list[x]  # Swap
                swapped = True
        if not swapped:
            break

    # Second sort to sort the keys by alphabetic order
    #this is done by counting how many (sorted) letters have the same frequency, sort them in a different list
    #then add them back to the original key_list
    repeated_keyslist = []
    count = 0
    for n in range(len(keys_list)-1):

        if dictionary.get(keys_list[n]) == dictionary.get(keys_list[n+1]):
            repeated_keyslist.append(keys_list[n])
            count += 1

        elif dictionary.get(keys_list[n]) != dictionary.get(keys_list[n+1]) and len(repeated_keyslist) != 0:
            repeated_keyslist.append(keys_list[n])
            repeated_keyslist.sort()
            keys_list[n-count:n+1] = repeated_keyslist
            count= 0
            repeated_keyslist.clear()

    if len(repeated_keyslist) != 0:
        repeated_keyslist.append(keys_list[-1])
        repeated_keyslist.sort()
        keys_list[n - count+1:n + 2] = repeated_keyslist


    return keys_list

def main():
    text = input()
    print(analyze_character_frequencies(text))

if __name__ == "__main__":
    main()