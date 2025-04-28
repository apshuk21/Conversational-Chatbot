from mem0 import Memory
from config import config
from open_ai_client import client as client_open_ai
from system_prompt import getSystemPrompt

mem_client = Memory.from_config(config)
user_id="p123"

def chat(message: str):
    # search memory for the given user query
    mem_search_result = mem_client.search(query=message, user_id=user_id)

    memories = "\n".join([mem_search.get('memory') for mem_search in mem_search_result.get('results')])
    
    # Create system prompt based on memories
    SYSTEM_PROMPT = getSystemPrompt(memories)

    # Add system prompt to the messages
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": message }
    ]

    # Get response from the Open AI
    response = client_open_ai.responses.create(
        model="gpt-4.1",
        input=messages
    )

    response_output = response.output

    for output in response_output:
        role = output.role
        response_message = output.content[0].text

        # Print the response message to the user
        print(f"{role.upper()}: {response_message}")

        # Add the Open AI response to the messages
        messages.append(
            { "role": role, "content": response_message }
        )

    mem_client.add(messages, user_id=user_id)

    return messages

while True:
    user_message = input(">>: ")
    messages = chat(user_message) 