import sys
from tkinter.ttk import Widget
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout,
                             QVBoxLayout,QLabel,QPushButton,QSpinBox,QLineEdit,QDoubleSpinBox,
                             QCheckBox,QComboBox,QListWidget)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Gas Mileage Calculator")

        # Main layout ####################
        main_layout = QHBoxLayout()

        # Left and right panes #############
        left_pane = QVBoxLayout()
        right_pane = QVBoxLayout()
        
        title_label = QLabel("Gas Mileage Calculator")
        
        # Set fonts #################
        h1_font = title_label.font()
        h1_font.setPointSize(30)
        title_label.setFont(h1_font)

        # Results label ###################
        results_label = QLabel("MPG")
        h2_font = results_label.font()
        h2_font.setPointSize(26)
        results_label.setFont(h2_font)

        
        # Add left pane widgets
        left_pane.addWidget(title_label)

        # Add right pane widgets
        right_pane.addWidget(results_label)

        # Add the two panes to the layout
        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)
                                 

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()