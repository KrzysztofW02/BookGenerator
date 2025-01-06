import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def load_data(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def get_user_choice(options, prompt):
    while True:
        try:
            print(prompt)
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")
            choice = int(input("Enter the number of your choice: ")) - 1
            if 0 <= choice < len(options):
                return options[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def generate_plot():
    genres = load_data("data/genres.txt")
    names = load_data("data/names.txt")
    events = load_data("data/events.txt")

    genre = get_user_choice(genres, "Choose a genre:")

    protagonist_choice = input("Do you want to provide a name for the protagonist? (yes/no): ").strip().lower()
    if protagonist_choice == "yes":
        protagonist = input("Enter the protagonist's name: ").strip()
    else:
        protagonist = random.choice(names)

    antagonist = random.choice(names)

    while True:
        try:
            num_events = int(input("How many events should happen in the story? "))
            if num_events > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    story_events = [random.choice(events) for _ in range(num_events)]

    story = f"""
    Genre: {genre}

    Protagonist: {protagonist}
    Antagonist: {antagonist}

    Story:
    {protagonist} is struggling against {antagonist}. Here's what happens:
    """
    for i, event in enumerate(story_events, start=1):
        story += f"\n    {i}. {event}"

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
    print("Welcome to the Interactive Story Generator!")
    story = generate_plot()
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
