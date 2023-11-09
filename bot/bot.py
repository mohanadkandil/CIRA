import openai
import os
import time
import sys
import threading


openai.api_key = os.getenv("OPENAI_API_KEY")


def chatbot():
    draw_logo()
    print("Start chatting with the bot (type 'options' for more commands)!")
    messages = [
        {"role": "system", "content": "You are a helpful assistant"}
    ]

    while True:
        message = input("User: ")

        if message.lower() == "options":
            print("\nType 'quit' to stop the chat.")
            print("Type 'restart' to restart the chat.")
            continue
        elif message.lower() == "quit":
            print("Goodbye!")
            break
        elif message.lower() == "restart":
            messages = [{"role": "system", "content": "You are a helpful assistant."}]
            print("\nChat restarted. How can I assist you today?")
            continue

        messages.append({"role": "user", "content": message})

        loading_thread_event = threading.Event()
        loading_thread = threading.Thread(target = loading_message, args = (loading_thread_event,))
        loading_thread.start()

        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
        )

        loading_thread_event.set()
        loading_thread.join()

        chat_message = response['choices'][0]['message']['content']
        print(f"Bot: {chat_message}")
        messages.append({"role": "assistant", "content": chat_message})


def draw_logo():
    logo = """
████████╗██╗   ██╗███╗   ███╗
╚══██╔══╝██║   ██║████╗ ████║
   ██║   ██║   ██║██╔████╔██║
   ██║   ██║   ██║██║╚██╔╝██║
   ██║   ╚██████╔╝██║ ╚═╝ ██║
   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
    """
    print(logo)


def loading_message(event):
    print("Thinking...", end="")
    sys.stdout.flush()
    while not event.is_set():
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print()


if __name__ == "__main__":
    chatbot()
