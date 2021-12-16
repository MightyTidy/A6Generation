import requests

import random


def main():
    print("Hello world")
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    first500 = response.content.splitlines()
    random.shuffle(first500)
    randint = 100
    j = 0
    print("\nArray at place 0 is ", first500[0])
    for z in range(0, len(first500)):
        first500[z] = str(first500[z])
        first500[z] = first500[z][2:-1]
    print("\nArray at place 0 is ", first500[0])
    for i in range(0, 50):
        tempString = "testfilezzthousand" + str(i) + ".txt"
        print("\nString was : ", tempString, "\n")
        j = 0
        with open("D:\\Users\\MightyTidy\\CLionProjects\\VazquezA6Real\\VazquezA6\\cmake-build-debug\\" + tempString, 'w') as file:
            while j < 1000:
                print("\nJ is : ", j, "\n")
                chanceInt = random.randint(1, 100)
                if chanceInt < 25:
                    file.write(str(first500[j]))
                    file.write(" ")
                    file.write(str(first500[j]))
                    file.write(" ")
                    j = j + 2
                else:
                    file.write(str(first500[j]))
                    file.write(" ")
                    j += 1
            file.close()
            print("\nFile num " + str(i) + " has been made")
            randint = 1000  # the number of random words in a file
            random.shuffle(first500)


main()
