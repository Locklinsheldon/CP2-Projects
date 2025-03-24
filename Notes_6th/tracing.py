#Locklin Sheldon, Degubbing notes
import trace
import sys

def trace_calls(frame, event, arg):
    if event == 'call':
        print(f'Call functions: {frame.f_code.co_name}')
    elif event == 'call': 
        print(f'Calling fu')

    return trace_calls

sys.settrace(trace_calls)
tracer = trace.trace(count=False, trace=True)
#Wuz tracing?
def sub(numone, numtwo):
    return numone - numtwo


def add(numone, numtwo):
    print(sub)
    return numone + numtwo


print(add)

#Allows you to access functions
#python -m trace --trace Notes_6th\tracing.py
#trace (displays lines as executed)
#count (displays number of times executed)
#listfuncs (displays functions used in the program)
#track calls (displys relationships between functions)

#F5
#Click debooger
#Dropdown thingy
#Testing is running your code to make sure it works as required.
#Boundry conditions = check the entries most likely to be wrong