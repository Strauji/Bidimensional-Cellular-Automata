import time
import random
############### This section define the global variables
global mapc
mapc = {}
global x
x = 20
global y
y =20
turns = 0
############### Here, we can see a way to handle a "2d array(huehue)"
def initialize_CellMap(x,y):
	for i in range(0,x+1):
		for j in range(0,y+1):
			mapc[str(i)+','+str(j)] = '-'
############## Return the map
def get_Map():
	global x
	global y
	ret = ''
	for i in range(0,y+1):
		for j in range(0,x+1):
			ret = ret + mapc[str(j)+','+str(i)]
		ret = ret + '\n'
	return ret
################ Initialize the 'Game'
def init_life():
	global x
	global y
	x = int(raw_input('Enter X plane size:'))
	y = int(raw_input('Enter Y plane size:'))
	cX = int(raw_input('Enter a start position X:'))
	cY = int(raw_input('Enter a start position Y:'))
	
	initialize_CellMap(x,y)
	done = False
	while done == False:
		cType = raw_input('Enter a cell type[Star,HLine,VLine,T,V]:')
		try:
			if cType == 'Star':
				cell_Create(str(cX+1)+','+str(cY+1))
				cell_Create(str(cX+1)+','+str(cY-1))
				cell_Create(str(cX-1)+','+str(cY+1))
				cell_Create(str(cX-1)+','+str(cY-1))
				cell_Create(str(cX)+','+str(cY))
				done = True
			if cType == 'HLine':
				cell_Create(str(cX+1)+','+str(cY))
				cell_Create(str(cX+2)+','+str(cY))
				cell_Create(str(cX-1)+','+str(cY))
				cell_Create(str(cX-2)+','+str(cY))
				cell_Create(str(cX)+','+str(cY))
				done = True
			if cType == 'VLine':
				cell_Create(str(cX)+','+str(cY+1))
				cell_Create(str(cX)+','+str(cY-1))
				cell_Create(str(cX)+','+str(cY+2))
				cell_Create(str(cX)+','+str(cY-2))
				cell_Create(str(cX)+','+str(cY))
				done = True
			if cType == 'T':
				cell_Create(str(cX-1)+','+str(cY))
				cell_Create(str(cX+1)+','+str(cY)) 
				cell_Create(str(cX)+','+str(cY)) 
				cell_Create(str(cX)+','+str(cY-1))
				cell_Create(str(cX)+','+str(cY-2))			
				done = True
			if cType == 'V':
				cell_Create(str(cX+1)+','+str(cY+1))
				cell_Create(str(cX+2)+','+str(cY+2))
				cell_Create(str(cX-1)+','+str(cY-1))
				cell_Create(str(cX-2)+','+str(cY-2))
				cell_Create(str(cX)+','+str(cY))

			
		except:
			print 'Something arent right... Trying again...'
			pass

###################### Check if some space have some kinda of life
def check_life(wx,wy):
	try:
		if mapc[str(wx)+','+str(wy)] == 'C':
			return True
	except:
		pass
	return False

###################### Look up to find free spaces
def check_free(wx,wy):
	if not check_life(wx+1,wy):	
		return str(wx+1)+','+str(wy)
	if not check_life(wx-1,wy):	
		return str(wx-1)+','+str(wy)
	if not check_life(wx,wy+1):	
		return str(wx)+','+str(wy+1)
	if not check_life(wx,wy-1):	
		return str(wx)+','+str(wy-1)
	if not check_life(wx+1,wy+1):	
		return str(wx+1)+','+str(wy-1)
	if not check_life(wx+1,wy-1):	
		return str(wx-1)+','+str(wy+1)
	if not check_life(wx-1,wy+1):	
		return str(wx+1)+','+str(wy+1)
	if not check_life(wx-1,wy-1):	
		return str(wx-1)+','+str(wy-1)
	return 'none'
########################### Remove 3x3 cells, where wx and wy is the 0-ground
def remove_neighbor(wx,wy):
	try:
		 cell_Remove(wx,wy)
	except:
		pass
	try:
		 cell_Remove(wx+1,wy)
	except:
		pass
	try:
		 cell_Remove(wx-1,wy)
	except:
		pass
	try:
		 cell_Remove(wx,wy+1)
	except:
		pass
	try:
		 cell_Remove(wx,wy-1)
	except:
		pass
	try:
		 cell_Remove(wx-1,wy-1)
	except:
		pass
	try:
		 cell_Remove(wx+1,wy+1)
	except:
		pass
	try:
 		 cell_Remove(wx-1,wy+1)
	except:
		pass
	try:
		 cell_Remove(wx+1,w-1)
	except:
		pass
########################## Check the cell neighbor
def check_neighbor(wx,wy):
	
		nLevel = 1
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
		return nLevel
################### remove a cell on a POG'ed 2D array
def cell_Remove(wx,wy):
	mapc[str(wx)+','+str(wy)] = '-'

################### Create a cell on a POG'ed 2D array
def cell_Create(w):
	
	mapc[w] = 'C'
	
############# Update map function, removing and creating cell		
def update():
	global x
	global y
	d = 1
	for i in range(0,y+1):
		for j in range(0,x+1):
			d = d * (-1)
			if check_life(j,i):
				if check_neighbor(j,i) >= 2 :
					cell_Create(check_free(j,i+d))
					cell_Create(check_free(j+d,i))
					cell_Remove(j,i)
				else:
					remove_neighbor(j,i)
				if check_neighbor(j,i) >= 6:
					remove_neighbor(j,i)
				

				
	
					

init_life() #Call Game init


#####Keep the map updating
while True:
	
	print get_Map()
	update()
	time.sleep(0.7)




######################## OMG now i realize that i luv cells... <3
