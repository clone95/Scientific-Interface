from Functions import *

vect = [1, 4, 12]


def common_stats(values):
    print("Average:  ", (average(values)))
    print("Median: ", median(values))
    print("Trend:  ", trend(values))
    print("Standard Deviation:  ", std_deviation(values))


menu = "Welcome to your scientific utility tool:\n" \
       "Which operation do you need?\n\n" \
       "a.   I want to get common statistical values of my vector\n" \
       "b.   Convert values counting occurences, from file to output file\n" \
       "c.   I want to predict object velocity\n"


def main():
    choice = input(menu)
    if choice == "a":
        choice_1 = input("Do you want to manually upload values or read from file?\n file / man\n")
        if choice_1 == "man":
            print("Insert value then press enter, press 'end' to end the vector\n")
            value = 0
            man_vect = []
            vect = []
            while value != "end":
                value = input()
                man_vect.append(value)
            man_vect.remove("end")
            for el in range(0, len(man_vect)):
                vect.append(float(man_vect[el]))
            common_stats(vect)
        else:
            file_location = input("Specify file location: the file has to be like this:\n\n"
                                  "1 5 22 5.6 ......... 9.54\n")
            file = open(file_location, "r")
            file_vect = file.read().split()
            vals =[]
            for el in range(0, len(file_vect)):
                vals.append(float(file_vect[el]))
            common_stats(vals)
    elif choice == "b":
        file_to_clean = input("Insert absolute file path.")
        data_cleaner(file_to_clean)

    # other options


main()

