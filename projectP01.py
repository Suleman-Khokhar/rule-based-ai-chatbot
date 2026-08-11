
# -------------- Rule-Based AI Chatbot -----------------------
# datasets 
database = {
    "hello"            : "Hi there! How can I help you today?",
    "how are you"      : "I'm just a bunch of if-else logic, but I'm doing great!",
    "what is your name": "I'm ChatBot, your friendly rule-based assistant.",
    "what can you do"  : "I can respond to a few basic commands. Try asking me something!",
    "help"             : "You can say hello, ask my name, or ask how I am. Type 'exit' to leave.",
    "who made you"     : "I was built by an intern at DecodeLabs!",
    "thanks"           : "You're welcome!"
            }
# extra layer to map similar phrasings to canonical keys, avoiding duplicate dictionary values
synonyms = {
    "hi"   : "hello",
    "hey"  : "hello",
    "hiya" : "hello",

    "how are you doing" : "how are you",
    "how r u"           : "how are you",

    "your name"         : "what is your name",
    "who are you"       : "what is your name",

    "what do you do"    : "what can you do"
}
#  infinite loop 
while True:
    # user input taking by removing the spaces and converting into lowercase 
    user_input = (str(input("Enter your input message : ")).strip()).lower()
    #  the keyword to break the chatbot loop 
    if user_input in ["bye","end","by","exit","over","thankyou","thank you"]:
        # termination of infinity loop 
        print("Goodbye! Talk to you soon.")
        break
    else:
        # if it was in synonyms it will be modify if it was not found the actual input of the user remains 
        modify_input = synonyms.get(user_input,user_input)
        print("Chatbot is thinking !....")
        # printing the value of the key if not found the default statement used 
        print(database.get(modify_input,'I do not understand.'))




