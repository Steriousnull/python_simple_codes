import openai

# Insert your API key here
openai.api_key = 'your-api-key-here'

messages = [{"role": "system", "content": "You are an intelligent assistant."}]

try:
    while True:
        message = input("User: ")
        if message:
            # Append user input to messages
            messages.append({"role": "user", "content": message})

            # Make API call
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )

            # Get reply from OpenAI
            reply = chat.choices[0].message['content']
            print(f"ChatGPT: {reply}")

            # Append assistant's reply to messages
            messages.append({"role": "assistant", "content": reply})
except KeyboardInterrupt:
    print("\nExiting chat.")
