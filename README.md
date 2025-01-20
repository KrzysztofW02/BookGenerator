# Book Generator App

Book Generator App is a PyQt5-based application for generating stories based on selected genres, protagonists, antagonists, subplots, and events. It also includes an optional AI-powered feature for enhanced story generation.

## Features

- **Random Name Generation**: Generate random names for protagonists and antagonists.
- **Custom Subplots**: Add and remove subplots to personalize your story.
- **Story Generation**: Create stories based on defined parameters with optional AI support.
- **Export to TXT and PDF**: Save stories in popular formats.
- **AI Integration**: Optional AI-powered story generation using Groq API.
  To use AI functions, you'll need to obtain a free API key from [https://console.groq.com/keys](https://console.groq.com/keys) and set it as the environment variable `GROQ_API_KEY`.

## System Requirements

- Python 3.8+
- PyQt5
- reportlab
- qtvscodestyle
- Groq API key (optional)

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/KrzysztofW02/BookGenerator.git
   ```
   Navigate to the project folder:  
   ```bash
   cd BookGenerator
   ```
   
2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Set the Groq API key if you want to use AI-powered features:  
   ```bash
   export GROQ_API_KEY=your_api_key_here
   ```

6. Run the application:  
   ```bash
   python main.py
   ```

## How to Use the Application

1. Select the story genre from the dropdown menu.
2. Enter names for the protagonist and antagonist or use the random generation button.
3. Choose the number of chapters.
4. Add subplots from the list or enter custom ones.
5. If you don't want to use AI, uncheck the "Use AI for story generation" option.
6. Click "Generate Story" to create the story.
7. Save your story as a TXT or PDF file.

## Project Structure

- `main.py` - Main application file.
- `story_generator.py` - Handles story generation logic.
- `data_manager.py` - Manages data input/output.
- `AI_groq.py` - Module for Groq AI integration.
- `ui_elements.py` - Handles user interface elements.
- `data` - Folder containing input data such as genres, names, and events.
