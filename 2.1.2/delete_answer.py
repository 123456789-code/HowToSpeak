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
    file = ".\\wordlist"
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




size = (545, 410)

main_window = QMainWindow()
main_window.resize(size[0], size[1])
main_window.move((1920 - size[0]) / 2, (1080 - size[1]) / 2)
main_window.setWindowTitle('Delete an answer')

word_input = QTextBrowser(main_window)
word_input.append("word_input:")
word_input.move(20, 20)
word_input.resize(250, 30)

input_word = QPlainTextEdit(main_window)
input_word.setPlaceholderText("btw")
input_word.move(275, 20)
input_word.resize(250, 30)

complete_word_input = QTextBrowser(main_window)
complete_word_input.append("complete_word_input:")
complete_word_input.move(20, 60)
complete_word_input.resize(250, 30)

input_complete_word = QPlainTextEdit(main_window)
input_complete_word.setPlaceholderText("by the way")
input_complete_word.move(275, 60)
input_complete_word.resize(250, 30)

add_button = QPushButton(main_window)
add_button.setText("Delete")
add_button.move(20, 100)
add_button.resize(100, 30)

tips = QTextBrowser(main_window)
tips.move(20, 140)
tips.resize(500, 250)


def search(word, complete_word):
    for i in range(n):
        if word_list[i][0] == word and word_list[i][1] == complete_word:
            return True
    return False


# delete answer
def delete():
    word = input_word.toPlainText()
    word.strip()
    complete_word = input_complete_word.toPlainText()
    complete_word.strip()

    if search(word, complete_word):
        global n, word_list

        word_list_ = []
        # refresh wordlist
        with open(file=file, mode="w", encoding="utf-8") as f:
            f.write(str(n-1) + "\n")
            for i in range(n):
                if (word, complete_word) != word_list[i]:
                    f.write(word_list[i][0] + "\n")
                    f.write(word_list[i][1] + "\n")
                    word_list_.append(word_list[i])
            f.close()
        word_list = word_list_
        n -= 1
        tips.append(word + " " * (4 - len(word) + 20) + complete_word)
    else:
        tips.append("There hasn't been such an answer.")


add_button.clicked.connect(delete)


tips.append("word" + " "*20 + "complete word")



file_window.show()

app.exec_()
