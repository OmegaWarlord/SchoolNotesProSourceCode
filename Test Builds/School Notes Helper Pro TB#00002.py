import tkinter as tk
import datetime
import easygui as e #Datetime for updating label, easygui for simple boxes
import os
currenttime = None
CurClass = None
weekday = datetime.now().strftime("%A")
winopacity = []
homeworklist = []
homeworkdue = []
bgcolor = '#ffffff'
fgcolor = '#000000'
weekdayNoCustom = True
# Lets not use batch comamnds because I want this to have ubuntu support

'''
***HEADER***

School Notes Pro 

Original written by A.I.

School Notes Pro written by A.I. & G.N.

All rights reserved
'''

# GLOBAL VARS GO HERE:
version = '1.3.0'
title = f'School Notes Pro v{version}'

##Creates a list of time intervels
def datetime_range(start, end, delta):
	current = start
	while current < end:
		yield current
		current += delta

dts = [dt.strftime('%I:%M-%p') for dt in
	   datetime_range(datetime.datetime(2016, 1, 1), datetime.datetime(2016, 1, 2),
	   timedelta(minutes=1))]

dtsd = [dt.strftime('%D') for dt in
   datetime_range(datetime.datetime(2020,1,1), datetime.datetime(2030, 1, 1),
   timedelta(days=1))]

def globalize(): global version, title
globalize()
#################

def msg(x): e.msgbox(x, title)

home = os.path.expanduser("~")
defaultpath = home + '\\Documents\\.schoolnotespro'
customPath = defaultpath+'\\custom'
hwFile = home + '\\Documents\\.schoolnotespro\\hwFile.wlist'
configFile = home + '\\Documents\\.schoolnotespro\\settingsFile.wlist'


MonFile = customPath+'\\Mon.wlist'
TueFile = customPath+'\\Tue.wlist'
WedFile = customPath+'\\Wed.wlist'
ThurFile = customPath+'\\Thur.wlist'
FriFile = customPath+'\\Fri.wlist'
# Get user input

def customClasses():

	os.mkdir(defaultpath)
	os.mkdir(customPath)

	global values
	values = []
	classesAmount = e.multenterbox(msg='How many classes do you have on each day (including clubs)?', title=title, fields=[
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thursday",
		"Friday",
		])
	if classesAmount == None: os.rmdir(customPath); os.rmdir(defaultpath); exit()
	if "" in classesAmount: msg('Please fill in all fields.')

	for i in range(int(classesAmount[0])):
		i = int(i+1)
		values.append(i)
	MonClasses = e.multenterbox(msg = 'Please enter your Monday classes in order:', title=title,
		fields=values)
	values = []

	for i in MonClasses:
		index = MonClasses.index(i)
		a = e.multenterbox(msg="Pick start/end time of this period ("+i+", Monday) HH:MM-AM/PM", title=i, fields=['Start', 'End'])
		if a == None or '' in a: os.rmdir(customPath); os.rmdir(defaultpath); exit()
		start = a[0]; end = a[1]
		if start in dts: pass
		else: msg("Invalid input."); os.rmdir(customPath); os.rmdir(defaultpath); exit()
		if end in dts: pass
		else: msg("Invalid input."); os.rmdir(customPath); os.rmdir(defaultpath); exit()
		i = i.replace(' ', '$_')
		i = ' '.join([i,f"Start:{start}", f"End:{end}"])
		MonClasses[index] = i

	Mon = open(MonFile,'x')
	Mon.close()
	Mon = open(MonFile,'w')
	for Aclass in MonClasses:
		Mon.write(Aclass+'\n')
	Mon.close()

	for i in range(int(classesAmount[1])):
		i = int(i+1)
		values.append(i)
	TueClasses = e.multenterbox(msg = 'Please enter your Tuesday classes in order:', title=title,
		fields=values)
	values = []

	for i in TueClasses:
		index = TueClasses.index(i)
		a = e.multenterbox(msg="Pick start/end time of this period ("+i+", Tuesday) HH:MM-AM/PM", title=i, fields=['Start', 'End'])
		if a == None or '' in a: os.rmdir(customPath); os.rmdir(defaultpath); exit()
		start = a[0]; end = a[1]
		if start in dts: pass
		else: msg("Invalid input."); os.rmdir(customPath); os.rmdir(defaultpath); exit()
		if end in dts: pass
		else: msg("Invalid input."); os.rmdir(customPath); os.rmdir(defaultpath); exit()
		i = i.replace(' ', "$_")
		i = ' '.join([i,f"Start:{start}", f"End:{end}"])
		TueClasses[index] = i

	Tue = open(TueFile,'x')
	Tue.close()
	Tue = open(TueFile,'w')
	for Aclass in TueClasses:
		Tue.write(Aclass+'\n')
	Tue.close()

	for i in range(int(classesAmount[2])):
		i = int(i+1)
		values.append(i)
	WedClasses = e.multenterbox(msg = 'Please enter your Wednesday classes in order:', title=title,
		fields=values)
	values = []

	for i in WedClasses:
		index = WedClasses.index(i)
		a = e.multenterbox(msg="Pick start/end time of this period ("+i+", Wednesday) HH:MM-AM/PM", title=i, fields=['Start', 'End'])
		if a == None or '' in a: os.rmdir(customPath); os.rmdir(defaultpath); exit()
		start = a[0]; end = a[1]
		if start in dts: pass
		else: msg("Invalid input."); os.rmdir(customPath); os.rmdir(defaultpath); exit()
		if end in dts: pass
		else: msg("Invalid input."); os.rmdir(customPath); os.rmdir(defaultpath); exit()
		i = i.replace(' ', '$_')
		i = ' '.join([i,f"Start:{start}", f"End:{end}"])
		WedClasses[index] = i

	Wed = open(WedFile,'x')
	Wed.close()
	Wed = open(WedFile,'w')
	for Aclass in WedClasses:
		Wed.write(Aclass+'\n')
	Wed.close()

	for i in range(int(classesAmount[3])):
		i = int(i+1)
		values.append(i)
	ThurClasses = e.multenterbox(msg = 'Please enter your Thursday classes in order:', title=title,
		fields=values)
	values = []

	for i in ThurClasses:
		index = ThurClasses.index(i)
		a = e.multenterbox(msg="Pick start/end time of this period ("+i+", Thursday) HH:MM-AM/PM", title=i, fields=['Start', 'End'])
		if a == None or '' in a: os.rmdir(customPath); os.rmdir(defaultpath); exit()
		start = a[0]; end = a[1]
		if start in dts: pass
		else: msg("Invalid input."); os.rmdir(customPath); os.rmdir(defaultpath); exit()
		if end in dts: pass
		else: msg("Invalid input."); os.rmdir(customPath); os.rmdir(defaultpath); exit()
		i = i.replace(' ', '$_')
		i = ' '.join([i,f"Start:{start}", f"End:{end}"])
		ThurClasses[index] = i

	Thur = open(ThurFile,'x')
	Thur.close()
	Thur = open(ThurFile,'w')
	for Aclass in ThurClasses:
		Thur.write(Aclass+'\n')
	Thur.close()

	for i in range(int(classesAmount[4])):
		i = int(i+1)
		values.append(i)
	FriClasses = e.multenterbox(msg = 'Please enter your Friday classes in order:', title=title,
		fields=values)
	values = []

	for i in FriClasses:
		index = FriClasses.index(i)
		a = e.multenterbox(msg="Pick start/end time of this period ("+i+", Friday) HH:MM-AM/PM", title=i, fields=['Start', 'End'])
		if a == None or '' in a: os.rmdir(customPath); os.rmdir(defaultpath); exit()
		start = a[0]; end = a[1]
		if start in dts: pass
		else: msg("Invalid input."); os.rmdir(customPath); os.rmdir(defaultpath); exit()
		if end in dts: pass
		else: msg("Invalid input."); os.rmdir(customPath); os.rmdir(defaultpath); exit()
		i = i.replace(' ', '$_')
		i = ' '.join([i,f"Start:{start}", f"End:{end}"])

		FriClasses[index] = i

	Fri = open(FriFile,'x')
	Fri.close()
	Fri = open(FriFile,'w')
	for Aclass in FriClasses:
		Fri.write(Aclass+'\n')
	Fri.close()

