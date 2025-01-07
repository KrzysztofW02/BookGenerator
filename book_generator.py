import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def load_data(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def get_user_choice(options, prompt, allow_done=False):
    while True:
        try:
            print(prompt)
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")
            if allow_done:
                print("Type 'done' to finish your selection.")

            user_input = input("Enter the number of your choice: ").strip().lower()

            # Check for 'done' input
            if allow_done and user_input == "done":
                return None  # Signal that the user is done selecting

            # Process numerical input
            choice = int(user_input) - 1
            if 0 <= choice < len(options):
                return options[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number or type 'done' if applicable.")

def generate_plot_with_chapters_and_subplots():
    genres = load_data("data/genres.txt")
    names = load_data("data/names.txt")
    events = load_data("data/events.txt")
    subplots = load_data("data/subplots.txt")

    genre = get_user_choice(genres, "Choose a genre:")

    protagonist_choice = input("Do you want to provide a name for the protagonist? (yes/no): ").strip().lower()
    if protagonist_choice == "yes":
        protagonist = input("Enter the protagonist's name: ").strip()
    else:
        protagonist = random.choice(names)

    antagonist = random.choice(names)

    while True:
        try:
            num_chapters = int(input("How many chapters should the story have? "))
            if num_chapters > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    story = f"""
    Genre: {genre}

    Protagonist: {protagonist}
    Antagonist: {antagonist}

    Story:
    """

    for chapter in range(1, num_chapters + 1):
        story += f"\nChapter {chapter}:\n"
        story += f"{protagonist} faces a new challenge:\n"

        while True:
            subplot = get_user_choice(subplots, "Select a subplot (or type 'done' to finish):", allow_done=True)
            if subplot is None:  # User typed 'done'
                break
            story += f"    - Subplot: {subplot}\n"

        event = random.choice(events)
        story += f"    - Main event: {event}\n"

    return story

def save_to_file(content, file_name="generated_story.txt"):
    with open(file_name, "w") as file:
        file.write(content)
    print(f"Story saved to file: {file_name}")

def save_to_pdf(content, file_name="generated_story.pdf"):
    pdf = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter
    pdf.setFont("Times-Roman", 12)
    y_position = height - 50
    for line in content.split("\n"):
        pdf.drawString(50, y_position, line)
        y_position -= 15
        if y_position < 50:
            pdf.showPage()
            pdf.setFont("Times-Roman", 12)
            y_position = height - 50
    pdf.save()
    print(f"Story saved as PDF: {file_name}")

def main():
    print("Welcome to the Interactive Story Generator with Chapters and Subplots!")
    story = generate_plot_with_chapters_and_subplots()
    print("\nGenerated Story:")
    print(story)

    while True:
        save_option = input("Do you want to save the story as (1) TXT, (2) PDF, or (3) Both? ").strip()
        if save_option in {"1", "2", "3"}:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    if save_option == "1":
        save_to_file(story)
    elif save_option == "2":
        save_to_pdf(story)
    elif save_option == "3":
        save_to_file(story)
        save_to_pdf(story)

if __name__ == "__main__":
    main()
