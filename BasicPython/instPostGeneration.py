import random
# List of possible post templates
post_templates = [
    "🎓📚 Ready to learn something new? Check out our comprehensive digital course for beginners! #DigitalCourse #BeginnersWelcome #LearnSomethingNew",
    "👋🏼👋🏾 Hey there! Are you a beginner looking to dive into the digital world? Our course has got you covered. #DigitalBeginners #OnlineCourse #JoinUs",
    "🤩👨🏻‍💻👩🏾‍💻 Exciting news! Our digital course for beginners is now live. Enroll now and start your digital journey. #NewCourse #DigitalLearning #EnrollNow",
    "🌟🎉 Join the community of digital learners with our comprehensive course for beginners. Get started today! #DigitalCommunity #BeginnersCourse #GetStarted",
    "🤔🤯 Feeling overwhelmed by the digital world? Our course breaks it down into manageable steps for beginners. #DigitalOverwhelm #BeginnersWelcome #StartSmall"
]

# List of possible call-to-actions
call_to_actions = [
    "Enroll now!",
    "Join us today!",
    "Get started!",
    "Sign up now!",
    "Start your journey!",
    "Let's go!"
]

# List of possible emojis
emojis = ["🎓", "📚", "👨🏻‍💻", "👩🏾‍💻", "🤩", "👋🏼", "👋🏾", "🤯", "🤔", "🌟", "🎉", "💻", "👨‍💼", "👩‍💼"]

# Generate and print 10 random posts
for i in range(3):
    post_template = random.choice(post_templates)
    call_to_action = random.choice(call_to_actions)
    emojis_list = random.sample(emojis, 3)
    hashtags = "#DigitalCourse #BeginnersWelcome #LearnSomethingNew"  # Add more hashtags as needed

    # Combine post elements and print
    post = f"{post_template} {emojis_list[0]} {emojis_list[1]} {emojis_list[2]} {call_to_action} {hashtags}"
    print(post)