def getClasses(defaultpath):
	def stemSetup():
		classes = e.multenterbox(msg='Type in all of your A-DAY classes:', title=title, fields=[
			'1st Period',
			'3rd Period',
			'4th Period',
			'Design Time (A-DAY)',
		])
		if classes == None: exit()
		if "" in classes: msg('Please fill in all fields.'); getClasses(defaultpath)
		counter = 0
		for i in classes:
			if " " in i: classes[counter] = i.replace(' ', '$_')
			counter+=1

		classes1 = e.multenterbox(msg='Type in all of your B-DAY classes:', title=title, fields=[
			'6th Period',
			'8th Period',
			'9th Period',
			'Design Time (B-DAY)',
		])
		if classes1 == None: exit()
		if "" in classes1: msg('Please fill in all fields.'); getClasses(defaultpath)
		counter = 0
		for i in classes1:
			if " " in i: classes1[counter] = i.replace(' ', '$_')
			counter+=1

		classes2 = e.multenterbox(msg='Type in all of your Istem classes:', title=title, fields=[
			'Monday Istem',
			'Tuesday Istem',
			'Wednesday Istem',
			'Thursday Istem',
			'Friday Istem'
		])
		if classes2 == None: exit()
		if "" in classes2: msg('Please fill in all fields.'); getClasses(defaultpath)
		counter = 0
		for i in classes2:
			if " " in i: classes2[counter] = i.replace(' ', '$_')
			counter+=1

		for i in classes1: classes.append(i)
		for i in classes2: classes.append(i)

		# Write to file
		os.mkdir(defaultpath)
		os.mkdir(defaultpath+'\\custom')

		global MonFile, TueFile, WedFile, ThurFile, FriFile

		# File parser
		j = classes
		Classes = list(j)
		if '' in Classes: Classes.remove('')

		Mclass = [
			Classes[0],
			Classes[8],
			Classes[1],
			Classes[2],
			Classes[3],
		]
		Tclass = [
			Classes[4],
			Classes[9],
			Classes[5],
			Classes[6],
			Classes[7],
		]
		Wclass = [
			Classes[0],
			Classes[10],
			Classes[1],
			Classes[2],
			Classes[3],
		]
		Thclass = [
			Classes[4],
			Classes[11],
			Classes[5],
			Classes[6],
			Classes[7],
		]
		Fclass = [
			Classes[4],
			Classes[7],
			Classes[0],
			Classes[12],
			Classes[1],
			Classes[2],
			Classes[5],
			Classes[6],
			Classes[7],
		]
		if '$_' in Mclass[2]: aday2 = Mclass[2].replace('$_', ' ')
		else: aday2 = Mclass[2]
		if '$_' in Tclass[2]: bday2 = Tclass[2].replace('$_', ' ')
		else: bday2 = Tclass[2]
		seminarA = e.boolbox("When is your seminar time on A-DAY?", title, [f"Before {aday2}", f"After {aday2}"])
		seminarB = e.boolbox("When is your seminar time on B-DAY?", title, [f"Before {bday2}", f"After {bday2}"])

		Mon = open(MonFile,'x')
		Mon.close()
		Mon = open(MonFile,'w')

		Mon.write(f'{Mclass[0]} Start:08:45-AM End:10:08-AM'+'\n')
		Mon.write(f'{Mclass[1]} Start:10:10-AM End:10:54-AM'+'\n')
		Mon.write(f'{Mclass[2]}$_(Before$_Lunch) Start:10:56-AM End:11:06-AM'+'\n')
		Mon.write('Lunch$_Time Start:11:08-AM End:11:38-AM'+'\n')
		if seminarA:
			Mon.write('Seminar Start:11:40-AM End:12:10-PM'+'\n')
			Mon.write(f'{Mclass[2]} Start:12:11-PM End:01:26-PM'+'\n')
		else:
			Mon.write(f'{Mclass[2]} Start:11:40-AM End:12:55-PM'+'\n')
			Mon.write('Seminar Start:12:56-PM End:01:26-PM'+'\n')

		Mon.write(f'{Mclass[3]} Start:01:28-PM End:02:50-PM'+'\n')
		Mon.write(f'{Mclass[4]} Start:02:52-PM End:04:15-PM')
		Mon.close()


		Tue = open(TueFile,'x')
		Tue.close()
		Tue = open(TueFile,'w')

		Tue.write(f'{Tclass[0]} Start:08:45-AM End:10:08-AM'+'\n')
		Tue.write(f'{Tclass[1]} Start:10:10-AM End:10:54-AM'+'\n')
		Tue.write(f'{Tclass[2]}$_(Before$_Lunch) Start:10:56-AM End:11:06-AM'+'\n')
		Tue.write('Lunch$_Time Start:11:08-AM End:11:38-AM'+'\n')
		if seminarB:
			Tue.write('Seminar Start:11:40-AM End:12:10-PM'+'\n')
			Tue.write(f'{Tclass[2]} Start:12:11-PM End:01:26-PM'+'\n')
		else:
			Tue.write(f'{Tclass[2]} Start:11:40-AM End:12:55-PM'+'\n')
			Tue.write('Seminar Start:12:56-PM End:01:26-PM'+'\n')

		Tue.write(f'{Tclass[3]} Start:01:28-PM End:02:50-PM'+'\n')
		Tue.write(f'{Tclass[4]} Start:02:52-PM End:04:15-PM')
		Tue.close()


		Wed = open(WedFile,'x')
		Wed.close()
		Wed = open(WedFile,'w')

		Wed.write(f'{Wclass[0]} Start:08:45-AM End:10:08-AM'+'\n')
		Wed.write(f'{Wclass[1]} Start:10:10-AM End:10:54-AM'+'\n')
		Wed.write(f'{Wclass[2]}$_(Before$_Lunch) Start:10:56-AM End:11:06-AM'+'\n')
		Wed.write('Lunch$_Time Start:11:08-AM End:11:38-AM'+'\n')
		if seminarA:
			Wed.write('Seminar Start:11:40-AM End:12:10-PM'+'\n')
			Wed.write(f'{Wclass[2]} Start:12:11-PM End:01:26-PM'+'\n')
		else:
			Wed.write(f'{Wclass[2]} Start:11:40-AM End:12:55-PM'+'\n')
			Wed.write('Seminar Start:12:56-PM End:01:26-PM'+'\n')

		Wed.write(f'{Wclass[3]} Start:01:28-PM End:02:50-PM'+'\n')
		Wed.write(f'{Wclass[4]} Start:02:52-PM End:04:15-PM')
		Wed.close()


		Thur = open(ThurFile,'x')
		Thur.close()
		Thur = open(ThurFile,'w')

		Thur.write(f'{Thclass[0]} Start:08:45-AM End:10:08-AM'+'\n')
		Thur.write(f'{Thclass[1]} Start:10:10-AM End:10:54-AM'+'\n')
		Thur.write(f'{Thclass[2]}$_(Before$_Lunch) Start:10:56-AM End:11:06-AM'+'\n')
		Thur.write('Lunch$_Time Start:11:08-AM End:11:38-AM'+'\n')
		if seminarB:
			Thur.write('Seminar Start:11:40-AM End:12:10-PM'+'\n')
			Thur.write(f'{Thclass[2]} Start:12:11-PM End:01:26-PM'+'\n')
		else:
			Thur.write(f'{Thclass[2]} Start:11:40-AM End:12:55-PM'+'\n')
			Thur.write('Seminar Start:12:56-PM End:01:26-PM'+'\n')

		Thur.write(f'{Thclass[3]} Start:01:28-PM End:02:50-PM'+'\n')
		Thur.write(f'{Thclass[4]} Start:02:52-PM End:04:15-PM')
		Thur.close()


		Fri = open(FriFile,'x')
		Fri.close()
		Fri = open(FriFile,'w')

		Fri.write(f'{Fclass[0]} Start:08:45-AM End:09:30-AM'+'\n')
		Fri.write(f'{Fclass[1]} Start:09:33-AM End:10:18-AM'+'\n')
		Fri.write(f'{Fclass[2]} Start:10:21-AM End:11:06-AM'+'\n')
		Fri.write('Lunch$_Time Start:11:08-AM End:11:38-AM'+'\n')
		Fri.write(f'{Fclass[3]} Start:11:40-AM End:12:17-PM'+'\n')
		Fri.write(f'{Fclass[4]} Start:12:20-PM End:01:05-PM'+'\n')
		Fri.write(f'{Fclass[5]} Start:01:08-PM End:01:53-PM'+'\n')
		Fri.write(f'{Fclass[6]} Start:01:55-PM End:02:40-PM'+'\n')
		Fri.write(f'{Fclass[7]} Start:02:42-PM End:03:27-PM'+'\n')
		Fri.write(f'{Fclass[8]} Start:03:30-PM End:04:15-PM')
		Fri.close()

	# Get user input
	firstChoice = e.buttonbox("Welcome to the School Notes Pro first time setup!", title, ["STEM 2019 Setup", "Custom"])
	if firstChoice == None: exit()
	if firstChoice == "STEM 2019 Setup": stemSetup()
	elif firstChoice == "Custom": customClasses()

