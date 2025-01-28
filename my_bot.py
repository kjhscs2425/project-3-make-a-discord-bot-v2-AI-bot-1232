"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "robot" in user_message:
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def should_i_respond(user_message, user_name):
    """
    Check if the message contains 'robot' as specified in the original template
    """
    if "robot" in user_message:
        return True
    else:
        return False

def respond(user_message, user_name):
    """Return appropriate response based on the message"""
    message = user_message.lower()
    
    if "hi" in message:
        return "Hi! My name is Billy. I'm a Discord bot. How can I help you today?"
        
    elif "temperature" in message:
        return "The temperature outside today is 72°F"
        
    elif "time" in message:
        return "The current time is 3:00 PM. Want to know anything else?"
        
    elif "favorite color" in message:
        return "Well, since I'm a bot, I don't really have a favorite color. But I think blue looks pretty cool! What's your favorite color?"
        
    elif "joke" in message:
        return "Sure! Why don't skeletons fight each other? They don't have the guts! 😂 Want to hear another?"
        
    elif "created" in message:
        return "I was created by some awesome developers! They designed me to make your Discord experience better. Want to know more about me?"
        
    elif "music" in message:
        return "Yep, I can play music! Just tell me what song you want, and I'll get it going for you."
        
    elif "how are you" in message:
        return f"I'm doing great, thanks for asking! How about you, {user_name}?"
        
    elif "reminder" in message:
        return "I can help with reminders! Just let me know what you want to be reminded of and when."
        
    elif "goodbye" in message or "bye" in message:
        return f"Goodbye {user_name}! Hope to chat with you again soon. Have a great day!"
        
    # Default response if no specific match is found
    return f"Hey {user_name}! How can I help you today?"