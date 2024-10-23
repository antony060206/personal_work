# Name: Antony Feng
# ccid: zfeng8
# studentId: 1802829
# operating system: windows 10
# python version: 3.12

#Input: The given input string
#Output: The "clean" version of the input string without characters specified in the problem statement like ?, !, etc
def clean_input_string(inputString):
    remove = [".", ",", "!","?", "'"]

    for x in remove:
        if inputString.find(x) != -1:
            inputString = inputString.replace(x, '')

    return inputString


#Input: The output from clean_input_string()
#Output: The reversed version of the input string
def reverse_string(cleanInputString):
    s = cleanInputString.split()[::-1]
    l = []
    for i in s:
        l.append(i)
    reversed_string = " ".join(l)
    return reversed_string


#Input: The output from reverse_string()
#Output: A string with all the duplicate occurrences of words removed. Only the first occurrence will remain in the string
def remove_duplicates(reversedString):
    duplicateremoved = ' '.join(dict.fromkeys(reversedString.split()))
    return duplicateremoved


#Input: The output from remove_duplicates()
#Output: The median length of the words in the input string. This function must return an integer, more specifically the floor value.
def calculate_median_length(reversedStringWithoutDuplicates):
    medianword = sorted(list(reversedStringWithoutDuplicates.split()), key=len)

    median = 0
    middle = len(medianword)//2

    if len(medianword) % 2 == 0:
        median = (len(medianword[middle-1]) + len(medianword[middle]))//2
    else:
        median = len(medianword[middle])
    return median

def main():
    inputString = input()

    cleanInputString = clean_input_string(inputString)

    reversedString = reverse_string(cleanInputString)
    print(reversedString)
    
    reversedStringWithoutDuplicates = remove_duplicates(reversedString)
    print(reversedStringWithoutDuplicates)
    
    medianWordLength = calculate_median_length(reversedStringWithoutDuplicates)
    print(medianWordLength)

    
if __name__ == "__main__":
    main()