def customclass():
	global MCName, MCStart, MCEnd
	MCName = []; MCStart = []; MCEnd = []
	Monday = open(MonFile,'r')
	Mclass = Monday.readlines()
	Monday.close()
	if "" in Mclass:
		Mclass.remove("")
	for i in Mclass:
		values = i.split(' ', 3)
		ClassName = values[0]
		ClassName = ClassName.replace('$_'," ")
		MCName.append(ClassName)
		StartTime = values[1]
		Start = StartTime.split('-',2)
		Start[0] = Start[0].replace('Start:','')
		if Start[1] == "AM":
			hhmm = Start[0].split(':',2)
			if int(hhmm[0]) == 12:
				hhmm[0] = str(int(hhmm[0])+12)
				Start[0] = ':'.join(hhmm)
			MCStart.append(Start[0])
		elif Start[1] == "PM":
			hhmm = Start[0].split(':',2)
			if int(hhmm[0]) < 12:
				hhmm[0] = str(int(hhmm[0])+12)
				Start[0] = ':'.join(hhmm)
			MCStart.append(Start[0])
		EndTime = values[2]
		End = EndTime.split('-',2)
		End[0] = End[0].replace('End:','')
		End[1] = End[1].replace(str("\n"),'')
		if End[1] == "AM":
			hhmm = End[0].split(':',2)
			if int(hhmm[0]) == 12:
				hhmm[0] = str(int(hhmm[0])+12)
				End[0] = ':'.join(hhmm)
			MCEnd.append(End[0])
		elif End[1] == "PM":
			hhmm = End[0].split(':',2)
			if int(hhmm[0]) < 12:
				hhmm[0] = str(int(hhmm[0])+12)
				End[0] = ':'.join(hhmm)
			MCEnd.append(End[0])
		values.clear()

	global TCName, TCStart, TCEnd
	TCName = []; TCStart = []; TCEnd = []
	Tuesday = open(TueFile,'r')
	Tclass = Tuesday.readlines()
	Tuesday.close()
	if "" in Tclass:
		Tclass.remove('')
	for i in Tclass:
		values = i.split(' ', 3)
		ClassName = values[0]
		ClassName = ClassName.replace('$_'," ")
		TCName.append(ClassName)
		StartTime = values[1]
		Start = StartTime.split('-',2)
		Start[0] = Start[0].replace('Start:','')
		if Start[1] == "AM":
			hhmm = Start[0].split(':',2)
			if int(hhmm[0]) == 12:
				hhmm[0] = str(int(hhmm[0])+12)
				Start[0] = ':'.join(hhmm)
			TCStart.append(Start[0])
		elif Start[1] == "PM":
			hhmm = Start[0].split(':',2)
			if int(hhmm[0]) < 12:
				hhmm[0] = str(int(hhmm[0])+12)
				Start[0] = ':'.join(hhmm)
			TCStart.append(Start[0])
		EndTime = values[2]
		End = EndTime.split('-',2)
		End[0] = End[0].replace('End:','')
		End[1] = End[1].replace(str("\n"),'')
		if End[1] == "AM":
			hhmm = End[0].split(':',2)
			if int(hhmm[0]) == 12:
				hhmm[0] = str(int(hhmm[0])+12)
				End[0] = ':'.join(hhmm)
			TCEnd.append(End[0])
		elif End[1] == "PM":
			hhmm = End[0].split(':',2)
			if int(hhmm[0]) < 12:
				hhmm[0] = str(int(hhmm[0])+12)
				End[0] = ':'.join(hhmm)
			TCEnd.append(End[0])
		values.clear()

	global WCName, WCStart, WCEnd
	WCName = []; WCStart = []; WCEnd = []
	Wednesday = open(WedFile,'r')
	Wclass = Wednesday.readlines()
	Wednesday.close()
	if "" in Wclass:
		Wclass.remove('')
	for i in Wclass:
		values = i.split(' ', 3)
		ClassName = values[0]
		ClassName = ClassName.replace('$_'," ")
		WCName.append(ClassName)
		StartTime = values[1]
		Start = StartTime.split('-',2)
		Start[0] = Start[0].replace('Start:','')
		if Start[1] == "AM":
			hhmm = Start[0].split(':',2)
			if int(hhmm[0]) == 12:
				hhmm[0] = str(int(hhmm[0])+12)
				Start[0] = ':'.join(hhmm)
			WCStart.append(Start[0])
		elif Start[1] == "PM":
			hhmm = Start[0].split(':',2)
			if int(hhmm[0]) < 12:
				hhmm[0] = str(int(hhmm[0])+12)
				Start[0] = ':'.join(hhmm)
			WCStart.append(Start[0])
		EndTime = values[2]
		End = EndTime.split('-',2)
		End[0] = End[0].replace('End:','')
		End[1] = End[1].replace(str("\n"),'')
		if End[1] == "AM":
			hhmm = End[0].split(':',2)
			if int(hhmm[0]) == 12:
				hhmm[0] = str(int(hhmm[0])+12)
				End[0] = ':'.join(hhmm)
			WCEnd.append(End[0])
		elif End[1] == "PM":
			hhmm = End[0].split(':',2)
			if int(hhmm[0]) < 12:
				hhmm[0] = str(int(hhmm[0])+12)
				End[0] = ':'.join(hhmm)
			WCEnd.append(End[0])
		values.clear()

	global ThCName, ThCStart, ThCEnd
	ThCName = []; ThCStart = []; ThCEnd = []
	Thursday = open(ThurFile,'r')
	Thclass = Thursday.readlines()
	Thursday.close()
	if "" in Thclass:
		Thclass.remove('')
	for i in Thclass:
		values = i.split(' ', 3)
		ClassName = values[0]
		ClassName = ClassName.replace('$_'," ")
		ThCName.append(ClassName)
		StartTime = values[1]
		Start = StartTime.split('-',2)
		Start[0] = Start[0].replace('Start:','')
		if Start[1] == "AM":
			hhmm = Start[0].split(':',2)
			if int(hhmm[0]) == 12:
				hhmm[0] = str(int(hhmm[0])+12)
				Start[0] = ':'.join(hhmm)
			ThCStart.append(Start[0])
		elif Start[1] == "PM":
			hhmm = Start[0].split(':',2)
			if int(hhmm[0]) < 12:
				hhmm[0] = str(int(hhmm[0])+12)
				Start[0] = ':'.join(hhmm)
			ThCStart.append(Start[0])
		EndTime = values[2]
		End = EndTime.split('-',2)
		End[0] = End[0].replace('End:','')
		End[1] = End[1].replace(str("\n"),'')
		if End[1] == "AM":
			hhmm = End[0].split(':',2)
			if int(hhmm[0]) == 12:
				hhmm[0] = str(int(hhmm[0])+12)
				End[0] = ':'.join(hhmm)
			ThCEnd.append(End[0])
		elif End[1] == "PM":
			hhmm = End[0].split(':',2)
			if int(hhmm[0]) < 12:
				hhmm[0] = str(int(hhmm[0])+12)
				End[0] = ':'.join(hhmm)
			ThCEnd.append(End[0])
		values.clear()

	global FCName, FCStart, FCEnd
	FCName = []; FCStart = []; FCEnd = []
	Friday = open(FriFile,'r')
	Fclass = Friday.readlines()
	Friday.close()
	if "" in Fclass:
		Fclass.remove('')
	for i in Fclass:
		values = i.split(' ', 3)
		ClassName = values[0]
		ClassName = ClassName.replace('$_'," ")
		FCName.append(ClassName)
		StartTime = values[1]
		Start = StartTime.split('-',2)
		Start[0] = Start[0].replace('Start:','')
		if Start[1] == "AM":
			hhmm = Start[0].split(':',2)
			if int(hhmm[0]) == 12:
				hhmm[0] = str(int(hhmm[0])+12)
				Start[0] = ':'.join(hhmm)
			FCStart.append(Start[0])
		elif Start[1] == "PM":
			hhmm = Start[0].split(':',2)
			if int(hhmm[0]) < 12:
				hhmm[0] = str(int(hhmm[0])+12)
				Start[0] = ':'.join(hhmm)
			FCStart.append(Start[0])
		EndTime = values[2]
		End = EndTime.split('-',2)
		End[0] = End[0].replace('End:','')
		End[1] = End[1].replace(str("\n"),'')
		if End[1] == "AM":
			hhmm = End[0].split(':',2)
			if int(hhmm[0]) == 12:
				hhmm[0] = str(int(hhmm[0])+12)
				End[0] = ':'.join(hhmm)
			FCEnd.append(End[0])
		elif End[1] == "PM":
			hhmm = End[0].split(':',2)
			if int(hhmm[0]) < 12:
				hhmm[0] = str(int(int(hhmm[0]))+12)
				End[0] = ':'.join(hhmm)
			FCEnd.append(End[0])
		values.clear()

