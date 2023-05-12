import sys
from tkinter.ttk import Widget
from PyQt6.QtWidgets import ( QMainWindow, QApplication, QVBoxLayout, QHBoxLayout,
    QLabel, QCheckBox, QComboBox, QListWidget, QTextEdit,
    QSpinBox, QDoubleSpinBox, QSlider, QWidget, QPushButton,)
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
        self.results_title_label = QLabel()
        h2_font = self.results_title_label.font()
        h2_font.setPointSize(26)
        self.results_title_label.setFont(h2_font)

        self.results_label = QLabel("Enter distance and gallons filled")
        p_font = self.results_label.font()
        p_font.setPointSize(16)
        self.results_label.setFont(p_font)


        # Add left pane widgets
        self.distance_sb = QSpinBox()
        self.distance_sb.setMaximum(500)
        self.distance_sb.setSuffix(" Miles")
        self.gallons_sb = QSpinBox()
        self.gallons_sb.setSuffix(" Gallons")
        self.calculate_btn = QPushButton("Calculate")
        self.calculate_btn.clicked.connect(self.calculate)
       
        # Add left pane widgets
        left_pane.addWidget(title_label)
        left_pane.addWidget(self.distance_sb)
        left_pane.addWidget(self.gallons_sb)
        left_pane.addWidget(self.calculate_btn)


        # Add right pane widgets
        right_pane.addWidget(self.results_title_label)
        right_pane.addWidget(self.results_label)


        # Add the two panes to the layout
        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)


        # Set the main Layout
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)


    def calculate(self):
        message = ""
        distance = self.distance_sb.value()
        gallons = self.gallons_sb.value()
        
        try:
            results = distance / gallons
            message = f"MPG = {results}"
        except ZeroDivisionError:
            message = "You cannot divide by zero, \nplease enter a number in both boxes"
        
        self.results_label.setText(message)

        
                                 


app = QApplication(sys.argv)


window = MainWindow()
window.show()


app.exec()