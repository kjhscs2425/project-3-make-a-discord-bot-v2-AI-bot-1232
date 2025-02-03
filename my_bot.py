"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
import random

def should_i_respond(user_message, user_name):\
   
    message = user_message.lower()
    
    trigger_phrases = [
        "hello bot",
        "robot",
        "game",
        "joke",
        "weather",
        "time",
    ]
    
    # Count vowels in the message
    vowel_count = sum(1 for char in message if char in 'aeiou')
    
    # Check for any trigger phrase
    for phrase in trigger_phrases:
        if phrase in message:
            return True
            
    # Return True if message has more than 5 vowels
    return vowel_count > 5

def respond(user_message, user_name):

    # Convert message to lowercase for matching
    message = user_message.lower()
    
    # Replace common abbreviations
    message = message.replace("u", "you")
    message = message.replace("r", "are")
    
    # Special greeting for messages starting with "hello"
    if message.startswith("hello") or message.startswith("hi"):
        return f"Hello {user_name.capitalize()}! How can I help you today?"
    
    # Random responses for different triggers
    if "joke" in message:
        jokes = [
            "Why don't programmers like nature? It has too many bugs!",
            "What do you call a bot that steals? A ROB-ot!",
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "Why don't skeletons fight each other? Because they don't have the guts.", 
            "How do get straight A's? By using a ruler"

        ]
        return random.choice(jokes)
    
    if "game" in message:
        games = ["Rock Paper Scissors", "Number Guessing", "Word Chain"]
        return f"I know several games! Let's play {random.choice(games)}!"
    
    if "quote" in message:
        quotes = [
            "Be the change you wish to see in the world.",
            "Code is poetry in motion.",
            "Keep your face to the sunshine and you cannot see the shadows."
        ]
        return random.choice(quotes).upper()
    
    if "flip" in message:
        return f"flips a coin It's {random.choice(['heads', 'tails'])}!"
    
    if "roll" in message:
        return f" You rolled a {random.randint(1, 6)}!"
    
    if "weather" in message:
        conditions = ["sunny", "rainy", "thunder storm", "windy", "stormy"]
        return f"Looking out my virtual window, it seems {random.choice(conditions)} today!"
    
    if "time" in message:
        return "I'm still learning to tell time! "
    
    # Check for user's name in message
    if user_name.lower() in message:
        return f"Hey {user_name}! I noticed you're talking about yourself!"
    
    # Default response using string slicing
    if len(message) > 10:
        return f"Interesting message! The first few characters were: '{message[:10]}...'"
    
    return "Beep boop! I'm here if you need anything!"



def spin_twister_spinner():
    """
    Generates random Twister game information.
    
    Returns:
        list: List containing color and body part
    """
    colors = ["red", "black", "yellow", "green"]
    body_parts = ["left hand", "right hand", "left foot", "right foot"]
    
    info = []
    color = random.choice(colors)
    body_part = random.choice(body_parts)
    
    info.extend([color, body_part])
    return info

import random

def generate_random_adventure():
    """
    Generates a random mini-adventure scenario for the bot to share.

    Returns:
    str: A randomly generated adventure
    """
    locations = [
        "mysterious cave",
        "enchanted forest",
        "abandoned spaceship",
        "hidden mountain temple",
        "underwater city"
    ]
    
    challenges = [
        "solve a riddle",
        "defeat a guardian",
        "find a hidden treasure",
        "escape a trap",
        "repair a broken artifact"
    ]
    
    companions = [
        "a old wizard",
        "a timy sidekick",
        "Naveen",
        "an ancient burruito"
    ]

    location = random.choice(locations)  # Changed variable name to singular
    challenge = random.choice(challenges)  # Changed from random.choices to random.choice
    companion = random.choice(companions)  # Changed from random.choices to random.choice

    adventure = (
        f"You find yourself in a {location}, "
        f"accompanied by {companion}. "
        f"Your mission: {challenge}! "
        "Will you succeed? The adventure awaits!"
    )

    return adventure

# def respond(user_message, user_name):
#     # Check if 'adventure' is in the user's message
#     if "adventure" in user_message.lower():
#         return generate_random_adventure()
    
#     # (rest of the previous code remains unchanged)