if os.path.exists(defaultpath):
	if os.path.exists(customPath): customclass() #Run custom class function
else: getClasses(defaultpath); customclass() #If first time setup, run setup proce

# Load GUI
root = tk.Tk()

# Setting Defaults

root.title(title)
root.maxsize(350,800)
root.minsize(350,500)
root.resizable(False, False)
root.attributes('-alpha', 0.9)

currenttime = tk.StringVar()
currenttime.set("Loading...")
weekday1 = tk.StringVar()
weekday1.set("Loading...")
displayClasses = tk.StringVar()
displayClasses.set("0")
displayTimes = tk.StringVar()
displayTimes.set("0")
amntofhw = tk.StringVar()
amntofhw.set("Homework: Loading...")
CurClass = tk.StringVar()
root.config(background=bgcolor)
CurClass.set("Current Class N/A")

global alwaysontop
alwaysontop = False


def SortHomework():
	global homeworklist, hwFile
	if os.path.exists(hwFile):
		if not len(homeworklist) == 0:
			now = datetime.now()
			homeworkdue = []
			for j in homeworklist:
				index = homeworklist.index(j)
				b = j.split(' ')
				Date = b[4].split('/')
				w = b[5].split('-',2)
				Time = w[0].split(':')
				if w[1].upper() == "AM":
					if int(Time[0]) == 12:
						Time[0] = str(int(Time[0])+12)
				elif w[1].upper() == "PM":
					if int(Time[0]) < 12:
						Time[0] = str(int(Time[0])+12)
				duedate = datetime.datetime( int(Date[2]) +2000,
									int(Date[0]),
									int(Date[1]),
									int(Time[0]),
									int(Time[1]))
				TimeLeft = duedate - now
				try: homeworkdue[index] = TimeLeft
				except IndexError: homeworkdue.insert(index, TimeLeft)
			displayHomework.delete(0,'end')
			homeworkdue, homeworklist =[list(t) for t in zip(*sorted(zip(homeworkdue, homeworklist)))]
			for z2 in homeworklist:
				if '$_' in str(z2):
					displayHomework.insert('end',str(z2).replace('$_', ' '))
				else: displayHomework.insert('end',z2)

