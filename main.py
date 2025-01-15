import sys
import random
import qtvscodestyle as qtvsc
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from ui_elements import setup_ui
from story_generator import generate_story
from data_manager import load_data, save_data

class BookGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book Generator")
        self.setGeometry(100, 100, 1000, 900)

        self.genres = load_data("data/genres.txt")
        self.names = load_data("data/names.txt")
        self.events = load_data("data/events.txt")
        self.subplots = load_data("data/subplots.txt")

        self.story = ""
        self.selected_subplots = []

        self.layout = setup_ui(self)
        self.setLayout(self.layout)

        self.random_name_button.clicked.connect(self.set_random_name)
        self.random_antagonist_button.clicked.connect(self.set_random_antagonist)
        self.save_txt_button.clicked.connect(self.save_to_txt)
        self.save_pdf_button.clicked.connect(self.save_to_pdf)
        self.add_subplot_button.clicked.connect(self.add_subplot)
        self.delete_subplot_button.clicked.connect(self.delete_subplot)
        self.generate_button.clicked.connect(self.generate_story)
        self.remove_subplot_button.clicked.connect(self.remove_selected_subplot)

    def set_random_name(self):
        self.name_input.setText(random.choice(self.names))

    def set_random_antagonist(self):
        self.antagonist_input.setText(random.choice(self.names))

    def add_subplot(self):
        selected_item = self.subplots_list.currentItem()
        if selected_item:
            subplot = selected_item.text()
            if subplot and subplot not in self.selected_subplots:
                self.selected_subplots.append(subplot)
                self.selected_subplots_text.addItem(subplot)

    def delete_subplot(self):
        selected_item = self.subplots_list.currentItem()
        if selected_item:
            subplot = selected_item.text()
            if subplot in self.subplots:
                self.subplots.remove(subplot)
                save_data("data/subplots.txt", self.subplots)
                self.subplots_list.takeItem(self.subplots_list.row(selected_item))
                QMessageBox.information(self, "Success", f"Subplot '{subplot}' deleted!")

    def remove_selected_subplot(self):
        selected_item = self.selected_subplots_text.currentItem()
        if selected_item:
            subplot = selected_item.text()
            self.selected_subplots.remove(subplot)
            self.selected_subplots_text.takeItem(self.selected_subplots_text.row(selected_item))

    def count_words(self):
        return len(self.story.split())

    def update_word_count(self):
        word_count = self.count_words()
        self.word_count_label.setText(f"Word Count: {word_count}")

    def generate_story(self):
        genre = self.genre_combo.currentText()
        protagonist = self.name_input.text().strip()
        antagonist = self.antagonist_input.text().strip()

        try:
            self.story = generate_story(
                genre,
                protagonist,
                antagonist,
                self.chapters_spin.value(),
                self.selected_subplots,
                self.events
            )
            self.story_output.setText(self.story)
            self.update_word_count()
        except ValueError as e:
            QMessageBox.warning(self, "Validation Error", str(e))

    def save_to_txt(self):
        if not self.story:
            QMessageBox.warning(self, "Error", "No story to save!")
            return
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Story as TXT", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, "w") as file:
                file.write(self.story)
            QMessageBox.information(self, "Success", f"Story saved as {file_name}")

    def save_to_pdf(self):
        if not self.story:
            QMessageBox.warning(self, "Error", "No story to save!")
            return
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Story as PDF", "", "PDF Files (*.pdf)")
        if file_name:
            pdf = canvas.Canvas(file_name, pagesize=letter)
            pdf.setFont("Times-Roman", 12)
            y_position = 750
            for line in self.story.split("\n"):
                pdf.drawString(50, y_position, line)
                y_position -= 15
                if y_position < 50:
                    pdf.showPage()
                    pdf.setFont("Times-Roman", 12)
                    y_position = 750
            pdf.save()
            QMessageBox.information(self, "Success", f"Story saved as {file_name}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stylesheet = qtvsc.load_stylesheet(qtvsc.Theme.DARK_VS)
    custom_button_style = """
    QPushButton {
        background-color: #323232; 
        color: #FFF;  
        border: 1px solid #555; 
        border-radius: 10px;  
        padding: 5px;  
    }
    QPushButton:hover {
        background-color: #444; 
        color: #FFF;  
        border: 1px solid #666;  
    }
    QPushButton:pressed {
        background-color: #555;  
        color: #FFF; 
        border: 1px solid #777; 
    }
    """
    app.setStyleSheet(stylesheet + custom_button_style)
    window = BookGeneratorApp()
    window.show()
    sys.exit(app.exec_())
