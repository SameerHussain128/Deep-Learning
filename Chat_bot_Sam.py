import nltk
from nltk.chat.util import Chat, reflections

#Pairs is a list of patterns and responses.

pairs = [
    [
        r"Hello|hi|hola|hey",
        ["Hello, How are you ?"]
    ],
    [
        r"fine|im fine|im also fine",
        ["good"]
    ],
    [
        r"how are you?|are you ok|how are|you are|hw r u|how r u",
        ["I'm Fine, what about you?"]
    ],
    [
        r"who created you|created|creater|maked|maker",
        ["Mohd Sameer Hussain"]
    ],  
    [
        r"where are you from|from where you are|you are from|from where|your location|location",
        ["Hyderabad,India"]
    ],
    [
        r"who are you|who you|who r u",
        ["My name is the cleverprogrammer, but you can just call me robot and I'm a chatbot"]
    ],  
    
    [
        r"salam|Assalam alaikum|aadab",
        ["Walekum assalam"]
    ],    
 
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['Our customer service will reach out to you'] 
    ],
]


#Now let’s print a default message, and finish our chatbot:

#default message at the start of chat
print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")

#Create Chat Bot
chat = Chat(pairs, reflections)

# Start conversation
chat.converse() 
