# Determines the level depending on the amount of experience.
def get_level (xp):

	if xp >= 10000:
		return 20
	elif xp >= 8410:
		return 19
	elif xp >= 7009:
		return 18
	elif xp >= 5782:
		return 17
	elif xp >= 4716:
		return 16
	elif xp >= 3798:
		return 15
	elif xp >= 3015:
		return 14
	elif xp >= 2353:
		return 13
	elif xp >= 1802:
		return 12
	elif xp >= 1350:
		return 11
	elif xp >= 985:
		return 10
	elif xp >= 696:
		return 9
	elif xp >= 473:
		return 8
	elif xp >= 306:
		return 7
	elif xp >= 186:
		return 6
	elif xp >= 104:
		return 5
	elif xp >= 52:
		return 4
	elif xp >= 22:
		return 3
	elif xp >= 7:
		return 2
	elif xp >= 1:
		return 1
