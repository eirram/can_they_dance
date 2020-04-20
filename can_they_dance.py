# !Python 3
#
# filename can_they_dance.py
#
# This project is an attempt to model participants of the popular British
# dance show 'Strictly Come Dancing'. User should be able to enter the name
# a celebrity, or anybody else for that matter, and the program should return
# results saying whether this person participated or not. If the name of a
# participant is true, then the programs presents a number of facts around
# that celebrity dancer.

# First we tackle the most recent year to work out the kinks and bugs.
# As the professionals cover multiple series, keys and values may be
# different.

# Professionals 2019: We nest a list inside a dictionary,
# as we want more than 1 value associated with the key 'professionals':
professionals_2019 = {'professionals':
                      ['AJ pritchard',
                       'katya jones',
                       'aljaž skorjanec',
                       'amy dowden',
                       'anton du beke',
                       'janette manrara',
                       'neil jones',
                       'oti mabuse',
                       'kevin clifton',
                       'karen clifton',
                       'nadiya bychkova',
                       'graziano di prima',
                       'gorka marquez',
                       'johannes radebe',
                       'luba mushtuk',
                       'giovanni pernice',
                       'dianne buswell',
                       'nancy xu'],
                      }

# Celebrities Glossary.
celebrities_glossary = {
    'david james': {
        'first': 'david',
        'last': 'james',
        'title': 'mbe',
        'year': '2019',
        'professional': 'out',
        'series': '17',
        'final position': 'out',
        'week eliminated': 'out',
        'score': '',
        'cursed': '',
    },
    'chris ramsey': {
        'first': 'chris',
        'last': 'ramsey',
        'title': '',
        'year': '2019',
        'professional': 'karen clifton',
        'series': '17',
        'final position': 'eliminated',
        'week eliminated': '12',
        'score': '',
        'cursed': '',
    },
    'emma barton': {
        'first': 'emma',
        'last': 'barton',
        'title': '',
        'year': '2019',
        'professional': 'anton du beke',
        'series': '17',
        'final position': 'runner up',
        'week eliminated': '10',
        'score': '',
        'cursed': '',
    },
    'saffron barker': {
        'first': 'saffron',
        'last': 'barker',
        'title': '',
        'year': '2019',
        'professional': 'AJ pritchard',
        'series': '17',
        'final position': 'eliminated',
        'week eliminated': '10',
        'score': '',
        'cursed': '',
    },
    'katherine tyldesley': {
        'first': 'katherine',
        'last': 'tyldesley',
        'title': '',
        'year': '2019',
        'professional': 'johannes radebe',
        'series': '17',
        'final position': 'eliminated',
        'week eliminated': '6',
        'score': '',
        'cursed': '',
    },
    'mike bushell': {
        'first': 'mike',
        'last': 'bushell',
        'title': '',
        'year': '2019',
        'professional': 'katya jones',
        'series': '17',
        'final position': 'eliminated',
        'week eliminated': '8',
        'score': '',
        'cursed': '',
    },
    'karim zeroual': {
        'first': 'karim',
        'last': 'zeroual',
        'title': '',
        'year': '2019',
        'professional': 'amy dowden',
        'series': '17',
        'final position': 'runner up',
        'week eliminated': '',
        'score': '',
        'cursed': '',
    },
    'emma thynn': {
        'first': 'emma',
        'last': 'thynn',
        'title': 'viscountess weymouth',
        'year': '2019',
        'professional': 'aljaž skorjanec',
        'series': '17',
        'final position': 'eliminated',
        'week eliminated': '7',
        'score': '',
        'cursed': '',
    },
    'michelle visage': {
        'first': 'michelle',
        'last': 'visage',
        'title': '',
        'year': '2019',
        'professional': 'giovannice pernice',
        'series': '17',
        'final position': 'eliminated',
        'week eliminated': '9',
        'score': '',
        'cursed': '',
    },
    'will bayley': {
        'first': 'will',
        'last': 'bayley',
        'title': 'mbe',
        'year': '2019',
        'professional': 'out',
        'series': '17',
        'final position': 'out',
        'week eliminated': 'out',
        'score': 'out',
        'cursed': '',
    },
    'alex scott': {
        'first': 'alex',
        'last': 'scott',
        'title': 'mbe',
        'year': '2019',
        'professional': 'neil jones',
        'series': '17',
        'final position': 'eliminated',
        'week eliminated': '10',
        'score': '',
        'cursed': '',
    },
    'dev griffin': {
        'first': 'dev',
        'last': 'griffin',
        'title': '',
        'year': '2019',
        'professional': 'dianne bushwell',
        'series': '17',
        'final position': 'eliminated',
        'week eliminated': '4',
        'score': '',
        'cursed': '',
    },
    'james cracknell': {
        'first': 'james',
        'last': 'cracknell',
        'title': 'obe',
        'year': '2019',
        'professional': 'luba mushtuk',
        'series': '17',
        'final position': 'eliminated',
        'week eliminated': '2',
        'score': '',
        'cursed': '',
    },
    'anneka rice': {
        'first': 'anneka',
        'last': 'rice',
        'title': '',
        'year': '2019',
        'professional': 'kevin clifton',
        'series': '17',
        'final position': 'eliminated',
        'week eliminated': '3',
        'score': '',
        'cursed': '',
    },
    'kelvin fletcher': {
        'first': 'kelvin',
        'last': 'fletcher',
        'title': '',
        'year': '2019',
        'professional': 'oti mabuse',
        'series': '17',
        'final position': 'winner',
        'week eliminated': '',
        'score': '',
        'cursed': 'yes',
    },
}

# Main code asking user to enter a name, or enter quit.
# Using a while loop and Active flag. Got the idea from Python
# Crash Course.
#
# Made sure to allow for an empty string to continue the loop
# and a break statement to exit the loop. 

prompt = "\nPlease enter the celebrity's name, "
prompt += "or enter 'quit' to exit:  "

active = True
while active:
    celebrity_name = input(prompt)
    if celebrity_name == '':
        continue
    if celebrity_name == 'quit':
        break
    if celebrity_name in celebrities_glossary:
        print(celebrity_name.title() + " danced in series " +
              celebrities_glossary[celebrity_name]['series'] + ", " +
              celebrities_glossary[celebrity_name]['year'] + "." +
              "\nProfessional partner: \t" +
              celebrities_glossary[celebrity_name]['professional'].title() + ".")
        print("Final position: \t" +
              celebrities_glossary[celebrity_name]['final position'].title())
    else:
        print("That person did not dance in 2019.")

# Epilogue;
# This was my first attempt to complete an idea into working code.
# 
# This format of dictionary and lookup seems to work well. There is of
# course not much in the sense of complexity.

# Should I come up with more ideas around this project, the github
# repository will be updated. For now I consider this project to be
# finished as far as the educational aspect goes.
