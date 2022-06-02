import pandas
import datetime
PMs = pandas.read_excel('input.xlsx', sheet_name='PMs').to_dict(orient='records')
Commands = pandas.read_excel('input.xlsx', sheet_name='Commands')


def get_time_slots(period, slot_duration):
	period_list = period.split('-')
	time_slots = []
	start_period = datetime.datetime.strptime(period_list[0],'%H:%M')
	end_period = datetime.datetime.strptime(period_list[1],'%H:%M')
	start_period_slot = start_period
	timedelta = datetime.timedelta(minutes=slot_duration)
	while start_period_slot + timedelta <= end_period:
		time_slots.append(start_period_slot.strftime('%H:%M'))
		start_period_slot = start_period_slot + timedelta
	return (time_slots)

slot_duration = 20 # можно задавать длину слота в минутах 

index = 0
for PM in PMs:
	time_slots = get_time_slots(PM['period'], slot_duration)
	for time_slot in time_slots:
		new_row = {
		'number' : index,
		'PM_name' : PM['name'],
		'slot' : time_slot,
		}
		Commands = Commands.append(new_row, ignore_index=True)
		index += 1
print(Commands)
Commands.to_excel('output_commands.xlsx')
