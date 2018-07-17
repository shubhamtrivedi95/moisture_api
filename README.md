please use non proxy wifi connection and connect the system and arduino to the same wifi router. 

Software requirements:

	1.  Arduino IDE with NODEMCU board setup.
		visit here for more details(http://www.instructables.com/id/Steps-to-Setup-Arduino-IDE-for-NODEMCU-ESP8266-WiF/)
	2.  Python3 visit this link https://www.python.org/downloads/ to download python3 

follow the following procedure to run the webapp:
 
	1. open the command window and navigate to moisture_api-master directory.
	2. run the command "pip install -r requirements.txt" 
	   or "pip3 install -r requirements.txt"(Note-Internet connection is needed)
	3. after the installation run the command "python manage.py runserver 0.0.0.0:80"
		you should get following message.
		
		Performing system checks...

		System check identified no issues (0 silenced).
		June 16, 2018 - 13:48:32
		Django version 2.0.6, using settings 'moisture_api.settings'
		Starting development server at http://0.0.0.0:80/
		Quit the server with CTRL-BREAK.
	4.	after this open another command window and type "ipconfig".
	5. Note the ip address of wireless lan adapter.
	6. open the arduino sketch "nodemcu_sketch" and modify the ip address ,wifi ssid and password.
	7. connect nodemcu to system through USB cable and Upload the code.
	8. confirm the connection on your router.
	9. Thats it now you can use the system. at "localhost/Update"
	
	
Some troubleshooting tips.

	if you want to delete some entries the visit localhost/admin and login there and click on machiness.
	if you are getting disallowed host error then,
	 nevigate to the moisture_api-master/moisture_api 
	 and open settings.py add your ip address to the ALLOWED_HOST
	 
	 LOGIN DETAILS
	 username-shubh
	 password- SIH2018ssce
