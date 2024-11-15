"""
H((P[5:] True) IMPLIES P[:5] battery_published)"""

PROPERTY = r"historically(once[0.0000001:]{t} -> once[:0.0000001]{battery_published})"

# predicates used in the property (initialization for time 0)

# in here we can add all the predicates we are interested in.. Of course, we also need to define how to translate Json messages to predicates.

# function to abstract a dictionary (obtained from Json message) into a list of predicates

predicates = dict(

    time = 0,

    t = True,

    battery_published = False

)

# in here we can add all the predicates we are interested in.. Of course, we also need to define how to translate Json messages to predicates.

# function to abstract a dictionary (obtained from Json message) into a list of predicates

def abstract_message(message):

    predicates['time'] = message['time']
    
    predicates['battery_published'] = 'topic' in message and 'battery' in message['topic']

    return predicates
