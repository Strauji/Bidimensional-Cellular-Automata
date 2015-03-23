#############
import time
import random
############ Variables/inits
global mapc
global x
global y
global turns
global life
global updTime
mapc = {}
updTime = 0.0
x = 0
y = 0
life = 0
turns = 0
############################# Here, we can see a way to handle a "2d array(huehue)"
def cellmap_initialize(x,y):
	for i in range(0,x+1):
		for j in range(0,y+1):
			mapc[str(i)+','+str(j)] = '-'
############### Return the map
def map_get():
	global x
	global y
	ret = ''
	for i in range(0,y+1):
		for j in range(0,x+1):
			ret = ret + mapc[str(j)+','+str(i)]
		ret = ret + '\n'
	return ret
################# Initialize the 'Game'
def life_init():
	global x
	global y
	global updTime
	times = 0
	x = int(raw_input('Enter X plane size:'))
	y = int(raw_input('Enter Y plane size:'))
	while (updTime < 0.1):
		updTime = float(raw_input('Enter the update time(0.1 min):'))
	while (times <= 0):
		times = int(raw_input('Enter how much shapes you want to create:'))
	cellmap_initialize(x,y)
	for i in range(0,times):
		cX = int(raw_input('Enter a start(' + str(i+1) + ') position X:'))
		cY = int(raw_input('Enter a start(' + str(i+1) + ') position Y:'))
	
	
		done = False
		while done == False:
			cType = raw_input('Enter a cell type[Star,HLine,VLine,T,V,+]:')
			try:
				if cType == 'Star':
					cell_create(str(cX+1)+','+str(cY+1))
					cell_create(str(cX+1)+','+str(cY-1))
					cell_create(str(cX-1)+','+str(cY+1))
					cell_create(str(cX-1)+','+str(cY-1))
					cell_create(str(cX)+','+str(cY))
					done = True
				if cType == 'HLine':
					cell_create(str(cX+1)+','+str(cY))
					cell_create(str(cX+2)+','+str(cY))
					cell_create(str(cX-1)+','+str(cY))
					cell_create(str(cX-2)+','+str(cY))
					cell_create(str(cX)+','+str(cY))
					done = True
				if cType == 'VLine':
					cell_create(str(cX)+','+str(cY+1))
					cell_create(str(cX)+','+str(cY-1))
					cell_create(str(cX)+','+str(cY+2))
					cell_create(str(cX)+','+str(cY-2))
					cell_create(str(cX)+','+str(cY))
					done = True
				if cType == 'T':
					cell_create(str(cX-1)+','+str(cY))
					cell_create(str(cX+1)+','+str(cY)) 
					cell_create(str(cX)+','+str(cY)) 
					cell_create(str(cX)+','+str(cY+1))
					cell_create(str(cX)+','+str(cY+2))			
					done = True
				if cType == 'V':
					cell_create(str(cX+1)+','+str(cY+1))
					cell_create(str(cX+2)+','+str(cY+2))
					cell_create(str(cX-1)+','+str(cY-1))
					cell_create(str(cX-2)+','+str(cY-2))
					cell_create(str(cX)+','+str(cY))
					done = True
				if cType == '+':
					cell_create(str(cX-1)+','+str(cY))					
					cell_create(str(cX+1)+','+str(cY))
					cell_create(str(cX)+','+str(cY+1))
					cell_create(str(cX)+','+str(cY-1))
					cell_create(str(cX)+','+str(cY))
					done = True
			except:
				print 'Something arent right... Trying again...'
				pass
####################### Check if some space have some kinda of life
def isalive_check(wx,wy):
	try:
		if mapc[str(wx)+','+str(wy)] == 'C':
			return True
	except:
		pass
	return False
