import random

def load_data(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def generate_plot():
    genres = load_data("data/genres.txt")
    names = load_data("data/names.txt")
    events = load_data("data/events.txt")

    genre = random.choice(genres)
    protagonist = random.choice(names)
    antagonist = random.choice(names)
    main_event = random.choice(events)

    story = f"""
    Genre: {genre}

    Protagonist: {protagonist}
    Antagonist: {antagonist}

    Story:
    {protagonist} is struggling against {antagonist} when suddenly, {main_event} happens.
    """
    return story

def save_to_file(content, file_name="generated_story.txt"):
    with open(file_name, "w") as file:
        file.write(content)
    print(f"Story saved to file: {file_name}")

def main():
    story = generate_plot()
    print(story)
    save_to_file(story)

if __name__ == "__main__":
    main()
