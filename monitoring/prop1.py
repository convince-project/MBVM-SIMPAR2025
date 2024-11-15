"""
H((alarm => P battery_level < 30%) AND - ( -alarm S[5 : ] battery_level  < 30%))"""

PROPERTY = r"historically(({alarm} -> once{low_battery}) and not( not {alarm} since[5:] {low_battery}))"

# predicates used in the property (initialization for time 0)

# in here we can add all the predicates we are interested in.. Of course, we also need to define how to translate Json messages to predicates.

# function to abstract a dictionary (obtained from Json message) into a list of predicates

predicates = dict(

    time = 0,

    alarm = False,

    low_battery = False,

)

# in here we can add all the predicates we are interested in.. Of course, we also need to define how to translate Json messages to predicates.

# function to abstract a dictionary (obtained from Json message) into a list of predicates

def abstract_message(message):

    predicates['time'] = message['time']

    predicates['alarm'] = False

    predicates['low_battery'] = False


    return predicates