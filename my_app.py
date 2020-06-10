import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        answer = input("Did you mean %s instead? Write [y/n]\n" % get_close_matches(word, data.keys())[0])
        answer = answer.lower()
        if answer == "y" or answer == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif answer == "n" or answer == "no":
            return "The word doesn't exist. Please double check it."
        else:
            return "Sorry, I didn't understand your entry, try again!"

    else:
        print("The word doesn't exist. Please double check it.")


user_input = input("Enter word: ")

output = translate(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
