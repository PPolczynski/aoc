from d01.historian_hysteria import HistorianHysteria

if __name__ == '__main__':
    list_a = []
    list_b = []
    split_characters = "   "
    with open("data", "r") as data_file:
        for line in data_file:
            values = line.rstrip().split(split_characters)
            list_a.append(int(values[0]))
            list_b.append(int(values[1]))
    if len(list_a) == len(list_b):
        historian_hysteria = HistorianHysteria(list_a, list_b)
        print("What is the total distance between your lists?")
        print(historian_hysteria.get_list_distance())
        print("What is their similarity score?")
        print(historian_hysteria.get_list_similarity())
