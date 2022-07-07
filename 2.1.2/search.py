from PySide2.QtWidgets import *

n = 0
word_list = []

app = QApplication([])

size = (480, 90)

file_window = QMainWindow()
file_window.resize(size[0], size[1])
file_window.move((1920 - size[0]) / 2, (1080 - size[1]) / 2)
file_window.setWindowTitle("load data")

load_from_system = QPushButton(file_window)
load_from_system.setText("load from system")
load_from_system.move(10, 10)
load_from_system.resize(150, 30)

load_from_file = QPushButton(file_window)
load_from_file.setText("load from file")
load_from_file.move(10, 50)
load_from_file.resize(150, 30)

load_file_location = QLineEdit(file_window)
load_file_location.move(170, 50)
load_file_location.resize(300, 30)
file = ""


def load_data():
    with open(file=file, mode="r", encoding="utf-8") as f:
        global n
        n = int(f.readline())
        for i in range(n):
            word = f.readline().strip()
            complete = f.readline().strip()
            word_list.append((word, complete))
        f.close()
    # print(word_list)

def system_load():
    global file
    file = '.\\wordlist'
    load_data()
    file_window.close()
    main_window.show()
load_from_system.clicked.connect(system_load)

def file_load():
    global file
    file = load_file_location.text().strip()
    load_data()
    file_window.close()
    main_window.show()
load_from_file.clicked.connect(file_load)

size = (545, 370)

main_window = QMainWindow()
main_window.resize(size[0], size[1])
main_window.move((1920 - size[0]) / 2, (1080 - size[1]) / 2)
main_window.setWindowTitle('How To Speak')

what_to_search = QTextBrowser(main_window)
what_to_search.append("What do you want to search:")
what_to_search.move(20, 20)
what_to_search.resize(250, 30)

input_word = QPlainTextEdit(main_window)
input_word.setPlaceholderText("btw")
input_word.move(275, 20)
input_word.resize(250, 30)

search_button = QPushButton(main_window)
search_button.setText("Search")
search_button.move(20, 60)
search_button.resize(100, 30)

answer = QTextBrowser(main_window)
answer.move(20, 100)
answer.resize(500, 250)


# search
def search():
    answer.clear()

    word = input_word.toPlainText()
    word.strip()

    # print(word_list)
    # print(word)

    # search in the data
    ans_lst = []
    # print(n)
    for i in range(n):
        # print(word_list[i][0] + " " + word)
        if word_list[i][0] == word:
            ans_lst.append(word_list[i][1])

    # print(ans_lst)
    if len(ans_lst) != 0:  # There are answers
        # answer
        answer.append("You word is " + word + ".")
        answer.append("Answer may be:")
        for i in range(len(ans_lst)):
            answer.append(str(i + 1) + "." + ans_lst[i])
    else:  # There's no answer
        answer.append("There's no answer.")

search_button.clicked.connect(search)


file_window.show()

app.exec_()
