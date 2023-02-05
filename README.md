# Simple-Discord-SelfBot
This project was created with the intention of conducting testing and was inspired by Kunutza. It is a barebones structure, allowing you to perform basic actions such as reading, deleting, and sending messages. However, additional features can be easily added.

# What is this?
A Discord selfbot is a type of bot that is specifically designed to run on a single user account. These bots can automate various tasks and perform actions on behalf of the user, such as sending messages, reacting to messages, and managing user data. However, it's important to note that the use of selfbots goes against Discord's terms of service and can result in the user's account being banned.

# Examples
Sending a message:
```py
discord_client = Discord(token=auth_token, user_agent=random_user_agent)

response = discord_client.send_message(channel_id='channel_id', message='Hello World')

if response.status_code == 200:
    print("Message sent successfully")
else:
    print("Failed to send message")
```

Reading messages:
```py
discord_client = Discord(token=auth_token, user_agent=random_user_agent)

response = discord_client.read_messages(channel_id='channel_id')

if response.status_code == 200:
    messages = response.json()
    for message in messages:
        print(f"Message ID: {message['id']} - Message: {message['content']}")
else:
    print("Failed to retrieve messages")
```

Deleting a message:
```py
discord_client = Discord(token=auth_token, user_agent=random_user_agent)

response = discord_client.delete_message(channel_id='channel_id', message_id='message_id')

if response.status_code == 204:
    print("Message deleted successfully")
else:
    print("Failed to delete message")

```

# Terms of Use Disclaimer for Educational Project
This project is for educational purposes only and any use in violation of terms of service is the responsibility of the user.
