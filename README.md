<h1>Personal voice assistant</h1>

<h3>Description</h3>
The program execution starts from the driver function,where it has set a password as security, if the password doesnot matches with the security code then the function stop executing,if the passward matches then the it allows to the assistant. Then it calls the voice_assistant function to execute the remaining code until the listening variable  is set to true.The listening time of source is set to 10secs after that   stop recieveind the data and execute the data which is detected if it not detected then  it through an exception.
I created my personal voice assistant with some basic features which I use frequently like 
•	Jokes
•	coronavirus details
•	the top news from google,playing songs
•	sending message in whatssapp
•	sending mail
•	searching in google and Wikipedia
•	opening web cam
•	whether details of a place
•	timer
•	stopclock 
•	the top 10 movies according to imdb
•	finding location
•	current time




Packages
       
For this project I imported the packages which is in above picture.
•	Sys packages is for exit() function to exit from the program.
•	Speech_recognition package  is used to recognize the voice from the user .
•	From selenium package I imported the wedriver module to send messages from whatsapp.
•	From gtts package I imported the gTTS module to convert the text to speech so that user can listen.
•	Playsound package is used to play the songs using playsound module in it.
•	Time package is used to get the local time and also to dely the execution program.
•	Os package is used to get accsess to local files so that we can create and destroy the files.
•	Webbrowser package is used to open the browser.
•	Smtplib package is used to send mails .
•	Bs4 package is used to get the clear data after webscraping using Beautifulsoap.
•	Pyjokes package is used to get the random jokes for entertainment.
•	Urllib package is used to open the url link and get the required data.
•	Requests is used to get the connection with website  as API .
•	Imdb package is has API which used to get the data of top movies.
•	Winsound package is used to make some sound with certain frequency.
•	Cv2 package is open the webcam and detect the faces.
•	Pywhatkit is used to play the youtube videos.

<h3>Functions</h3>
 
•	Youtube : This module play the any youtube video using playonyt module from pywhatkit.
•	Joke : This module say some jokes randomly from get_jokes module in Pyjokes packages.
•	Coviddetails : This module has Covid module imported from covid package whis has API which continuously track the covid-19 details of active,confirmed,recovered,death cases around the globe.
•	news : This module gives the top news which is collected from the google. It has webscrapping method to get the title,link and DataandTime of the news.
•	Song : This module has playsound module from playsound package to play song from the memory.
•	Webcam : This module uses cv2 package which open the webcam and show the image frame by frame.
•	Timer : This module uses sleep method to stop the function to specific time and also has the Beep function from winsound to remind.
•	Movies :  This module uses imdb package to get top movies.
•	Whatsapp : This module uses the Chrome function from webdriver package to open website in browser and send message to the user specify person.It find the elements by xpath function from driver.
•	Weather : This module uses the Chrome function from webdriver package to open website in browser get the required data.
•	Stopclock : This module uses time package with sleep methop to stop execution for specific time.it start’s when we press enter.
•	Listen : This module uses recognizer function from speech_recognition package with microphone as source and converts the input audio to text, if it is in speech otherwise through exception.
•	Respond : This module gTTS function from gtts to convert text to audio, os is used to save the audio and delete after the use.
•	Voice_assistant : This is the main function where all function are called according to function.It has some extra features like sending mail,searching in wikipedia and in google.
