from PyQt5.QtWidgets import QMessageBox

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