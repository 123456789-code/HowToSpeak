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

def delete():
        global n, word_list
        n -= 1

        word_list_ = []
        # refresh wordlist
        with open(file=file, mode="w", encoding="utf-8") as f:
            f.write(str(n) + "\n")
            for i in range(n):
                if (word, complete_word) != word_list[i]:
                    f.write(word_list[i][0] + "\n")
                    f.write(word_list[i][1] + "\n")
                    word_list_.append(word_list[i])
            f.close()
        word_list = word_list_
        tips.append(word + " " * (4 - len(word) + 20) + complete_word)
    else:
        tips.append("There hasn't been such an answer.")
def main():
    for i in range(n):
        for j in range(i, n):
            if word_list[i] == word_list[j]:



def system_load():
    global file
    file = ".\\wordlist"
    load_data()
    file_window.close()
    main()


load_from_system.clicked.connect(system_load)


def file_load():
    global file
    file = load_file_location.text().strip()
    load_data()
    file_window.close()
    main()


load_from_file.clicked.connect(file_load)

file_window.show()

app.exec_()
