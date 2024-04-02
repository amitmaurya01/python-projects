'''
Filename : madlibs.py
Author : Amit Maurya
'''

# string concatnation

# youtube_channel = "FreeCodeCamp.org"

# print("Subscribe to "+youtube_channel)
# print("Subscribe to {}".format(youtube_channel))
# print(f"Subscribe to {youtube_channel}")


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)