####################### Look up to find free spaces on a 5x5 neighborhood
def freespace_check(wx,wy):
	if not isalive_check(wx+2,wy):	
		return str(wx+2)+','+str(wy)
	if not isalive_check(wx-2,wy):	
		return str(wx-2)+','+str(wy)
	if not isalive_check(wx,wy+2):	
		return str(wx)+','+str(wy+2)
	if not isalive_check(wx,wy-2):	
		return str(wx)+','+str(wy-2)
	if not isalive_check(wx+2,wy+2):	
		return str(wx+2)+','+str(wy-2)
	if not isalive_check(wx-2,wy-2):	
		return str(wx-2)+','+str(wy-2)
	if not isalive_check(wx-2,wy+2):	
		return str(wx-2)+','+str(wy+2)
	if not isalive_check(wx+2,wy-2):	
		return str(wx+2)+','+str(wy-2)
	if not isalive_check(wx+1,wy+2):	
		return str(wx+1)+','+str(wy-2)
	if not isalive_check(wx-1,wy-2):	
		return str(wx-1)+','+str(wy-2)
	if not isalive_check(wx-1,wy+2):	
		return str(wx-1)+','+str(wy+2)
	if not isalive_check(wx+1,wy-2):	
		return str(wx+1)+','+str(wy-2)
	if not isalive_check(wx+2,wy+1):	
		return str(wx+2)+','+str(wy+1)
	if not isalive_check(wx-2,wy-1):	
		return str(wx-2)+','+str(wy-1)
	if not isalive_check(wx-2,wy+1):	
		return str(wx-2)+','+str(wy+1)
	if not isalive_check(wx+2,wy-1):	
		return str(wx+2)+','+str(wy-1)
	if not isalive_check(wx+1,wy):	
		return str(wx+1)+','+str(wy)
	if not isalive_check(wx-1,wy):	
		return str(wx-1)+','+str(wy)
	if not isalive_check(wx,wy+1):	
		return str(wx)+','+str(wy+1)
	if not isalive_check(wx,wy-1):	
		return str(wx)+','+str(wy-1)
	if not isalive_check(wx+1,wy+1):	
		return str(wx+1)+','+str(wy-1)
	if not isalive_check(wx+1,wy-1):	
		return str(wx-1)+','+str(wy+1)
	if not isalive_check(wx-1,wy+1):	
		return str(wx+1)+','+str(wy+1)
	if not isalive_check(wx-1,wy-1):	
		return str(wx-1)+','+str(wy-1)
	return 'none'
###################### Look up to find alive cells on a 5x5 neighborhood
def alivecell_check(wx,wy):
	if isalive_check(wx+2,wy):	
		return str(wx+2)+','+str(wy)
	if isalive_check(wx-2,wy):	
		return str(wx-2)+','+str(wy)
	if isalive_check(wx,wy+2):	
		return str(wx)+','+str(wy+2)
	if isalive_check(wx,wy-2):	
		return str(wx)+','+str(wy-2)
	if isalive_check(wx+2,wy+2):	
		return str(wx+2)+','+str(wy-2)
	if isalive_check(wx-2,wy-2):	
		return str(wx-2)+','+str(wy-2)
	if isalive_check(wx-2,wy+2):	
		return str(wx-2)+','+str(wy+2)
	if isalive_check(wx+2,wy-2):	
		return str(wx+2)+','+str(wy-2)
	if isalive_check(wx+1,wy+2):	
		return str(wx+1)+','+str(wy-2)
	if isalive_check(wx-1,wy-2):	
		return str(wx-1)+','+str(wy-2)
	if isalive_check(wx-1,wy+2):	
		return str(wx-1)+','+str(wy+2)
	if isalive_check(wx+1,wy-2):	
		return str(wx+1)+','+str(wy-2)
	if isalive_check(wx+2,wy+1):	
		return str(wx+2)+','+str(wy+1)
	if isalive_check(wx-2,wy-1):	
		return str(wx-2)+','+str(wy-1)
	if isalive_check(wx-2,wy+1):	
		return str(wx-2)+','+str(wy+1)
	if isalive_check(wx+2,wy-1):	
		return str(wx+2)+','+str(wy-1)
	if isalive_check(wx+1,wy):	
		return str(wx+1)+','+str(wy)
	if isalive_check(wx-1,wy):	
		return str(wx-1)+','+str(wy)
	if isalive_check(wx,wy+1):	
		return str(wx)+','+str(wy+1)
	if isalive_check(wx,wy-1):	
		return str(wx)+','+str(wy-1)
	if isalive_check(wx+1,wy+1):	
		return str(wx+1)+','+str(wy-1)
	if isalive_check(wx+1,wy-1):	
		return str(wx-1)+','+str(wy+1)
	if isalive_check(wx-1,wy+1):	
		return str(wx+1)+','+str(wy+1)
	if isalive_check(wx-1,wy-1):	
		return str(wx-1)+','+str(wy-1)
	return 'none'
