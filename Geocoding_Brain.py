import json
import requests 



class Geocoder():

	def __init__(self,address):
		self.address = address
		self.prams = {
			'key' : '',
			'address': self.address
			}

		self.base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

		self.response = requests.get(self.base_url,params=self.prams).json()
		#print(self.address)

		if self.response['status'] == 'OK':
			self.geometry = self.response['results'][0]['geometry']
			self.lat,self.lng = self.converter(self.geometry['location']['lat'],self.geometry['location']['lng'])
		
	def converter(self,*args):
		args=list(args)
		direc=[];degress=[];minutes=[];seconds=[]
		if args[0]>0:
			direc+=['N',]
		else:
			args[0]=args[0]*(-1)
			direc+=['S',]
		if args[0]>0:
			direc+=['E',]
		else:
			args[1]=args[1]*(-1)
			direc+=['W',]
		degress=[int(args[0]),int(args[1])]
		for i in range(2):
			args[i]=(args[i]%degress[i])*60

		minutes=[int(args[0]),int(args[1])]
		for i in range(2):
			args[i]=(args[i]%minutes[i])*60

		seconds=[int(args[0]),int(args[1])]
		#print(degress,minutes,seconds,direc)
		lat=str(degress[0])+'°'+str(minutes[0])+"'"+str(seconds[0])+'"'+direc[0]
		lng=str(degress[1])+'°'+str(minutes[1])+"'"+str(seconds[1])+'"'+direc[1]

		return lat,lng

