#! /usr/bin/python3.7

"""
random quiz generator - creates quizzes with questions and answers in random order,
along with answer key
"""


import random, os


# dict for states and capitals
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island':
'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


#create sub dir

subdir = os.path.join(os.getcwd(), "quizzes")
os.makedirs(subdir)
os.chdir(subdir)


# Generate 35 quiz files.
for quizNum in range(1,36):

    questionFile = open("capitalQuiz%s.txt" % (quizNum), "w")
    answerFile = open("capitalQuiz%s_Answers.txt" % (quizNum), "w")

    #header
    questionFile.write("Name: " + "_" * 20)
    questionFile.write("Date: " + "__/__/____")
    questionFile.write("Class: " + "____")
    questionFile.write("\n" * 3)
    questionFile.write(("-" * 5) + "Capital Quiz" + ("-" * 5) + ("\n" * 3))

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):     #create 50 questions
        corrAnswer = capitals[states[questionNum]] # correct capital for state

        wrongAnswers = list(capitals.values()) # list with potential capitlas
        del wrongAnswers[wrongAnswers.index(corrAnswer)]    # deleting correct capital via index
        wrongAnswers = random.sample(wrongAnswers, 3)   # choose 3 random incorrect wrongAnswers

        answerOptions = wrongAnswers + [corrAnswer]
        random.shuffle(answerOptions)

        #write to question file
        questionFile.write("Question " + str(questionNum + 1) + "\n\n")
        questionFile.write("What is the capital of " + states[questionNum] + "?\n\n")
        for a in range(4):
            questionFile.write("ABCD"[a] + " " + answerOptions[a] + "\n")

        questionFile.write(("\n") * 3 )


        #write to answer file
        answerFile.write("Question " + str(questionNum + 1) + ": " + "ABCD"[answerOptions.index(corrAnswer)] + " " + corrAnswer + "\n\n")

    questionFile.close()
    answerFile.close()