############################ remove a 5x5 neighborhood, where wx and wy r the 0-groud
def neighborhood_remove(wx,wy):
	try:
		 cell_remove(wx+2,wy)
	except:
		pass
	try:
		 cell_remove(wx-2,wy)
	except:
		pass
	try:
		 cell_remove(wx,wy-2)
	except:
		pass
	try:
		 cell_remove(wx,wy+2)
	except:
		pass
	try:
		 cell_remove(wx+2,wy+2)
	except:
		pass
	try:
		 cell_remove(wx-2,wy-2)
	except:
		pass
	try:
		 cell_remove(wx+2,wy-2)
	except:
		pass
	try:
		 cell_remove(wx-2,wy+2)
	except:
		pass
	try:
		 cell_remove(wx+2,wy+1)
	except:
		pass
	try:
		 cell_remove(wx-2,wy+1)
	except:
		pass
	try:
		 cell_remove(wx+2,wy-1)
	except:
		pass
	try:
		 cell_remove(wx-2,wy-1)
	except:
		pass
	try:
		 cell_remove(wx+1,wy+2)
	except:
		pass
	try:
		 cell_remove(wx-1,wy+2)
	except:
		pass
	
	try:
		 cell_remove(wx+1,wy-2)
	except:
		pass
	try:
		 cell_remove(wx-1,wy-2)
	except:
		pass
	try:
		 cell_remove(wx,wy)
	except:
		pass
	try:
		 cell_remove(wx+1,wy)
	except:
		pass
	try:
		 cell_remove(wx-1,wy)
	except:
		pass
	try:
		 cell_remove(wx,wy+1)
	except:
		pass
	try:
		 cell_remove(wx,wy-1)
	except:
		pass
	try:
		 cell_remove(wx-1,wy-1)
	except:
		pass
	try:
		 cell_remove(wx+1,wy+1)
	except:
		pass
	try:
 		 cell_remove(wx-1,wy+1)
	except:
		pass
	try:
		 cell_remove(wx+1,w-1)
	except:
		pass
########################### Check the cell neighborhood
def neighborhood_check(wx,wy):
		nLevel = 1 # at this moment i don't remind why i've seted this var to 1, but if aren't broken, don't fix 
		try:
			if mapc[str(wx+2)+','+str(wy)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-2)+','+str(wy)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx)+','+str(wy+2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx)+','+str(wy-2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx+1)+','+str(wy)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-1)+','+str(wy)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx)+','+str(wy+1)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx)+','+str(wy-1)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx+1)+','+str(wy+1)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx+1)+','+str(wy-1)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-1)+','+str(wy+1)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-1)+','+str(wy-1)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-2)+','+str(wy+2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-1)+','+str(wy+2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx)+','+str(wy+2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx+1)+','+str(wy+2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx+2)+','+str(wy+2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-2)+','+str(wy+-2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx+2)+','+str(wy-2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-2)+','+str(wy+2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx+2)+','+str(wy+1)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx+2)+','+str(wy)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx+2)+','+str(wy-1)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx+1)+','+str(wy+2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx)+','+str(wy+2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-1)+','+str(wy+2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-2)+','+str(wy+1)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-2)+','+str(wy)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-2)+','+str(wy-1)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx+1)+','+str(wy-2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx)+','+str(wy-2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		try:
			if mapc[str(wx-1)+','+str(wy-2)] == 'C':
				nLevel = nLevel+1
		except:
			pass
		return nLevel
################### remove a cell on a POG'ed 2D array
def cell_remove(wx,wy):
	mapc[str(wx)+','+str(wy)] = '-'
##################### yep, the name is TOO MUCH intuitive
def fcell_remove(w):
	mapc[w] = '-'
#################### create a cell on a POG'ed 2D array
def cell_create(w):
	mapc[w] = 'C'
############## Update map function, removing and creating cell		
def update():
	global life
	global turns
	global x
	global y
	d = 1
	for i in range(0,y+1):
		for j in range(0,x+1):
			d = d * (-1)
			if isalive_check(j,i):
					
				if neighborhood_check(j,i) <= 6 and  neighborhood_check(j,i) > 1 :
					cell_create(freespace_check(j,i))
					life = life+1
				elif neighborhood_check(j,i) > 6:
					fcell_remove(alivecell_check(j,i))
				else:
					neighborhood_remove(j,i)	
	if life == 0:
		print 'The organism has been destroyed'
		print 'Life time ' + str(turns)
		quit()
	else:
		life = 0
		turns = turns +1

#######################################################################################################################
################################################### BELLOW THE MAGIC HAPPENS... #######################################
#######################################################################################################################
life_init() #Call Game init
############ Keep the map updating
while True:
	print map_get()
	update()
	time.sleep(updTime)




######################## OMG now i realize that i luv cells... <3
