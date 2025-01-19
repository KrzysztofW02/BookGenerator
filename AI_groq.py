import os
from groq import Groq

def generate_story_with_groq(genre, protagonist, antagonist, num_chapters, selected_subplots, events):
    groq_api_key = os.environ.get('GROQ_API_KEY')
    if groq_api_key is None:
        raise KeyError("Environment variable 'GROQ_API_KEY' is not set.")
    
    client = Groq(api_key=groq_api_key)
    prompt = (
        f"Generate a story with the following details:\n"
        f"Genre: {genre}\n"
        f"Protagonist: {protagonist}\n"
        f"Antagonist: {antagonist}\n"
        f"Number of Chapters: {num_chapters}\n"
        f"Selected Subplots: {', '.join(selected_subplots)}\n"
        f"Events: {', '.join(events)}\n"
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"An error occurred during story generation: {e}")
