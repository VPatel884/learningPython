#  Problem 1

def welcome_message() :
    print("Welcome to Python Programming!")

welcome_message()

# Problem 2
# greeting("Vikash") // Function can not be called before defining it

def greeting(name) :
    print(f"Good Morning {name}!")

greeting("Vikash")
greeting("Vikram")

# Problem 3

def square(num) :
    return num ** 2

print(square(3))

# Problem 4

def convert_to_upper(word) :
    return word.upper()

print(convert_to_upper("apple"))

# Takes string as input and returns number vowels and consonants

def count_vow_Conso(str) :
    vowels = "aeiouAEIOU"

    countVow = 0
    countConso = 0

    for letter in str :
        if(letter.isalpha()) :
            if(letter in vowels) :
                countVow += 1
            else :
                countConso += 1

    return countVow, countConso

vowNum, consoNum = count_vow_Conso("Vikash Patel")
print(f"Number of vowels is {vowNum}")
print(f"Number of consonants is {consoNum}")
