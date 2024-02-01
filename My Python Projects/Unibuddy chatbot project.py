
'''
[Case Study Story] --> Imagine the first day of university for a freshman named Alex. greee
Alex is excited but also overwhelmed by the vast campus, numerous courses, and the sea of new faces. 
To aid new students like Alex, the university's IT department has developed a personalised chatbot. 
This chatbot, named "UniBuddy", is designed to make the transition smoother for freshmen.
Upon accessing the chatbot, Alex is prompted to enter their name, favourite colour, and age. 
Based on this input, UniBuddy offers a personalised greeting.
For instance, if Alex's favourite colour is blue,
    UniBuddy might suggest joining the university's "Blue Art Club".
If Alex is 18, the chatbot might provide information about freshman-specific events.
The chatbot also offers a feature where Alex can input specific queries, like "Where is the library?"
    or "How do I join the debate club?", 
        and UniBuddy responds with relevant information, all while adhering to a friendly tone,
        using string transformation methods to ensure the responses feel personalised and engaging.
'''

# Initialise message, for first-time start
print('''
Welcome to UniBuddy! Your all-in-one app that makes your freshman journey a bit
easier to navigate!
    Please enter your credentials to get started! :
''')

user_name = input("Please enter your student name: ").capitalize()
user_age = int(input("Please enter your age: "))
fav_colour = input("Please enter your favourite colour: ").capitalize()

print(f"""
Welcome {user_name}! I see that your favourite colour is {fav_colour}.
I have a few suggestions based on your choice!
""")

if fav_colour == 'Red':
    print("If you like the colour RED, I have the following for you! Check out: ")

    print("""
1. Martial Arts Enclave - Join a club that practices various forms inspired by red-themed movies.
2. Crimson Cardio Club - Engage in intense workout sessions to stay fit and active.
3. Blood Donation Society - Make a difference in the community by joining this philanthropic group.
4. Red Planet Stargazers - Explore the wonders of the night sky with astronomy enthusiasts.
""")

elif fav_colour == 'Blue':
    print("If you like the colour BLUE, I have the following for you! Check out: ")

    print("""
1. Deep Dive Swimmers - Improve your swimming skills and participate in water-related activities.
2. Blue Canvas Art Society - Express your creativity through painting and artistic pursuits.
3. Skywalkers Hiking Club - Embark on scenic hikes and enjoy the great outdoors.
4. Blue Note Music Collective - Join fellow musicians and explore various music genres.
""")

elif fav_colour == 'Yellow':
    print("If you like the colour YELLOW, I have the following for you! Check out: ")

    print("""
1. Sunshine Yoga Community - Embrace tranquility and flexibility through yoga practices.
2. Mountain Explorers Club - Conquer hiking trails and experience the thrill of mountain adventures.
3. Dance Fusion Society - Join a vibrant dance community and express yourself through dance.
""")

else:
    print("I'm not sure if that was a colour you have entered; please try again.")

if user_age <= 22:
    print("Here are some freshman-specific events!")
    print("""
1.  Freshers party - Join us for an exciting night of music, food, and socializing.
2.  Freshers Academic Orientation - Get to know the ins and outs of your academic journey
3.  Fresher University Tour - Helping new students become familiar with the campus layout, facilities.
4.  Freshers Fair - Ideal for new students to explore and join groups matching their interests.
""")

else:
    print("Here are a few event suggestions that might be to your liking!")
    print("""
1. All Cultures Fair - Celebrate diversity by organizing a fair that showcases different cultures through food, music, and traditional activities. It's an excellent way for international and local students to connect.
Tech Meetup:
2. Tach Fair : For students interested in technology, host a tech meetup where they can discuss the latest trends, network, and even collaborate on small projects.
Wellness Day : Based around mindfulness workshops, and health tips to help students manage stress.
""")




# FAQ ; frequently asked questions
question = input("Is there anything you would like to ask me? (type in q to quit): ")

if question == 'How is your day':
    print("I exist, so my day is going rather well!")

