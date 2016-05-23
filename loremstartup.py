import math
import random
import LoremStartupDictionary as LSD # ayylmao

def generate(length=30):
	"""
	Input:
	length -- desired length (in 'words') of the lorem statement

	Output:
	lorem -- the generated lorem statement
	"""
	if length <= 0:
		return
	elif length == 1:
		return "Lorem"
	elif length == 2:
		return "Lorem ipsum"

	count = 0
	lorem = "Lorem ipsum"

	new_sentence = False
	while count < length:
		# This is arbitrary
		divisor = random.random()*3
		# This is also arbitrary
		sentence_length = random.randint(3, math.ceil(length/divisor))
		for word in xrange(sentence_length):
			if new_sentence:
				lorem += " " + random.choice(LSD.upperdict)
				new_sentence = False
			else:
				lorem += " " + random.choice(LSD.lowerdict)
			count += 1
			if count == length:
				return lorem + "."
		# So is this
		if random.random() > .35:
			lorem += ","
		else:
			lorem += "."
			new_sentence = True

	return lorem + "."

print generate(40)