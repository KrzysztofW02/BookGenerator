from PyQt5.QtWidgets import (
    QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit,
    QTextEdit, QSpinBox, QListWidget, QWidget
)

def setup_ui(widget):
    layout = QVBoxLayout()

    widget.genre_label = QLabel("Choose a Genre:")
    widget.genre_combo = QComboBox()
    layout.addWidget(widget.genre_label)
    layout.addWidget(widget.genre_combo)

    widget.name_label = QLabel("Protagonist's Name:")
    widget.name_input = QLineEdit()
    widget.random_name_button = QPushButton("Random Name")
    name_layout = QHBoxLayout()
    name_layout.addWidget(widget.name_input)
    name_layout.addWidget(widget.random_name_button)
    layout.addWidget(widget.name_label)
    layout.addLayout(name_layout)

    widget.antagonist_label = QLabel("Antagonist's Name:")
    widget.antagonist_input = QLineEdit()
    widget.random_antagonist_button = QPushButton("Random Antagonist")
    antagonist_layout = QHBoxLayout()
    antagonist_layout.addWidget(widget.antagonist_input)
    antagonist_layout.addWidget(widget.random_antagonist_button)
    layout.addWidget(widget.antagonist_label)
    layout.addLayout(antagonist_layout)

    widget.chapters_label = QLabel("Number of Chapters:")
    widget.chapters_spin = QSpinBox()
    widget.chapters_spin.setRange(1, 50)
    widget.chapters_spin.setValue(5)
    layout.addWidget(widget.chapters_label)
    layout.addWidget(widget.chapters_spin)

    widget.subplots_label = QLabel("Select Subplots:")
    widget.subplots_list = QListWidget()
    widget.add_subplot_button = QPushButton("Add Subplot")
    widget.delete_subplot_button = QPushButton("Delete Subplot")
    subplot_layout = QHBoxLayout()
    subplot_layout.addWidget(widget.subplots_list)
    subplot_layout.addWidget(widget.add_subplot_button)
    subplot_layout.addWidget(widget.delete_subplot_button)
    layout.addWidget(widget.subplots_label)
    layout.addLayout(subplot_layout)

    widget.selected_subplots_text = QListWidget()
    widget.remove_subplot_button = QPushButton("Remove Selected Subplot")
    selected_subplots_layout = QVBoxLayout()
    selected_subplots_layout.addWidget(widget.selected_subplots_text)
    selected_subplots_layout.addWidget(widget.remove_subplot_button)
    layout.addLayout(selected_subplots_layout)

    widget.story_output = QTextEdit()
    widget.story_output.setReadOnly(True)
    layout.addWidget(widget.story_output)

    widget.generate_button = QPushButton("Generate Story")
    layout.addWidget(widget.generate_button)

    widget.save_txt_button = QPushButton("Save as TXT")
    widget.save_pdf_button = QPushButton("Save as PDF")
    save_layout = QHBoxLayout()
    save_layout.addWidget(widget.save_txt_button)
    save_layout.addWidget(widget.save_pdf_button)
    layout.addLayout(save_layout)

    return layout