def AddHomework():
	global homeworklist, homeworkdue, dtsd
	def thing():
		global datedue, hwitem
		hwthing = e.multenterbox("Please enter the Name, Class, and Due Date of your assignment:", title, ['Name:', 'Class:', 'MM/DD/YY', 'HH:MM', 'AM/PM']) # todo Add calendar date picker
		hwitem = hwthing[:2]
		datedue = hwthing[2:]
	thing()
	now = datetime.now()
	dtsdCheck = now.strftime('%D')
	index = dtsd.index(dtsdCheck)
	daysOfWeek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
	if datedue[0].lower() in daysOfWeek:
		day = datedue[0].lower()
		day2 = str(now.strftime('%A')).lower()
		if day == day2:
			datedue[0] = dtsd[index]
		else:
			int1 = int(daysOfWeek.index(day2)) + 1
			int2 = int(daysOfWeek.index(day)) + 1
			int3 = int2 - int1
			datedue[0] = dtsd[index + int3]
	else:
		j = datedue[0].split('/')
		if len(str(j[0])) == 1:
			j[0] = f'0{j[0]}'
		if len(str(j[1])) == 1:
			j[1] = f'0{j[1]}'
		datedue[0] = f'{j[0]}/{j[1]}/{j[2]}'
	if datedue[0] in dtsd:pass
	else:
		msg('Please enter in a valid date!')
		thing()
	if datedue[1] == '':
		datedue[1] = '11:59'
	if datedue[2] == '':
		datedue[2] = 'PM'
	if '' in hwitem:
		AddHomework()
	homework = f'[{hwitem[1]}] {hwitem[0]} - Due {datedue[0]} {datedue[1]}-{datedue[2].upper()}'
	homework2 =  f"[{hwitem[1].replace(' ', '$_')}] {hwitem[0].replace(' ', '$_')} - Due {datedue[0]} {datedue[1]}-{datedue[2].upper()}"
	homeworklist.append(homework2)
	displayHomework.insert('end',homework)
	SaveHomework()

