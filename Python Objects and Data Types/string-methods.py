message = "Hi, Naber yo!"
message1 = message.upper()
message2 = message.lower()
message3 = message.title() #each letter of a word is upper
message4 = message.capitalize() #just first letter is upper

# print(message)

message5 = message.strip() #if the first and last letter is space (" "), it deletes
message6 = message.split() #it is a series of the words in the sentence

# print(message6)

# message7 = "*".join(message6)
# print("  I merged again! with join()  "+ message7)
# index = message.lower().find("naber")

# isStarted = message.startswith("H")
# isEnded = message.endswith("yo!")
# print(isEnded)

# message8 = message.replace("Hi", "HELLOOO")
# message9 = message.replace("Hi", "Hey!").replace("yo", "Yey").replace().....
# print(message8)

message10 = message.center(31, "-")
print(message10)