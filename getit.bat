@echo off
mode con: cols=65 lines=35
color a
cd /
netsh wlan show profiles
goto getspecificwlan
:getspecificwlan
	echo++++++++++++++++++++++++++
	set /p opti=WLAN Name: 
	netsh wlan show profiles "%opti%" key=clear > "C:/virtualenvironment/Codes/getIt.txt
	cls
	echo Done!
	Timeout 0
	exit
