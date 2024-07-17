from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import randint

app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("Random number")
main_window.resize(500, 300)



instruction_label = QLabel("Натисніть щоб обрати переможця!")

random_number = QLabel("?")

generate_button = QPushButton("Згенерувати")

def generate():
    instruction_label.setText("Преможець:")
    random_number.setText(str(randint(1,100)))

generate_button.clicked.connect(generate)
    

main_layuot = QVBoxLayout()
main_layuot.addWidget(instruction_label)
main_layuot.addWidget(random_number)
main_layuot.addWidget(generate_button)



main_window.setLayout(main_layuot)
main_window.show()
app.exec()