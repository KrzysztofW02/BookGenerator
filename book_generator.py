import sys
import random
import qtvscodestyle as qtvsc
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QComboBox, QLineEdit, QTextEdit, QSpinBox, QFileDialog, QMessageBox, QListWidget
)
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        QMessageBox.critical(None, "Error", f"File not found: {file_path}")
        return []
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An error occurred: {e}")
        return []

def save_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write('\n'.join(data))
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An error occurred while saving: {e}")

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

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.genre_label = QLabel("Choose a Genre:")
        self.genre_combo = QComboBox()
        self.genre_combo.addItems(self.genres)
        layout.addWidget(self.genre_label)
        layout.addWidget(self.genre_combo)

        self.name_label = QLabel("Protagonist's Name:")
        self.name_input = QLineEdit()
        self.random_name_button = QPushButton("Random Name")
        self.random_name_button.clicked.connect(self.set_random_name)
        name_layout = QHBoxLayout()
        name_layout.addWidget(self.name_input)
        name_layout.addWidget(self.random_name_button)
        layout.addWidget(self.name_label)
        layout.addLayout(name_layout)

        self.antagonist_label = QLabel("Antagonist's Name:")
        self.antagonist_input = QLineEdit()
        self.random_antagonist_button = QPushButton("Random Antagonist")
        self.random_antagonist_button.clicked.connect(self.set_random_antagonist)
        antagonist_layout = QHBoxLayout()
        antagonist_layout.addWidget(self.antagonist_input)
        antagonist_layout.addWidget(self.random_antagonist_button)
        layout.addWidget(self.antagonist_label)
        layout.addLayout(antagonist_layout)

        self.chapters_label = QLabel("Number of Chapters:")
        self.chapters_spin = QSpinBox()
        self.chapters_spin.setRange(1, 50)
        self.chapters_spin.setValue(5)
        layout.addWidget(self.chapters_label)
        layout.addWidget(self.chapters_spin)

        self.subplots_label = QLabel("Select Subplots:")
        self.subplots_list = QListWidget()
        self.subplots_list.addItems(self.subplots)
        self.add_subplot_button = QPushButton("Add Subplot")
        self.add_subplot_button.clicked.connect(self.add_subplot)

        self.delete_subplot_button = QPushButton("Delete Subplot")
        self.delete_subplot_button.clicked.connect(self.delete_subplot)

        subplot_layout = QHBoxLayout()
        subplot_layout.addWidget(self.subplots_list)
        subplot_layout.addWidget(self.add_subplot_button)
        subplot_layout.addWidget(self.delete_subplot_button)
        layout.addWidget(self.subplots_label)
        layout.addLayout(subplot_layout)

        self.selected_subplots_label = QLabel("Selected Subplots:")
        self.selected_subplots_text = QListWidget()
        self.remove_subplot_button = QPushButton("Remove Subplot")
        self.remove_subplot_button.clicked.connect(self.remove_selected_subplot)
        selected_layout = QHBoxLayout()
        selected_layout.addWidget(self.selected_subplots_text)
        selected_layout.addWidget(self.remove_subplot_button)
        layout.addWidget(self.selected_subplots_label)
        layout.addLayout(selected_layout)

        self.customization_label = QLabel("Customize Story Elements:")
        layout.addWidget(self.customization_label)

        self.add_subplot_label = QLabel("Add New Subplot:")
        self.add_subplot_input = QLineEdit()
        self.add_subplot_button_custom = QPushButton("Add New Subplot")
        self.add_subplot_button_custom.clicked.connect(self.add_subplot_custom)
        subplot_customization_layout = QHBoxLayout()
        subplot_customization_layout.addWidget(self.add_subplot_input)
        subplot_customization_layout.addWidget(self.add_subplot_button_custom)
        layout.addWidget(self.add_subplot_label)
        layout.addLayout(subplot_customization_layout)

        self.generate_button = QPushButton("Generate Story")
        self.generate_button.clicked.connect(self.generate_story)
        layout.addWidget(self.generate_button)

        self.story_output = QTextEdit()
        self.story_output.setReadOnly(True)
        layout.addWidget(self.story_output)

        self.word_count_label = QLabel("Word Count: 0")
        layout.addWidget(self.word_count_label)

        self.save_txt_button = QPushButton("Save as TXT")
        self.save_pdf_button = QPushButton("Save as PDF")
        self.save_txt_button.clicked.connect(self.save_to_txt)
        self.save_pdf_button.clicked.connect(self.save_to_pdf)
        save_layout = QHBoxLayout()
        save_layout.addWidget(self.save_txt_button)
        save_layout.addWidget(self.save_pdf_button)
        layout.addLayout(save_layout)

        self.setLayout(layout)

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

    def remove_selected_subplot(self):
        selected_item = self.selected_subplots_text.currentItem()
        if selected_item:
            subplot = selected_item.text()
            self.selected_subplots.remove(subplot)
            self.selected_subplots_text.takeItem(self.selected_subplots_text.row(selected_item))

    def add_subplot_custom(self):
        new_subplot = self.add_subplot_input.text().strip()
        if new_subplot and new_subplot not in self.subplots:
            self.subplots.append(new_subplot)
            save_data("data/subplots.txt", self.subplots)
            self.subplots_list.addItem(new_subplot)
            QMessageBox.information(self, "Success", f"Subplot '{new_subplot}' added!")
            self.add_subplot_input.clear()
    
    def delete_subplot(self):
        selected_item = self.subplots_list.currentItem()
        if selected_item:
            subplot = selected_item.text()
            if subplot in self.subplots:
                self.subplots.remove(subplot)
                save_data("data/subplots.txt", self.subplots)
                self.subplots_list.takeItem(self.subplots_list.row(selected_item))
                QMessageBox.information(self, "Success", f"Subplot '{subplot}' deleted!")

    def count_words(self):
        return len(self.story.split())

    def update_word_count(self):
        word_count = self.count_words()
        self.word_count_label.setText(f"Word Count: {word_count}")

    def generate_story(self):
        genre = self.genre_combo.currentText()
        protagonist = self.name_input.text().strip()
        antagonist = self.antagonist_input.text().strip()
        if not genre:
            QMessageBox.warning(self, "Validation Error", "Please choose a genre.")
            return
        if not self.selected_subplots:
            QMessageBox.warning(self, "Validation Error", "Please select at least one subplot.")
            return

        num_chapters = self.chapters_spin.value()

        self.story = f"Genre: {genre}\n\nProtagonist: {protagonist}\nAntagonist: {antagonist}\n\nStory:\n"
        for chapter in range(1, num_chapters + 1):
            self.story += f"\nChapter {chapter}:\n"
            self.story += f"{protagonist} faces a new challenge:\n"
            for subplot in self.selected_subplots:
                self.story += f"    - Subplot: {subplot}\n"
            event = random.choice(self.events)
            self.story += f"    - Main event: {event}\n"

        self.story_output.setText(self.story)
        self.update_word_count()

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
            width, height = letter
            pdf.setFont("Times-Roman", 12)
            y_position = height - 50
            for line in self.story.split("\n"):
                pdf.drawString(50, y_position, line)
                y_position -= 15
                if y_position < 50:
                    pdf.showPage()
                    pdf.setFont("Times-Roman", 12)
                    y_position = height - 50
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
