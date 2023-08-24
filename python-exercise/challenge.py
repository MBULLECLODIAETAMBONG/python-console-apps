""""
Write a program that allows a person to personalize a story
Take a page from a book or make up a story. Ask the user to 
enter information you can replace in the story such as their name, 
a place, or insert adjectives or adverbs into the story.
Then display the personalized story to the user
For extra credit make sure you correct anything they type in
with the incorrect case (e.g. if they type an adjective in uppercase you may want to display it in lowercase
"""""

# Getting the required info from the user
name = str(input("What's your name?: "))
location = str(input("What's your location?: "))
school = str(input("What is your institution of study?: "))

# figuring out what thee short story looks like with the credentials gotten from the user above
print("My name is", name.upper(), "am from", location.capitalize(), "\n Am a computer engineer from", school.capitalize(), "\n I so much love python as a programming language")


