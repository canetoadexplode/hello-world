import time
print 'Welcome! It\'s pavlova time!'

print '''Please select an option
(1) Read the recipe
(2) Realtime recipe guide'''
whatdo = raw_input()
print '''Please select a language
(1) English
(2) Swedish'''
whatlang = raw_input()

if whatdo == '1':
	if whatlang == '1':
		print '''
Ingredients:
4 egg whites
1 cup sugar
1 Tbsp cornstarch
1 tsp vinegar
2 tsp vanilla

Instructions:
Whip egg white until peaks form.
Add sugar slowly and continue to beat 7 minutes.
Make paste with cornstarch, vinegar, vanilla.
Add the paste to whipped egg whites and beat 4 minutes.
Line pan with parchment paper.
Plop mixture on pan in a circle.
Note- Do not handle the batter too much, just enough to get the form.
Place in 350*F oven, immediately turn oven to 225*F and bake 1 hour.
Turn off oven and leave in the oven 2 hours or overnight.

Top with whip cream and fruit.'''

	elif whatlang == '2':
		print 'Shit. Helen forgot to build the swedish bullshit.'
elif whatdo == '2':
	if whatlang == '1':
		step_one = 'no'
		while step_one == 'no':
			print '''Welcome to Helen\'s Realtime Recipe Guide (TM, patent pending)! 
I\'ll be with you every step of the way to remind you of the recipe, 
offer helpful tips, and keep track of the timing!
Also, I'm an idiot. So if I ask you a question, 
just type yes or no: no capitalization, no maybes. Got it?'''
			step_one = raw_input()
	elif whatlang == '2':
		print 'Still no swedish thing, sorry bro'
else:
	print 'Error. Does not compute. Initiating self destruct in:'
	for i in xrange(10,0,-1):
		time.sleep(1)
		print i