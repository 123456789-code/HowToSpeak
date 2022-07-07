# choose which file to load
mode = input("Where do you want to load the data from\n1.load from system\n2.load from a file\n")
if mode == "1":
    file = "./wordlist"
else:
    file = input("Please input your path:")

# load in data
print("loading")
with open(file=file, mode="r", encoding="utf-8") as f:
    n = int(f.readline())
    word_list = []
    for i in range(n):
        word = f.readline().strip()
        complete = f.readline().strip()
        word_list.append((word, complete))
    f.close()
print("over!\n")

# main
while True:
    # input what to search
    word = input("What do you want to search:")
    word.strip()

    # search in the data
    ans_lst = []
    for i in range(n):
        if word_list[i][0] == word:
            ans_lst.append(word_list[i][1])

    if len(ans_lst) != 0: # There are answers
        # answer
        print("You word is " + word + ".")
        print("Answer may be:")
        for i in range(len(ans_lst)):
            print(str(i+1) + "." + ans_lst[i])
        print("")
    else: # There's no answer
        print("There's no answer.")

    # choose if add an answer
    mode = input("Do you want to add an answer?[Y/N]")
    if mode == "Y":
        complete = input("The complete word is:")
        word_list.append((word, complete))
        n += 1

        # add the new answer
        with open("./wordlist", mode="w", encoding="utf-8") as f:
            f.write(str(n) + "\n")
            for i in range(n):
                f.write(word_list[i][0].strip() + "\n")
                f.write(word_list[i][1].strip() + "\n")
            f.close()

        print("Over!\n")
    else:
        print("Over!\n")

    # again?
    mode = input("Would you like to try again?[Y/N]")
    if mode != "Y":
        break


print("All over!")
