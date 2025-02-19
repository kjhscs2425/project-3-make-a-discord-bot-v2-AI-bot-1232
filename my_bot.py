"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
from http.client import responses
import random 

def should_i_respond(user_message, user_name):
   
    message = user_message.lower()
    
    trigger_phrases = [
        "hello bot", "flip","game", "joke", "what is the weather", "time", "roll","henry","justin","quote","roi","helpful", "not useful","facts","gordon","scramble","Jordon is bad at fortnite"
    ]
    
    vowel_count = sum(1 for char in message if char in 'aeiou')
 
    for phrase in trigger_phrases:
        if phrase in message:
            return True
            
def respond(user_message, user_name):

    message = user_message.lower()
    
    
    print(f"Message: {message}")

    if message.startswith("hello") or message.startswith("hi"):
        return f"Hello {user_name.capitalize()}! How can I help you today?"
    
    if "joke" in message:
        joke = [
            "Why don't programmers like nature? It has too many bugs!",
            "What do you call a bot that steals? A ROB-ot!",
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "Why don't skeletons fight each other? Because they don't have the guts.", 
            "How do get straight A's? By using a ruler"

        ]
        return random.choice(joke)
    

    if "quote" in message:
        quote = [
            "Be the change you wish to see in the world.",
            "Code is poetry in motion.",
            "Keep your face to the sunshine and you cannot see the shadows.",
        ]
        return random.choice(quote).upper()
    
    
    if "flip" in message:
        return f"flips a coin It's {random.choice(['heads', 'tails'])}!"
    
    if "roll" in message:
        return f" You rolled a {random.randint(1, 6)}!"
    import datetime

    x = datetime.datetime.now()
    if "weather" in message:
        conditions = ["sunny", "rainy", "thunder storm", "windy", "stormy"]
        return f"Looking out my virtual window, it seems {random.choice(conditions)} today!"
    
    if "henry" in message:
        print("omg henry!!")
        return random.choice(
            [
                "RIP Henry - taken out by a pillager in Minecraft", 
                "Henry vs pillager: pillager 1, Henry 0", 
                "Legend says Henry is still respawning from that pillager encounter..."
            ]
        )
        
    if "time" in message:
        return "you tell what the time is"
    if user_name.lower() in message:
        return f"Hey {user_name}! I noticed you're talking about yourself!"
    if len(message) > 10:
        return f"Interesting message! The first few characters were: '{message[:10]}...'"
    if "random number" in message:
        return "1,5,4,3,2,8,345,234,123,56345,8745!"
    if "justin" in message:
       return "be quite timy your gonna get us kicked out of the JCC"
    if "roi" in message:
       return "I like cats"
    if "not useful" in message:
       return "sorry, what else can I help you with"
    if "helpful" in message:
       return "Thanks, anything else I can help you with"
    if "facts" in message:
       return random.choice(
            [
            "Australia is wider than the moon: Australia is almost 4,000 km across from east to west, while the moon is only 3,400 km in diamete",
            "Avocados are fruits: Avocados are technically fruits, not vegetables.", 
            "Alaska is the only US state typed with one row of the keyboard: Alaska is the only US state that can be typed using one row of the keyboard.",
            "You can't hum while holding your nose",
            "A cloud weighs around a million tonnes.",
            "Venus is the only planet to spin clockwise.",
            "Reindeer like to eat bananas.",
            ]
        )       
    if "gordon" in message:
       return random.choice(
          [
             "My gran could do better! And shes dead!",
             "There’s enough garlic in here to kill every vampire in Europe.",
             "Don't just stand there like a big bleep muffin",
             "This fish is so raw, he’s still finding Nemo.",
             "You added so much salt and pepper I can hear the dish singing ‘Push It",
             "This pizza is so disgusting, if you take it to Italy you'll get arrested",
          ]
       )
      
    if "scramble" in message:
        chars = list(message)
        random.shuffle(chars)
        scrambled = ''.join(chars)
        return f"Your scrambled message: {scrambled}"
    if "Jordon is bad at fortnite" in message:
       chars = list(message)
       random.shuffle(chars)
       scrambled = ''.join(chars)
       return f"Your scrambles message {message}"
   
    return "im not sure how to answer that"

    


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


def get_player_choice():
  while True:
    choice = input("Choose Rock, Paper, or Scissors: ").lower()
    if choice in ["rock", "paper", "scissors"]:
      return choice
    else:
      print("Invalid choice. Please try again.")

def get_computer_choice():
  return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
  print(f"You chose {player_choice}, computer chose {computer_choice}.")
  if player_choice == computer_choice:
    print("It's a tie!")
  elif (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "paper" and computer_choice == "rock") or \
       (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
  else:
    print("You lose!")

while True:
  player_choice = get_player_choice()
  computer_choice = get_computer_choice()
  determine_winner(player_choice, computer_choice)

  play_again = input("Play again? (y/n): ").lower()
  if play_again != "y":
    break


