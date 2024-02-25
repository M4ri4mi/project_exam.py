import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt

# Importing the Calculator class from calculator_gui module
from calculator_gui import Calculator

# Create the QApplication instance
app = QApplication(sys.argv)

# Load the CSS stylesheet
with open('styles.css', 'r') as file:
    style_sheet = file.read()
    app.setStyleSheet(style_sheet)

# Main code
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exam System')
        self.setGeometry(100, 100, 600, 400)

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter) 

        # Create "Start an Exam" button
        self.start_exam_button = QPushButton('Start an Exam')
        self.start_exam_button.setObjectName('start-exam-button')  # Set the object name (ID)
        self.start_exam_button.clicked.connect(self.start_exam)

        self.layout.addWidget(self.start_exam_button)

        self.setLayout(self.layout)

    def start_exam(self):
        # Load questions from variables.json
        self.questions = self.load_questions('variables.json')
        self.current_question_index = 0
        self.score = 0
        self.display_question(self.questions[self.current_question_index])  # Display the first question

    def load_questions(self, file_path):
        # Function to load questions from JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get('questions', [])

    def display_question(self, question_data):
        # Function to display a question
        # Clear the layout before adding new widgets
        self.clear_layout()

        # Display the question
        self.question_label = QLabel(question_data['prompt'])
        self.question_label.setObjectName('question-label')  # Set the object name to match CSS ID

        self.layout.addWidget(self.question_label)

        # Add buttons for "Use Calculator" and "Answer the Question"
        use_calculator_button = QPushButton('Use Calculator')
        use_calculator_button.setObjectName('use-calculator-button')  # Setting the object name
        use_calculator_button.clicked.connect(self.use_calculator)
        self.layout.addWidget(use_calculator_button)

        answer_question_button = QPushButton('Answer the Question')
        answer_question_button.setObjectName('answer-question-button')
        answer_question_button.clicked.connect(self.answer_question)
        self.layout.addWidget(answer_question_button)

    def use_calculator(self):
        # Function to handle "Use Calculator" button click
        self.calculator = Calculator(self)
        self.calculator.exec_()

    def answer_question(self):
        # Function to handle "Answer the Question" button click
        # Clear the layout before adding new widgets
        self.clear_layout()

        # Display a line edit for the user's answer
        self.answer_line = QLineEdit()
        self.answer_line.setPlaceholderText('Type your answer here')
        self.answer_line.setObjectName('answer_line')

        # Connect the textChanged signal to the method for checking input
        self.answer_line.textChanged.connect(self.check_input)

        self.layout.addWidget(self.answer_line)

        # Add a button to submit the answer
        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.submit_answer)
        submit_button.setObjectName('submit_button')
        self.layout.addWidget(submit_button)

        # Add a button to return back to the question
        return_button = QPushButton('Return')
        return_button.clicked.connect(self.return_to_question)
        return_button.setObjectName('return_button')
        self.layout.addWidget(return_button)

    def check_input(self, text):
        # Function to check the input in the answer line edit
        # Check if the entered text contains only numbers
        if not text.isdigit():
            # Remove the last character if it's not a number
            self.answer_line.setText(text[:-1])

    def submit_answer(self):
        # Function to handle submitting the answer
        user_answer = self.answer_line.text().strip()

        if user_answer == "":
            QMessageBox.warning(self, "Warning", "Please enter a valid answer.")
            return

        correct_answer = str(self.questions[self.current_question_index]['answer'])
        
        if user_answer == correct_answer:
            result_message = 'Correct!'
            self.score += 1  # Increase score for correct answer
        else:
            result_message = 'Incorrect!'

        # Display result message directly on the main window
        result_label = QLabel(result_message)
        result_label.setObjectName("result-label")
        self.layout.addWidget(result_label)

        # Remove the answer line and submit button
        self.answer_line.deleteLater()
        self.sender().deleteLater()

        # Remove the return button
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QPushButton) and widget.text() == 'Return':
                widget.deleteLater()

        # Add a Next button or Finish button
        if self.current_question_index < len(self.questions) - 1:
            next_button = QPushButton('Next')
            next_button.clicked.connect(self.next_question)
            next_button.setObjectName('next_button')
            self.layout.addWidget(next_button)
        else:
            finish_button = QPushButton('Finish')
            finish_button.clicked.connect(self.finish_exam)
            finish_button.setObjectName('finish-button')
            self.layout.addWidget(finish_button)

    def next_question(self):
        # Function to move to the next question
        self.current_question_index += 1
        self.display_question(self.questions[self.current_question_index])

    def finish_exam(self):
        # Function to finish the exam and display results
        # Display results on the same page
        if self.score >= 3:
            result_message = 'Congratulations! You passed the exam.'
        else:
            result_message = 'You failed the exam.'
        result_label = QLabel(result_message)
        result_label.setObjectName("result-label")
        self.layout.addWidget(result_label)

        # Display the score
        score_label = QLabel(f'Your score is: {self.score}')
        score_label.setObjectName("score-label")  # Set object name
        self.layout.addWidget(score_label)
        
        # Remove the "Correct" and "Incorrect" labels
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QLabel) and (widget.text() == 'Correct!' or widget.text() == 'Incorrect!'):
                widget.setParent(None)

        # Remove the finish button
        self.sender().deleteLater()

    def return_to_question(self):
        # Function to return back to the question
        # Display the question again
        self.display_question(self.questions[self.current_question_index])

    def clear_layout(self):
        # Function to clear the layout
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

if __name__ == "__main__":
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())























