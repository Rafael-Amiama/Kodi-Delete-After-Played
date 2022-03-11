import xbmcaddon
import xbmcgui
import xbmc
import xbmcvfs
import os
import sys
import time
from time import sleep


DeviceType = "Unknown"
if os.path.isdir('Android/data/org.xbmc.kodi/files'):
	DeviceType = "Android"
	FolderStructure = "Android/data/org.xbmc.kodi/files/."
elif os.path.isdir('/Users/$USER/Library/Application Support'):
	DeviceType = "MAC"
	FolderStructure = "/Users/$USER/Library/Application Support/"
elif os.path.isdir('/private/var/mobile/Library/Preferences'):
	DeviceType = "iOS"
	FolderStructure = "/private/var/mobile/Library/Preferences/"
elif os.path.isdir("/home/pi/.kodi"):
	DeviceType = "Raspberry Pi"
	FolderStructure = "/home/pi/."
elif os.path.isdir('/storage/emulated/0/Android/data/org.xbmc.kodi/files'):
	DeviceType = "FireTV"
	FolderStructure = '/storage/emulated/0/Android/data/org.xbmc.kodi/files/.'
elif os.path.isdir('C:\\Users\\'):
	DeviceType = "Windows"
	fpath = xbmcvfs.translatePath('special://home') 
	HomePath = fpath[0:-1]
	FolderStructure = HomePath




dialog = xbmcgui.Dialog()
DeviceOS = os.environ.get("OS")

if DeviceType != "Windows":
	startAutomatically = xbmcvfs.exists(FolderStructure + "kodi/userdata/autoexec.py")
	if startAutomatically == False:
		My_variable = "import xbmc\nxbmc.executebuiltin('RunScript(script.service.deleteafterplayed)')"
		write2File = open(FolderStructure + "kodi/userdata/autoexec.py","w") # "a" means append to the end of the file. "w" over writes the entire file with new input.
		write2File.write (My_variable), # this comma at the end prevents from creating a new line inside the text file.
		write2File.close()
elif DeviceType == "Windows":
	startAutomatically = xbmcvfs.exists(FolderStructure + "\\userdata\\autoexec.py")
	if startAutomatically == False:
		My_variable = "import xbmc\nxbmc.executebuiltin('RunScript(script.service.deleteafterplayed)')"
		write2File = open(FolderStructure + "\\userdata\\autoexec.py","w") # "a" means append to the end of the file. "w" over writes the entire file with new input.
		write2File.write (My_variable), # this comma at the end prevents from creating a new line inside the text file.
		write2File.close()




def selected():
	while True:
		sleep(2.0)
		beenPlayed = xbmc.getInfoLabel('ListItem.Label')
		if ".mp4" in beenPlayed:
			
			whatPath = xbmc.getInfoLabel('ListItem.FolderPath')
			if "Youtube Videos" in whatPath:
				ExistsFile = xbmcvfs.exists(whatPath)
				if ExistsFile == True:
					
					wasPlayed = xbmc.getInfoLabel('ListItem.PlayCount')
					if wasPlayed == "1":
						dialog.notification("Youtube Video was Played:", "Tagging for Deletion.","", 1000)
						xbmcvfs.delete(whatPath)
					else:
						pass
				else:
					pass
			else:
				pass
		else:
			pass

selected()