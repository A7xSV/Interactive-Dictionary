import json
from difflib import get_close_matches

data = json.load(open('dictionary_data.json'))

def define(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        # Case to handle acronyms
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        # Prompt the closest match if it exists
        prompt = raw_input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        prompt = prompt.lower()
        if prompt == 'y' or prompt == 'yes':
            return data[get_close_matches(w, data.keys())[0]]
        elif prompt == 'n' or prompt == 'no':
            return "The word doesn't exist. Please double check it."
        else:
            return "Incorrect option"
    else:
        return "The word doesn't exist. Please double check it."

word = raw_input("Enter word: ")
output = define(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
