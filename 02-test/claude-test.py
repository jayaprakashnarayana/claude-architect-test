import os 
import anthropic 
from dotenv import load_dotenv 
load_dotenv()

model="claude-sonnet-4-6"

def add_user_message(messages, text):
    user_message = { "role": "user", "content": text}
    message.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "contennt": text}
    messages.append(assistant_message)


def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=500,
        messages=messages,
    )
    return message.content[0].text


client = anthropic.Anthropic()


message = client.messages.create(
    model=model,
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": " How to get job at Anthropic ? Answer perfectly I worked as solutions architect before for a decade now I am building AI",
        }
    ]
)

print (message.content[0].text)


messages = []

add_user_message(message, "Define quantum computing in simple terms")

answer = chat(messages)

add_assistant_message(messages, answer)

add_user_message(messages, "Write another sentence")

final_answer = chat(message)
