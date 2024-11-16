# property to verify
"""
H((P[5:] True) IMPLIES P[:5] battery_published)"""

PROPERTY = r"historically(once[5:]{t} -> once[:5]{battery_published})"

# predicates used in the property (initialization for time 0)

# in here we can add all the predicates we are interested in.. Of course, we also need to define how to translate Json messages to predicates.

# function to abstract a dictionary (obtained from Json message) into a list of predicates

predicates = dict(

    battery_published = False,

    t = True,

    time = 0

)

# in here we can add all the predicates we are interested in.. Of course, we also need to define how to translate Json messages to predicates.

# function to abstract a dictionary (obtained from Json message) into a list of predicates

def abstract_message(message):
    predicates['time'] = message['time']

    if message['topic'] == "clock":
        predicates['battery_published'] = False
    elif message['topic'] == "battery_level":
        predicates['battery_published'] = True

    return predicates