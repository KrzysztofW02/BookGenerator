import random

def generate_story(genre, protagonist, antagonist, num_chapters, selected_subplots, events):
    if not protagonist or not antagonist:
        raise ValueError("Protagonist and Antagonist names cannot be empty.")
    
    story = f"Genre: {genre}\n\nProtagonist: {protagonist}\nAntagonist: {antagonist}\n\nStory:\n"
    story += "Introduction:\n"
    story += f"{protagonist} begins their journey in a world defined by {genre}.\n"
    
    import random

    story = ""
    for chapter in range(1, num_chapters + 1):
        story += f"\nChapter {chapter}:\n"
        story += f"{protagonist} encounters new challenges and confronts {antagonist}.\n"
        subplot = random.choice(selected_subplots) if selected_subplots else None
        event = random.choice(events)
        
        if subplot: 
            story += f"{subplot}\n"
        
        story += f"{event}\n"

    
    story += "\nConclusion:\n"
    story += f"In the end, {protagonist} manages to confront their fears and achieve their goal.\n"
    return story
