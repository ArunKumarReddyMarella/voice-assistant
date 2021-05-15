<h1>Personal voice assistant</h1>

<h3>Description</h3>
<p>The program execution starts from the driver function,where it has set a password as security, if the password doesnot matches with the security code then the function stop executing,if the passward matches then the it allows to the assistant. Then it calls the voice_assistant function to execute the remaining code until the listening variable  is set to true.The listening time of source is set to 10secs after that   stop recieveind the data and execute the data which is detected if it not detected then  it through an exception.</p>
<p>I created my personal voice assistant with some basic features which I use frequently like </p>
<ul><li>Jokes</li>
<li>coronavirus details</li>
<li>the top news from google,playing songs</li>
<li>sending message in whatssapp</li>
<li>sending mail</li>
<li>s<li>rching in google and Wikipedia</li>
<li>opening web cam</li>
<li>whether details of a place</li>
<li>timer</li>
<li>stopclock</li>
<li>the top 10 movies according to imdb</li>
<li>finding location</li>
<li>current time</li>
</ul>




<h3>Packages</h3>
<p>For this project I imported the packages which is in above picture.</p>
<ul><li>Sys packages is for exit() function to exit from the program.</li>
<li>Speech_recognition package  is used to recognize the voice from the user.</li>
<li>From selenium package I imported the wedriver module to send messages from whatsapp.</li>
<li>From gtts package I imported the gTTS module to convert the text to speech so that user can listen.</li>
<li>Playsound package is used to play the songs using playsound module in it.</li>
<li>Time package is used to get the local time and also to dely the execution program.</li>
<li>Os package is used to get accsess to local files so that we can create and destroy the files.</li>
<li>Webbrowser package is used to open the browser.</li>
<li>Smtplib package is used to send mails .</li>
<li>Bs4 package is used to get the clear data after webscraping using Beautifulsoap.</li>
<li>Pyjokes package is used to get the random jokes for entertainment.</li>
<li>Urllib package is used to open the url link and get the required data.</li>
<li>Requests is used to get the connection with website  as API .</li>
<li>Imdb package is has API which used to get the data of top movies.</li>
<li>Winsound package is used to make some sound with certain frequency.</li>
<li>Cv2 package is open the webcam and detect the faces.</li>
<li>Pywhatkit is used to play the youtube videos.</li>
</ul>

<h3>Functions</h3>
<ul><li>Youtube : This module play the any youtube video using playonyt module from pywhatkit.</li>
<li>Joke : This module say some jokes randomly from get_jokes module in Pyjokes packages.</li>
<li>Coviddetails : This module has Covid module imported from covid package whis has API which continuously track the covid-19 details of active,confirmed,recovered,death cases around the globe.</li>
<li>news : This module gives the top news which is collected from the google. It has webscrapping method to get the title,link and DataandTime of the news.</li>
<li>Song : This module has playsound module from playsound package to play song from the memory.</li>
<li>Webcam : This module uses cv2 package which open the webcam and show the image frame by frame.</li>
<li>Timer : This module uses sleep method to stop the function to specific time and also has the Beep function from winsound to remind.</li>
<li>Movies :  This module uses imdb package to get top movies.</li>
<li>Whatsapp : This module uses the Chrome function from webdriver package to open website in browser and send message to the user specify person.It find the elements by xpath function from driver.</li>
<li>Weather : This module uses the Chrome function from webdriver package to open website in browser get the required data.</li>
<li>Stopclock : This module uses time package with sleep methop to stop execution for specific time.it start’s when we press enter.</li>
<li>Listen : This module uses recognizer function from speech_recognition package with microphone as source and converts the input audio to text, if it is in speech otherwise through exception.</li>
<li>Respond : This module gTTS function from gtts to convert text to audio, os is used to save the audio and delete after the use.</li>
<li>Voice_assistant : This is the main function where all function are called according to function.It has some extra features like sending mail,searching in wikipedia and in google.</li>
<ul>
