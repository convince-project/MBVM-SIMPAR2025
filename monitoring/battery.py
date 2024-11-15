# property to verify

PROPERTY = r"once{low_percentage} -> once{service}"

# predicates used in the property (initialization for time 0)

predicates = dict(

    time = 0,

    service = False,

    low_percentage = False

)

# in here we can add all the predicates we are interested in.. Of course, we also need to define how to translate Json messages to predicates.

# function to abstract a dictionary (obtained from Json message) into a list of predicates

def abstract_message(message):
    print("predicates")
    print(predicates)
    if 'response' in message:
        predicates['time'] = predicates['time'] + 0.0000001
    else:
        predicates['time'] = message['time']

    predicates['service'] = True if 'service' in message else False

    predicates['low_percentage'] = True if 'percentage' in message and message['percentage'] < 30 else False


    return predicates

