import os
import anthropic
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()
model = "claude-haiku-4-5-20251001"

messages = []

while True:
    user_input = input("> ")
    print("> ", user_input)

    messages.append({"role": "user", "content": user_input})
    message = client.messages.create(
        model=model,
        max_tokens=500,
        messages=messages,
    )
    assistant_response = message.content[0].text
    print ("> ", assistant_response)
    messages.append({"role": "assistant", "content": assistant_response})
    print ("> ", messages)

    