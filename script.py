import pandas as pd
import sys, os,json
import pip
import importlib.metadata

data= pd.read_csv('requirements.txt',delimiter='==',header=None,skiprows=2,engine='python',skipfooter=2)

def installdependencies(name,version):
		os.system("sudo pip install "+str(name)+"=="+str(version))

def checkanyuninstalled(data):
	dists = importlib.metadata.distributions()
	name=[]
	for dist in dists:
		name.append(dist.metadata["Name"])

	for key in range(len(data)):
		uninstalled = []
		if data[0][key] not in name:
			uninstalled.append(data[0][key])
	if uninstalled:
		print(uninstalled)
	else:
		print("Successfully installed all libraries")

for i in range(len(data)):
	try:
		installdependencies(data[0][i],data[1][i][:-1])
	except:
		print(str(data[0][i]+" library is not installed successfully."))
		
checkanyuninstalled(data)
		
