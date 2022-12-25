from checkbox import run_checkbox
from listofmocktails import Mocktails
import operator

def main():
    youringredients = run_checkbox()
    dict = {}
    for mocktail in Mocktails:
        print(mocktail[1])
        difference = len(set(mocktail[1]) - set(youringredients))
        print(difference)
        dict.update({mocktail[0]: difference})

    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
    print(sorted_dict)

main()