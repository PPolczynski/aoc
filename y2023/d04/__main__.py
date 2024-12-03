from y2023.d04.scratchcards import Scratchcards

if __name__ == '__main__':
    scratchcards = []
    with open("data", "r") as data_file:
        for line in data_file:
            scratchcards.append(line.rstrip())
    print("How many points are they worth in total?")
    print(Scratchcards.get_scratchcards_score(scratchcards))
    print("how many total scratchcards do you end up with?")
    print(Scratchcards.get_scratchcards_count(scratchcards))