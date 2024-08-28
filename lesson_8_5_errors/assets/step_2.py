slots1 = ("09:00", "11:00", "13:00", "15:00", "16:00", "18:00")
slots2 = ("10:00", "12:00", "14:00", "16:00", "17:00", "19:00")
common_slots = []

		for slot in slots1:
    if slot in slots2:
        common_slots.append(slot)

		print("Общее свободное время для встречи:", common_slots)