def RemoveHomework():
	global homeworklist, displayHomework
	value=str(displayHomework.get('active'))
	index = displayHomework.index('active')
	thing = homeworklist[index]
	displayHomework.delete(index)
	homeworklist.remove(thing)
	SaveHomework()

def SaveHomework():
	global hwFile, homeworklist
	from os import remove as delfile
	if os.path.exists(hwFile):
		delfile(hwFile)
	i = open(hwFile, 'x')
	i.close()
	i = open(hwFile, 'w', newline = '\n')
	for j in homeworklist:
		i.write(j+'\n')
	i.close()
	SortHomework()

def ReadHomework():
	global hwFile, homeworklist
	if os.path.exists(hwFile):
		i = open(hwFile, 'r')
		Homework = i.readlines()
		i.close()
		for j in Homework:
			b = split(j)
			if '\n' in b: b.remove('\n')
			j = ''.join(b)
			homeworklist.append(j)
			now = datetime.now()
			index = homeworklist.index(j)
			b = j.split(' ')
			b[0] = b[0].replace('$_', ' ')
			b[1] = b[1].replace('$_', ' ')
			Date = b[4].split('/')
			w = b[5].split('-',2)
			Time = w[0].split(':')
			if w[1].upper() == "AM":
				if int(Time[0]) == 12:
					Time[0] = str(int(Time[0])+12)
			elif w[1].upper() == "PM":
				if int(Time[0]) < 12:
					Time[0] = str(int(Time[0])+12)
			duedate = datetime.datetime( int(Date[2]) +2000,
								int(Date[0]),
								int(Date[1]),
								int(Time[0]),
								int(Time[1]))
			TimeLeft = duedate - now
			try: homeworkdue[index] = TimeLeft
			except IndexError: homeworkdue.insert(index, TimeLeft)
		if '' in homeworklist:
			homeworklist.remove('')

def EditHomework():
	global displayHomework, homeworklist
	value=str((displayHomework.get('active')))
	Index = displayHomework.index('active')
	b = homeworklist[Index].split(' ')
	b[0] = b[0].replace('[','').replace(']','')
	if '$_' in b[0]:
		b[0] = b[0].replace('$_', ' ')
	if '$_' in b[1]:
		b[1] = b[1].replace('$_', ' ')
	b.remove('-')
	b.remove('Due')
	j = b[3].split('-')
	b.remove(b[3])
	for i in j:
		b.append(i)
	t = e.multenterbox("Edit The Values",title,b)
	counter = 0
	for i in t:
		if i == '':
			t[counter] = b[counter]
		counter+=1

	homework = f'[{t[0]}] {t[1]} - Due {t[2]} {t[3]}-{t[4].upper()}'
	homework2 = f"[{t[0].replace(' ','$_')}] {t[1].replace(' ','$_')} - Due {t[2]} {t[3]}-{t[4].upper()}"
	homeworklist[Index] = homework2
	displayHomework.delete(Index)
	displayHomework.insert(Index, homework)
	SaveHomework()

def setbgcolor(bgcolor):
	root.config(background=bgcolor)
	lab.config(background=bgcolor)
	ab.config(background=bgcolor)
	lab1.config(background=bgcolor)
	lab2.config(background=bgcolor)
	lab3.config(background=bgcolor)
	hwadd.config(background=bgcolor)
	hwdel.config(background=bgcolor)
	displayHomework.config(background=bgcolor)
	sep1.config(background=bgcolor)
	sayhw.config(background=bgcolor)

def setfgcolor(fgcolor):
	lab.config(fg=fgcolor)
	ab.config(fg=fgcolor)
	lab1.config(fg=fgcolor)
	lab2.config(fg=fgcolor)
	lab3.config(fg=fgcolor)
	sep.config(background=fgcolor)
	hwadd.config(fg=fgcolor)
	hwdel.config(fg=fgcolor)
	displayHomework.config(fg=fgcolor)
	sep2.config(background=fgcolor)
	sayhw.config(fg=fgcolor)

def Config():
	global configFile, values, bgcolor, fgcolor, winopacity, alwaysontop
	if len(winopacity) == 0: winopacity.append(100)
	values = [f'bgcolor={bgcolor}', f'fgcolor={fgcolor}', f'winopacity={str(winopacity[0])}', f'alwaysontop={str(alwaysontop)}']
	from os import remove as delfile
	if os.path.exists(configFile):
		delfile(configFile)
	i = open(configFile, 'x')
	i.close()
	i = open(configFile,'w', newline = '\n')
	for j in values:
		i.write(j+'\n')
	i.close()
	values = []

