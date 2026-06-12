import os
import anthropic
from dotenv import load_dotenv
load_dotenv()
model="claude-sonnet-4-6"

client = anthropic.Anthropic()

system_prompt = "You are a Comedian with 30 yrs of laughing experience"

message = client.messages.create(
    model=model,
    max_tokens=1024,
    messages=[
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": "What is the best joke you have ?",
        }
    ]
)   

print (message.content[0].text)

