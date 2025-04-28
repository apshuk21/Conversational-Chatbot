from open_ai_client import client as client_open_ai

messages = []

def chat(message: str):
    messages.append(
        {"role": "user", "content": message }
    )

    response = client_open_ai.responses.create(
        model="gpt-4.1",
        input=messages
    )

    response_output = response.output

    for output in response_output:
        role = output.role
        response_message = output.content[0].text
        print(response_message)
        messages.append(
            { "role": role, "content": response_message }
        )
    return messages


while True:
    user_message = input(">>: ")
    messages = chat(user_message) 