def split(word):
	return list(word)

def ConfigRead():
	global configFile, values, bgcolor, fgcolor, winopacity, alwaysontop
	i = open(configFile, 'r')
	values = i.readlines()
	i.close()
	for j in values:
		things = j.split('=')
		thing = split(things[1])
		if '\n' in thing: thing.remove('\n')
		things[1] = ''.join(thing)
		if things[0] == 'bgcolor':
			bgcolor = things[1]
			setbgcolor(bgcolor)
		elif things[0] == 'fgcolor':
			fgcolor = things[1]
			setfgcolor(fgcolor)
		elif things[0] == 'winopacity':
			winopacity = [int(things[1])]
			root.attributes('-alpha', str(winopacity[0] / 100))##Try now
		elif things[0] == 'alwaysontop':
			alwaysontop = things[1]
			if alwaysontop == 'True':
				alwaysontop = True
				root.call('wm', 'attributes', '.', '-topmost', '1')
			else:
				alwaysontop = False
				root.call('wm', 'attributes', '.', '-topmost', '0')

def alwaystop1():
	global alwaysontop
	if alwaysontop:
		root.call('wm', 'attributes', '.', '-topmost', '0')
		alwaysontop = False
	else:
		root.call('wm', 'attributes', '.', '-topmost', '1')
		alwaysontop = True
	Config()

def transparancy():
	global winopacity
	winopacity = e.multenterbox("Type in the opacity percent.", title, fields=['Opacity'])
	if winopacity == None: pass
	else:
		root.attributes('-alpha', str(int(winopacity[0]) / 100))
		Config()

lab1 = tk.Label(root, textvariable=weekday1, background="#FFFFFF", fg="black", font=("Arial Bold", 35))
lab1.pack()

lab3 = tk.Label(root, textvariable=currenttime, background="#FFFFFF", fg="black", font=("Arial Bold", 15))
lab3.pack(side="top")

sep = tk.PanedWindow(root, orient="horizontal", width=200, background="black")
sep.pack(pady=5)

lab2 = tk.Label(root, textvariable=CurClass, background="#FFFFFF", fg="black", font=("Arial Bold", 10))
lab2.pack(side="top")

from os.path import exists as exist
if exist(hwFile): ReadHomework()

sep1 = tk.PanedWindow(root, orient="horizontal", width=200, background="white")
sep1.pack(pady=5)

sep2 = tk.PanedWindow(root, orient="horizontal", width=600, height=1)
sep2.config(background="#A0A0A0")
sep2.pack(pady=0, padx=5)

sayhw = tk.Label(root, textvariable=amntofhw, background='white', fg='black', font=("Arial", 10))
sayhw.pack(side='top', anchor='w', padx='0', pady='0')

displayHomework = tk.Listbox(root, background='#FFFFFF', fg='#000000', borderwidth='0', highlightthickness='0')
displayHomework.pack(side="top", expand=0, anchor='s', fill='x', padx='6', pady='0')

hwadd = tk.Button(root, text='Add Assignment', background='#FFFFFF', fg='#000000', command=AddHomework)
hwadd.pack(side="top", fill='x', padx='5')
hwdel = tk.Button(root, text='Remove Assignment', background='#FFFFFF', fg='#000000', command=RemoveHomework)
hwdel.pack(side="top", fill='x', padx='5')

for item in homeworklist:
	displayHomework.insert('end', item.replace('$_', ' '))
SortHomework()

lab = tk.Label(root, width='29', textvariable=displayClasses, anchor='w', justify="left", background="#FFFFFF", fg="black", font=("Arial", 10))
lab.pack(side="left", anchor='nw', padx='5', pady='10')

ab = tk.Label(root, textvariable=displayTimes, anchor='e', justify="center", background="#FFFFFF", fg="black", font=("Arial", 10))
ab.pack(side="right", anchor='ne', padx='5', pady='10')

if os.path.exists(configFile): ConfigRead()

def bgcolor1():
	global bgcolor
	bgcolor = e.multenterbox("Type in the HEX value of a background color (Ex: FFFFFF)", title, ['#'])
	bgcolor = f'#{str(bgcolor[0])}'
	setbgcolor(bgcolor)
	Config()

def fgcolor1():
	global fgcolor
	fgcolor = e.multenterbox("Type in the HEX value of a foreground color (Ex: FFFFFF)", title, ['#'])
	fgcolor = f'#{str(fgcolor[0])}'
	setfgcolor(fgcolor)
	Config()

def darkmode():
	global bgcolor, fgcolor
	fgcolor = '#FFFFFF'
	bgcolor = '#232323'
	setbgcolor(bgcolor)
	setfgcolor(fgcolor)
	Config()

def lightmode():
	global bgcolor, fgcolor
	fgcolor = '#000000'
	bgcolor = '#FFFFFF'
	setbgcolor(bgcolor)
	setfgcolor(fgcolor)
	Config()

def dayOfWeek(weekdaything):
	global weekdayNoCustom, weekday
	weekdaything = str(weekdaything)
	if weekdaything == 'Current':
		weekdayNoCustom = True
	else:
		weekday = weekdaything
		weekdayNoCustom = False
		weekday1.set(weekdaything)

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)

filemenu.add_command(label="Background color", command=bgcolor1)
filemenu.add_command(label="Foreground color", command=fgcolor1)
filemenu.add_command(label="Toggle always on top", command=alwaystop1)
filemenu.add_command(label="Transparency", command=transparancy)
filemenu.add_separator()
filemenu.add_command(label="Dark Mode", command=darkmode)
filemenu.add_command(label="Light Mode", command=lightmode)

