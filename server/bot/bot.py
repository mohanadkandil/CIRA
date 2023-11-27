import os
import openai
import random
from scipy.io.wavfile import write
import pyttsx3
from dotenv import load_dotenv
import speech_recognition as sr
from time import sleep
import sys
import threading

# Set your OpenAI API key here
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Adjectives and nouns for random names
adjectives = ["beautiful", "sad", "mystical", "serene", "whispering", "gentle", "melancholic"]
nouns = ["sea", "love", "dreams", "song", "rain", "sunrise", "silence", "echo"]

# Initialize pyttsx for text-to-speech output
engine = pyttsx3.init('dummy')
engine.setProperty('rate', 130)
print(engine)


def generate_random_name():
    # Generate random unique names for the audio voice recordings
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"


def new_record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording... Please speak into the microphone.")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results; {e}"


def trranscribe_audio(audio_path):
    # Transcribe the audio file using OpenAI's Whisper API
    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript['text']


def speech_to_text(response):
    # Convert the text response to speech
    engine.say(response)
    engine.runAndWait()


def chat_mode():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Exiting chat mode.")
            break

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        response = completion.choices[0].message["content"]
        print("Assistant:", response)


def thinking_message(event):
    print("Thinking...", end="")
    sys.stdout.flush()
    while not event.is_set():
        sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print()  # Move to the next line


def main():
    mode = input("Choose mode (speech/chat): ").lower()
    if mode == 'speech':
        while True:
             
            print("Speak now...")
            transcript = new_record_audio()
            print("Transcript:", transcript)

            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": transcript}
            ]

            # Starpyt the thinking message in a separate thread
            done = threading.Event()
            thinking_thread = threading.Thread(target=thinking_message, args=(done,))
            thinking_thread.start()

            # Get the response from OpenAI's API
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # Stop the thinking message
            done.set()
            thinking_thread.join()
            response = completion.choices[0].message["content"]
            speech_to_text(response)
            print("Assistant:", response)
            speech_to_text(response)

            user_choice = input("Continue? (y/n): ")
            if user_choice.lower() != "y":
                print("Glad to help. Goodbye!")
                break

    elif mode == 'chat':
        chat_mode()
    else:
        print("Invalid mode selected. Exiting.")

if __name__ == "__main__":
    main()

