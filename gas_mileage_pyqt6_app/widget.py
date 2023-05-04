import sys
from tkinter.ttk import Widget
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout,
                             QVBoxLayout,QLabel,QPushButton,QSpinBox,)
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        main_layout = QHBoxLayout()

        left_pane = QVBoxLayout()
        
        # Add layouts and widgets to left pane
        hbox1 = QHBoxLayout()
        current_label = QLabel("Current Mileage")
        mileage_sb = QSpinBox()
        mileage_sb.setMinimum(0)
        mileage_sb.setSuffix("  Miles")
        hbox1.addWidget(current_label)
        hbox1.addWidget(mileage_sb)
        left_pane.addLayout(hbox1)

        main_layout.addLayout(left_pane)

        # Add previous mileage box
        right_pane = QVBoxLayout()
        hbox2 = QHBoxLayout()
        current_label = QLabel("Previous Mileage")
        prev_mileage_sb = QSpinBox()
        prev_mileage_sb.setMinimum(0)
        prev_mileage_sb.setSuffix("  Miles")
        hbox2.addWidget(current_label)
        hbox2.addWidget(prev_mileage_sb)
        hbox2.addWidget(current_label)
        right_pane.addLayout(hbox2)

        
        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)
        
        
        # Add gallons filled box
        hbox3 = QHBoxLayout()
        current_label = QLabel("Gallons Filled")
        gallons_sb = QSpinBox()
        gallons_sb.setMinimum(0)
        gallons_sb.setSuffix("  Gallons")
        hbox3.addWidget(current_label)
        hbox3.addWidget(gallons_sb)
        hbox3.addWidget(current_label)
        hbox3.addWidget(current_label)
        left_pane.addLayout(hbox3)

        
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()