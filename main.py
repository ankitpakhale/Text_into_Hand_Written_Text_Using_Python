import pywhatkit
question = input("Enter the question here: ")
answer = input("Enter the answer here: ")
pywhatkit.text_to_handwriting("Question: "+question+"\n"+"Answer: "+answer,rgb=[33, 85, 205])

