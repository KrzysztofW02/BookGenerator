from PyQt5.QtWidgets import (
    QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit,
    QTextEdit, QSpinBox, QListWidget, QCheckBox
)

def setup_ui(widget):
    layout = QVBoxLayout()

    widget.genre_label = QLabel("Choose a Genre:")
    widget.genre_combo = QComboBox()
    widget.genre_combo.addItems(widget.genres)
    layout.addWidget(widget.genre_label)
    layout.addWidget(widget.genre_combo)

    widget.name_label = QLabel("Protagonist's Name:")
    widget.name_input = QLineEdit()
    widget.random_name_button = QPushButton("Random Name")
    widget.random_name_button.clicked.connect(widget.set_random_name)
    name_layout = QHBoxLayout()
    name_layout.addWidget(widget.name_input)
    name_layout.addWidget(widget.random_name_button)
    layout.addWidget(widget.name_label)
    layout.addLayout(name_layout)

    widget.antagonist_label = QLabel("Antagonist's Name:")
    widget.antagonist_input = QLineEdit()
    widget.random_antagonist_button = QPushButton("Random Antagonist")
    widget.random_antagonist_button.clicked.connect(widget.set_random_antagonist)
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
    widget.subplots_list.addItems(widget.subplots)
    widget.add_subplot_button = QPushButton("Add Subplot")
    widget.add_subplot_button.clicked.connect(widget.add_subplot)

    widget.delete_subplot_button = QPushButton("Delete Subplot")
    widget.delete_subplot_button.clicked.connect(widget.delete_subplot)

    subplot_layout = QHBoxLayout()
    subplot_layout.addWidget(widget.subplots_list)
    subplot_layout.addWidget(widget.add_subplot_button)
    subplot_layout.addWidget(widget.delete_subplot_button)
    layout.addWidget(widget.subplots_label)
    layout.addLayout(subplot_layout)


    widget.selected_subplots_label = QLabel("Selected Subplots:")
    widget.selected_subplots_text = QListWidget()
    widget.remove_subplot_button = QPushButton("Remove Subplot")
    widget.remove_subplot_button.clicked.connect(widget.remove_selected_subplot)
    selected_layout = QHBoxLayout()
    selected_layout.addWidget(widget.selected_subplots_text)
    selected_layout.addWidget(widget.remove_subplot_button)
    layout.addWidget(widget.selected_subplots_label)
    layout.addLayout(selected_layout)

    widget.customization_label = QLabel("Customize Story Elements:")
    layout.addWidget(widget.customization_label)

    widget.add_subplot_label = QLabel("Add New Subplot:")
    widget.add_subplot_input = QLineEdit()
    widget.add_subplot_button_custom = QPushButton("Add New Subplot")
    widget.add_subplot_button_custom.clicked.connect(widget.add_subplot_custom)
    subplot_customization_layout = QHBoxLayout()
    subplot_customization_layout.addWidget(widget.add_subplot_input)
    subplot_customization_layout.addWidget(widget.add_subplot_button_custom)
    layout.addWidget(widget.add_subplot_label)
    layout.addLayout(subplot_customization_layout)

    widget.use_ai_checkbox = QCheckBox("Use AI for story generation")
    widget.use_ai_checkbox.setChecked(True) 
    layout.addWidget(widget.use_ai_checkbox)

    widget.generate_button = QPushButton("Generate Story")
    widget.generate_button.clicked.connect(widget.generate_story)
    layout.addWidget(widget.generate_button)

    widget.story_output = QTextEdit()
    widget.story_output.setReadOnly(True)
    layout.addWidget(widget.story_output)

    widget.word_count_label = QLabel("Word Count: 0")
    layout.addWidget(widget.word_count_label)

    widget.save_txt_button = QPushButton("Save as TXT")
    widget.save_pdf_button = QPushButton("Save as PDF")
    widget.save_txt_button.clicked.connect(widget.save_to_txt)
    widget.save_pdf_button.clicked.connect(widget.save_to_pdf)
    save_layout = QHBoxLayout()
    save_layout.addWidget(widget.save_txt_button)
    save_layout.addWidget(widget.save_pdf_button)
    layout.addLayout(save_layout)

    return layout