#filemenu.add_separator()

menubar.add_cascade(label="Window", menu=filemenu)

hwmenu = tk.Menu(menubar, tearoff=0)
hwmenu.add_command(label="Add", command=AddHomework)
hwmenu.add_command(label="Remove", command=RemoveHomework)
hwmenu.add_separator()
hwmenu.add_command(label='Edit', command=EditHomework)

menubar.add_cascade(label="Homework", menu=hwmenu)

day = tk.Menu(menubar, tearoff=0)

day.add_command(label='Monday',command=lambda: dayOfWeek('Monday'))
day.add_command(label='Tuesday',command=lambda: dayOfWeek('Tuesday'))
day.add_command(label='Wednesday',command=lambda: dayOfWeek('Wednesday'))
day.add_command(label='Thursday',command=lambda: dayOfWeek('Thursday'))
day.add_command(label='Friday',command=lambda: dayOfWeek('Friday'))
day.add_separator()
day.add_command(label='Current',command=lambda: dayOfWeek('Current'))

menubar.add_cascade(label='Day', menu=day)

other = tk.Menu(menubar, tearoff=0)
other.add_command(label="Exit", command=lambda: root.destroy(), accelerator="Alt+F4")

menubar.add_cascade(label="Help", menu=other)


root.config(menu=menubar)

def clock():
	global weekday
	now = datetime.now()
	weekdaytime = datetime.now().strftime("%A")
	time = datetime.now().strftime("%I:%M:%S %p | %D")
	if time[0] == "0":
		time = time[1:]
	time = f"Time: {time}"
	currenttime.set(time)
	if weekdayNoCustom:
		weekday1.set(weekdaytime)
		weekday = weekdaytime
	dts12 = [dt.strftime('%I:%M%p').lower().replace('m', '') for dt in
	   datetime_range(datetime.datetime(2016, 1, 1), datetime.datetime(2016, 1, 2),
	   timedelta(minutes=1))]
	dts24 = [dt.strftime('%H:%M') for dt in
	   datetime_range(datetime.datetime(2016, 1, 1), datetime.datetime(2016, 1, 2),
	   timedelta(minutes=1))]

	def Schedule(Name, Start, End):
		global allclasses, alltimes
		allclasses = []; alltimes = []
		counter = 0
		for i in Name:
			start = dts12[int(dts24.index(Start[counter]))]
			end = dts12[int(dts24.index(End[counter]))]
			allclasses.append(f'{i}'); alltimes.append(f'{start} - {end}')
			counter +=1
		counter = 1; counter2 = 0
		for i in allclasses:
			allclasses[counter2] = f"{counter}. {i}"
			counter +=1; counter2 +=1
		allclasses = '\n'.join(str(elem) for elem in allclasses)
		alltimes = '\n'.join(str(elem) for elem in alltimes)
		displayClasses.set(allclasses)
		displayTimes.set(alltimes)
		global homeworklist
		if len(homeworklist) == 0:
			amntofhw.set(f'No homework assignments!')
			hwdel.config(state='disabled')
		else:
			if len(homeworklist) == 1: grammars = ''
			else: grammars = 's'
			amntofhw.set(f'Homework: {str(len(homeworklist))} assignment{grammars}.')
			hwdel.config(state='normal')

	def CurrentPeriod(Name, Start,End):
		for i in Name:
			index = Name.index(i)
			s = Start[index].split(':', 2)
			h = End[index].split(':', 2)
			if timedelta(hours=now.hour,minutes=now.minute) > timedelta(hours=int(s[0]),minutes=int(s[1])):
				if timedelta(hours=now.hour, minutes=now.minute) < timedelta(hours=int(h[0]),minutes=int(h[1])):
					CurClass.set(i)
					TimeLeft = timedelta(hours=int(h[0]),minutes=int(h[1])) - timedelta(hours=now.hour, minutes=now.minute)
					c = TimeLeft.seconds / 60
					s = str(c).split('.',2)
					if str(s[0]) == '1': plural = ''
					else: plural = 's'
					CurClass.set(f"{i} - {s[0]} minute{plural} left")

	if weekday == "Monday": CurrentPeriod(MCName, MCStart, MCEnd); Schedule(MCName, MCStart, MCEnd)
	if weekday == "Tuesday": CurrentPeriod(TCName, TCStart, TCEnd); Schedule(TCName, TCStart, TCEnd)
	if weekday == "Wednesday": CurrentPeriod(WCName, WCStart, WCEnd); Schedule(WCName, WCStart, WCEnd)
	if weekday == "Thursday": CurrentPeriod(ThCName, ThCStart, ThCEnd); Schedule(ThCName, ThCStart, ThCEnd)
	if weekday == "Friday": CurrentPeriod(FCName, FCStart, FCEnd); Schedule(FCName, FCStart, FCEnd)
	elif weekday in ("Saturday", "Sunday"): allclasses = 'No School'; alltimes = 'N/A'

	for j in homeworklist:
		index = homeworklist.index(j)
		b = j.split(' ')
		Date = b[4].split('/')
		w = b[5].split('-',2)
		Time = w[0].split(':')
		if w[1].upper() == "AM":
			if int(Time[0]) == 12:
				Time[0] = str(int(Time[0])+12)
		elif w[1].upper() == "PM":
			if int(Time[0]) < 12:
				Time[0] = str(int(Time[0])+12)
		duedate = datetime.datetime( int(Date[2]) +2000,
							int(Date[0]),
							int(Date[1]),
							int(Time[0]),
							int(Time[1]))
		if not duedate >= now:
			if not '[LATE]' in displayHomework.get(index):
				displayHomework.delete(index)
				displayHomework.insert(index, str(str(j).replace('$_', ' ') + ' [LATE]'))
	root.after(200, clock)

clock()

root.mainloop()
