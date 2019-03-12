# Supports two Basic Types of Loops

# 1. While and For Loop.

players = ['Kemba', 'Tim', 'Byron', 'Jokic', 'Kozlov']

i = 0;
while(i < 5):
    #print(players[i])
    i += 1

# Simplest for loop
for x in players:
    print(x)

# Python uses "range" function which behaves like xrange
# xrange returns an iterator which is more efficicent.
for numbers in range(5):
    print(numbers)

# "break" and "continue" statements
# Exit and Skips respectively
for prime in range(10):
    if prime % 2 == 0:
        continue
    print(prime)

count = 0
while True:
    print('Counter at {}'.format(count))
    count += 1
    if count > 5:
        break

# Else can be used with Loops too.
# Code in else executes even when there is a continue inside loop
# But never executes if a break is inside a loop
trip = 0
while trip < 5:
    print(f"Trip number {trip}")
    trip += 1
else:
    print(f"Trip value reached {trip}")
