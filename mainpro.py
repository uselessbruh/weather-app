import subprocess
from tkinter import *
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def cityname(city=None):
	if city is None:
		callscript("")
	else:
		callscript(city)

def searchcity():
   tab1canvas.destroy()
   scrollbar1.destroy()
   inner2_frame.destroy()
   tab2canvas.destroy()
   scrollbar.destroy()
   inner_frame.destroy()
   tab3canvas.destroy()
   tab4canvas.destroy()
   cityval=entercity.get()
   cityname(cityval)


def callscript(city):
	script_path = "lalu.sh"

	result=subprocess.run(["wsl", "bash",script_path, city], capture_output=True, text=True)

	weatherresult = result.stdout.strip()
    
	factlist=weatherresult.split("\n\n\n\n\n\n\n\n\n\n")
    
	global current    
	current=factlist[0];current=current.split("\n")
	current = {item.split("=")[0]: item.split("=")[1] for item in current}
    
	global nearest
	nearest=factlist[1];nearest=nearest.split("\n");nearest.remove("")
	nearest = {item.split("=")[0]: item.split("=")[1] for item in nearest}
    
	weather1=factlist[3];weather2=factlist[4];weather3=factlist[5]
	weather1=weather1.split("\n\n\n\n\n");weather2=weather2.split("\n\n\n\n\n");weather3=weather3.split("\n\n\n\n\n")
    
	global astro1,astro2,astro3
	astro1=weather1[0];astro1=astro1.split("\n");astro1.remove("")
	astro1 = {item.split(":")[0]: item.split(":")[1] for item in astro1}
	astro2=weather2[0];astro2=astro2.split("\n");astro2.remove("")
	astro2 = {item.split(":")[0]: item.split(":")[1] for item in astro2}
	astro3=weather3[0];astro3=astro3.split("\n");astro3.remove("")
	astro3 = {item.split(":")[0]: item.split(":")[1] for item in astro3}

	global hourly11,hourly12,hourly13,hourly14,hourly15,hourly16,hourly17,hourly18
	hourly1=weather1[1];hourly1=hourly1.split("\n");hourly1.remove("")
	hourly11=hourly1[:41];hourly11.remove("weatherIconUrl:")	
	hourly11 = {item.split(":")[0]: item.split(":")[1] for item in hourly11}
	hourly12=hourly1[41:82];hourly12.remove("weatherIconUrl:")
	hourly12 = {item.split(":")[0]: item.split(":")[1] for item in hourly12}
	hourly13=hourly1[82:123];hourly13.remove("weatherIconUrl:")
	hourly13 = {item.split(":")[0]: item.split(":")[1] for item in hourly13}
	hourly14=hourly1[123:164];hourly14.remove("weatherIconUrl:")
	hourly14 = {item.split(":")[0]: item.split(":")[1] for item in hourly14}
	hourly15=hourly1[164:205];hourly15.remove("weatherIconUrl:")
	hourly15 = {item.split(":")[0]: item.split(":")[1] for item in hourly15}
	hourly16=hourly1[205:246];hourly16.remove("weatherIconUrl:")
	hourly16 = {item.split(":")[0]: item.split(":")[1] for item in hourly16}
	hourly17=hourly1[246:287];hourly17.remove("weatherIconUrl:")
	hourly17 = {item.split(":")[0]: item.split(":")[1] for item in hourly17}
	hourly18=hourly1[287:328];hourly18.remove("weatherIconUrl:")
	hourly18 = {item.split(":")[0]: item.split(":")[1] for item in hourly18}
    
	global hourly21,hourly22,hourly23,hourly24,hourly25,hourly26,hourly27,hourly28
	hourly2=weather2[1];hourly2=hourly2.split("\n");hourly2.remove("")
	hourly21=hourly2[:41];hourly21.remove("weatherIconUrl:")	
	hourly21 = {item.split(":")[0]: item.split(":")[1] for item in hourly21}
	hourly22=hourly2[41:82];hourly22.remove("weatherIconUrl:")
	hourly22 = {item.split(":")[0]: item.split(":")[1] for item in hourly22}
	hourly23=hourly2[82:123];hourly23.remove("weatherIconUrl:")
	hourly23 = {item.split(":")[0]: item.split(":")[1] for item in hourly23}
	hourly24=hourly2[123:164];hourly24.remove("weatherIconUrl:")
	hourly24 = {item.split(":")[0]: item.split(":")[1] for item in hourly24}
	hourly25=hourly2[164:205];hourly25.remove("weatherIconUrl:")
	hourly25 = {item.split(":")[0]: item.split(":")[1] for item in hourly25}
	hourly26=hourly2[205:246];hourly26.remove("weatherIconUrl:")
	hourly26 = {item.split(":")[0]: item.split(":")[1] for item in hourly26}
	hourly27=hourly2[246:287];hourly27.remove("weatherIconUrl:")
	hourly27 = {item.split(":")[0]: item.split(":")[1] for item in hourly27}
	hourly28=hourly2[287:328];hourly28.remove("weatherIconUrl:")
	hourly28 = {item.split(":")[0]: item.split(":")[1] for item in hourly28}

	global hourly31,hourly32,hourly33,hourly34,hourly35,hourly36,hourly37,hourly38
	hourly3=weather3[1];hourly3=hourly3.split("\n");hourly3.remove("")
	hourly31=hourly3[:41];hourly31.remove("weatherIconUrl:")	
	hourly31 = {item.split(":")[0]: item.split(":")[1] for item in hourly31}
	hourly32=hourly3[41:82];hourly32.remove("weatherIconUrl:")
	hourly32 = {item.split(":")[0]: item.split(":")[1] for item in hourly32}
	hourly33=hourly3[82:123];hourly33.remove("weatherIconUrl:")
	hourly33 = {item.split(":")[0]: item.split(":")[1] for item in hourly33}
	hourly34=hourly3[123:164];hourly34.remove("weatherIconUrl:")
	hourly34 = {item.split(":")[0]: item.split(":")[1] for item in hourly34}
	hourly35=hourly3[164:205];hourly35.remove("weatherIconUrl:")
	hourly35 = {item.split(":")[0]: item.split(":")[1] for item in hourly35}
	hourly36=hourly3[205:246];hourly36.remove("weatherIconUrl:")
	hourly36 = {item.split(":")[0]: item.split(":")[1] for item in hourly36}
	hourly37=hourly3[246:287];hourly37.remove("weatherIconUrl:")
	hourly37 = {item.split(":")[0]: item.split(":")[1] for item in hourly37}
	hourly38=hourly3[287:328];hourly38.remove("weatherIconUrl:")
	hourly38 = {item.split(":")[0]: item.split(":")[1] for item in hourly38}
	
	global daydesc1,daydesc2,daydesc3
	daydesc1=weather1[2];daydesc1=daydesc1.split("\n");daydesc1.remove("")
	daydesc1 = {item.split("=")[0]: item.split("=")[1] for item in daydesc1}
	daydesc2=weather2[2];daydesc2=daydesc2.split("\n");daydesc2.remove("")
	daydesc2 = {item.split("=")[0]: item.split("=")[1] for item in daydesc2}
	daydesc3=weather3[2];daydesc3=daydesc3.split("\n");daydesc3.remove("")
	daydesc3 = {item.split("=")[0]: item.split("=")[1] for item in daydesc3};
	tab1info();tab2info();tab3info();tab4info()


def tab1info():
    
	global tab1canvas    
	tab1canvas=Canvas(tab1,bg="light salmon")
	tab1canvas.pack(fill="both", expand=True)
    
	if current['weatherDesc']=='Partly cloudy':
		weatherlogo=Label(tab1canvas,text="⛅️",font=('Segoe UI Emoji', 150),bg="light salmon")
		weatherlogo.place(x=5,y=5)
	elif current['weatherDesc']=="Clear":
		weatherlogo=Label(tab1canvas,text="☀️",font=('Segoe UI Emoji', 150),bg="light salmon")
		weatherlogo.place(x=5,y=5)
	elif current['weatherDesc']=="Mostly cloudy":
		weatherlogo=Label(tab1canvas,text="🌥️",font=('Segoe UI Emoji', 150),bg="light salmon")
		weatherlogo.place(x=5,y=5)
	elif current['weatherDesc']=="Overcast":
		weatherlogo=Label(tab1canvas,text="☁️",font=('Segoe UI Emoji', 150),bg="light salmon")
		weatherlogo.place(x=5,y=5)
	elif current['weatherDesc']=="Sunny":
		weatherlogo=Label(tab1canvas,text="🌞",font=('Segoe UI Emoji', 150),bg="light salmon")
		weatherlogo.place(x=5,y=5)
	elif current['weatherDesc']=="Rainy":
		weatherlogo=Label(tab1canvas,text="🌧️",font=('Segoe UI Emoji', 150),bg="light salmon")
		weatherlogo.place(x=5,y=5)
	elif current['weatherDesc']=="Showers":
		weatherlogo=Label(tab1canvas,text="🌦️",font=('Segoe UI Emoji', 150),bg="light salmon")
		weatherlogo.place(x=5,y=5)
	elif current['weatherDesc']=="Thunderstorms":
		weatherlogo=Label(tab1canvas,text="⛈️",font=('Segoe UI Emoji', 150),bg="light salmon")
		weatherlogo.place(x=5,y=5)
	elif current['weatherDesc']=="Snowy":
		weatherlogo=Label(tab1canvas,text="🌨️",font=('Segoe UI Emoji', 150),bg="light salmon")
		weatherlogo.place(x=5,y=5)
	else:
		weatherlogo=Label(tab1canvas,text="🌫️",font=('Segoe UI Emoji', 150),bg="light salmon")
		weatherlogo.place(x=5,y=5)
	
	if current['winddir16Point'] == 'N':
		windir = "North"
	elif current['winddir16Point'] == 'NNE':
		windir = "North-Northeast"
	elif current['winddir16Point'] == 'NE':
		windir = "Northeast"
	elif current['winddir16Point'] == 'ENE':
		windir = "East-Northeast"
	elif current['winddir16Point'] == 'E':
		windir = "East"
	elif current['winddir16Point'] == 'ESE':
		windir = "East-Southeast"
	elif current['winddir16Point'] == 'SE':
		windir = "Southeast"
	elif current['winddir16Point'] == 'SSE':
		windir = "South-Southeast"
	elif current['winddir16Point'] == 'S':
		windir = "South"
	elif current['winddir16Point'] == 'SSW':
		windir = "South-Southwest"
	elif current['winddir16Point'] == 'SW':
		windir = "Southwest"
	elif current['winddir16Point'] == 'WSW':
		windir = "West-Southwest"
	elif current['winddir16Point'] == 'W':
		windir = "West"
	elif current['winddir16Point'] == 'WNW':
		windir = "West-Northwest"
	elif current['winddir16Point'] == 'NW':
		windir = "Northwest"
	elif current['winddir16Point'] == 'NNW':
		windir = "North-Northwest"
	else:
		windir = "Unknown direction"

	weatherdesc=Label(tab1canvas,text=current['weatherDesc'],font=("times new roman",20,"bold"),bg="light salmon")
	weatherdesc.place(x=60,y=270)
	
	livplace=Label(tab1canvas,text=nearest['areaName']+"\n"+nearest['region']+", "+nearest['country'],font=("times new roman",10,"bold"),bg="light salmon")
	livplace.place(x=378,y=230)
	
	latlong=Label(tab1canvas,text="LAT: "+nearest['latitude']+" LONG: "+nearest['longitude'],font=("times new roman",10,"bold"),bg="light salmon")
	latlong.place(x=350,y=280)
	
	pop=Label(tab1canvas,text="POPULATION: "+nearest['population'],font=("times new roman",10,"bold"),bg="light salmon")
	pop.place(x=357,y=262)	
	
	temp=Label(tab1canvas,text=current['temp_C']+"°C"+"\n("+current['temp_F']+"°F)",font=("times new roman",50,"bold"),bg="light salmon")
	temp.place(x=330,y=30)	
	
	feelike=Label(tab1canvas,text="feels like: "+current['FeelsLikeC']+"°C"+"("+current['FeelsLikeF']+"°F)",font=("times new roman",12,"bold"),bg="light salmon")
	feelike.place(x=350,y=200)					
    	
	rest=Label(tab1canvas,text="CLOUD COVER: "+current['cloudcover']+"%\nHUMIDITY: "+current['humidity']+"%\nPRECIPITATION: "+current['precipInches']+"inches ("+current['precipMM']+"mm)\nPRESSURE: "+current['pressure']+"mb ("+current['pressureInches']+"inches)\nUV INDEX: "+current['uvIndex']+"\nVISIBILITY: "+current['visibility']+"km ("+current['visibilityMiles']+"miles)\n"+"\nWind coming from the "+windir+"\nat the speed of "+current['windspeedKmph']+"km/h ("+current['windspeedMiles']+"mph),\nwith wind direction of "+current['winddirDegree']+" degree",font=("times new roman",20,"bold"),bg="light salmon")
	rest.place(x=70,y=350)        	
        	
	recordtime=Label(tab1canvas,text="Local Observation Date and Time: "+current['localObsDateTime'],font=("times new roman",10,"bold"),bg="light salmon")
	recordtime.place(x=140,y=680)

def on_frame_configure(event):
    tab3canvas.configure(scrollregion=tab3canvas.bbox("all"))
        
def on_canvas_configure(event):
    tab3canvas.itemconfig(inner_frame, width=event.width)
    
def on_frame_configure1(event):
    tab2canvas.configure(scrollregion=tab2canvas.bbox("all"))
        
def on_canvas_configure1(event):
    tab2canvas.itemconfig(inner_frame, width=event.width)
    
    
def populate_table(tree):
    data = [
        ['DewPointC', hourly11['DewPointC'], hourly12['DewPointC'], hourly13['DewPointC'], hourly14['DewPointC'], hourly15['DewPointC'], hourly16['DewPointC'], hourly17['DewPointC'], hourly18['DewPointC']],
        ['DewPointF', hourly11['DewPointF'], hourly12['DewPointF'], hourly13['DewPointF'], hourly14['DewPointF'], hourly15['DewPointF'], hourly16['DewPointF'], hourly17['DewPointF'], hourly18['DewPointF']],
        ['FeelsLikeC', hourly11['FeelsLikeC'], hourly12['FeelsLikeC'], hourly13['FeelsLikeC'], hourly14['FeelsLikeC'], hourly15['FeelsLikeC'], hourly16['FeelsLikeC'], hourly17['FeelsLikeC'], hourly18['FeelsLikeC']],
        ['FeelsLikeF', hourly11['FeelsLikeF'], hourly12['FeelsLikeF'], hourly13['FeelsLikeF'], hourly14['FeelsLikeF'], hourly15['FeelsLikeF'], hourly16['FeelsLikeF'], hourly17['FeelsLikeF'], hourly18['FeelsLikeF']],
        ['HeatIndexC', hourly11['HeatIndexC'], hourly12['HeatIndexC'], hourly13['HeatIndexC'], hourly14['HeatIndexC'], hourly15['HeatIndexC'], hourly16['HeatIndexC'], hourly17['HeatIndexC'], hourly18['HeatIndexC']],
        ['HeatIndexF', hourly11['HeatIndexF'], hourly12['HeatIndexF'], hourly13['HeatIndexF'], hourly14['HeatIndexF'], hourly15['HeatIndexF'], hourly16['HeatIndexF'], hourly17['HeatIndexF'], hourly18['HeatIndexF']],
        ['WindChillC', hourly11['WindChillC'], hourly12['WindChillC'], hourly13['WindChillC'], hourly14['WindChillC'], hourly15['WindChillC'], hourly16['WindChillC'], hourly17['WindChillC'], hourly18['WindChillC']],
        ['WindChillF', hourly11['WindChillF'], hourly12['WindChillF'], hourly13['WindChillF'], hourly14['WindChillF'], hourly15['WindChillF'], hourly16['WindChillF'], hourly17['WindChillF'], hourly18['WindChillF']],
        ['WindGustKmph', hourly11['WindGustKmph'], hourly12['WindGustKmph'], hourly13['WindGustKmph'], hourly14['WindGustKmph'], hourly15['WindGustKmph'], hourly16['WindGustKmph'], hourly17['WindGustKmph'], hourly18['WindGustKmph']],
        ['WindGustMiles', hourly11['WindGustMiles'], hourly12['WindGustMiles'], hourly13['WindGustMiles'], hourly14['WindGustMiles'], hourly15['WindGustMiles'], hourly16['WindGustMiles'], hourly17['WindGustMiles'], hourly18['WindGustMiles']],
        ['chanceoffog', hourly11['chanceoffog'], hourly12['chanceoffog'], hourly13['chanceoffog'], hourly14['chanceoffog'], hourly15['chanceoffog'], hourly16['chanceoffog'], hourly17['chanceoffog'], hourly18['chanceoffog']],
        ['chanceoffrost', hourly11['chanceoffrost'], hourly12['chanceoffrost'], hourly13['chanceoffrost'], hourly14['chanceoffrost'], hourly15['chanceoffrost'], hourly16['chanceoffrost'], hourly17['chanceoffrost'], hourly18['chanceoffrost']],
        ['chanceofhightemp', hourly11['chanceofhightemp'], hourly12['chanceofhightemp'], hourly13['chanceofhightemp'], hourly14['chanceofhightemp'], hourly15['chanceofhightemp'], hourly16['chanceofhightemp'], hourly17['chanceofhightemp'], hourly18['chanceofhightemp']],
        ['chanceofovercast', hourly11['chanceofovercast'], hourly12['chanceofovercast'], hourly13['chanceofovercast'], hourly14['chanceofovercast'], hourly15['chanceofovercast'], hourly16['chanceofovercast'], hourly17['chanceofovercast'], hourly18['chanceofovercast']],
        ['chanceofrain', hourly11['chanceofrain'], hourly12['chanceofrain'], hourly13['chanceofrain'], hourly14['chanceofrain'], hourly15['chanceofrain'], hourly16['chanceofrain'], hourly17['chanceofrain'], hourly18['chanceofrain']],
        ['chanceofremdry', hourly11['chanceofremdry'], hourly12['chanceofremdry'], hourly13['chanceofremdry'], hourly14['chanceofremdry'], hourly15['chanceofremdry'], hourly16['chanceofremdry'], hourly17['chanceofremdry'], hourly18['chanceofremdry']],
        ['chanceofsnow', hourly11['chanceofsnow'], hourly12['chanceofsnow'], hourly13['chanceofsnow'], hourly14['chanceofsnow'], hourly15['chanceofsnow'], hourly16['chanceofsnow'], hourly17['chanceofsnow'], hourly18['chanceofsnow']],
        ['chanceofsunshine', hourly11['chanceofsunshine'], hourly12['chanceofsunshine'], hourly13['chanceofsunshine'], hourly14['chanceofsunshine'], hourly15['chanceofsunshine'], hourly16['chanceofsunshine'], hourly17['chanceofsunshine'], hourly18['chanceofsunshine']],
        ['chanceofthunder', hourly11['chanceofthunder'], hourly12['chanceofthunder'], hourly13['chanceofthunder'], hourly14['chanceofthunder'], hourly15['chanceofthunder'], hourly16['chanceofthunder'], hourly17['chanceofthunder'], hourly18['chanceofthunder']],
        ['chanceofwindy', hourly11['chanceofwindy'], hourly12['chanceofwindy'], hourly13['chanceofwindy'], hourly14['chanceofwindy'], hourly15['chanceofwindy'], hourly16['chanceofwindy'], hourly17['chanceofwindy'], hourly18['chanceofwindy']],
        ['cloudcover', hourly11['cloudcover'], hourly12['cloudcover'], hourly13['cloudcover'], hourly14['cloudcover'], hourly15['cloudcover'], hourly16['cloudcover'], hourly17['cloudcover'], hourly18['cloudcover']],
        ['diffRad', hourly11['diffRad'], hourly12['diffRad'], hourly13['diffRad'], hourly14['diffRad'], hourly15['diffRad'], hourly16['diffRad'], hourly17['diffRad'], hourly18['diffRad']],
        ['humidity', hourly11['humidity'], hourly12['humidity'], hourly13['humidity'], hourly14['humidity'], hourly15['humidity'], hourly16['humidity'], hourly17['humidity'], hourly18['humidity']],
        ['precipInches', hourly11['precipInches'], hourly12['precipInches'], hourly13['precipInches'], hourly14['precipInches'], hourly15['precipInches'], hourly16['precipInches'], hourly17['precipInches'], hourly18['precipInches']],
        ['precipMM', hourly11['precipMM'], hourly12['precipMM'], hourly13['precipMM'], hourly14['precipMM'], hourly15['precipMM'], hourly16['precipMM'], hourly17['precipMM'], hourly18['precipMM']],
        ['pressure', hourly11['pressure'], hourly12['pressure'], hourly13['pressure'], hourly14['pressure'], hourly15['pressure'], hourly16['pressure'], hourly17['pressure'], hourly18['pressure']],
        ['pressureInches', hourly11['pressureInches'], hourly12['pressureInches'], hourly13['pressureInches'], hourly14['pressureInches'], hourly15['pressureInches'], hourly16['pressureInches'], hourly17['pressureInches'], hourly18['pressureInches']],
        ['shortRad', hourly11['shortRad'], hourly12['shortRad'], hourly13['shortRad'], hourly14['shortRad'], hourly15['shortRad'], hourly16['shortRad'], hourly17['shortRad'], hourly18['shortRad']],
        ['tempC', hourly11['tempC'], hourly12['tempC'], hourly13['tempC'], hourly14['tempC'], hourly15['tempC'], hourly16['tempC'], hourly17['tempC'], hourly18['tempC']],
        ['tempF', hourly11['tempF'], hourly12['tempF'], hourly13['tempF'], hourly14['tempF'], hourly15['tempF'], hourly16['tempF'], hourly17['tempF'], hourly18['tempF']],
        ['time', '0', '300', '600', '900', '1200', '1500', '1800', '2100'],
        ['uvIndex', hourly11['uvIndex'], hourly12['uvIndex'], hourly13['uvIndex'], hourly14['uvIndex'], hourly15['uvIndex'], hourly16['uvIndex'], hourly17['uvIndex'], hourly18['uvIndex']],
        ['visibility', hourly11['visibility'], hourly12['visibility'], hourly13['visibility'], hourly14['visibility'], hourly15['visibility'], hourly16['visibility'], hourly17['visibility'], hourly18['visibility']],
        ['visibilityMiles', hourly11['visibilityMiles'], hourly12['visibilityMiles'], hourly13['visibilityMiles'], hourly14['visibilityMiles'], hourly15['visibilityMiles'], hourly16['visibilityMiles'], hourly17['visibilityMiles'], hourly18['visibilityMiles']],
        ['weatherCode', hourly11['weatherCode'], hourly12['weatherCode'], hourly13['weatherCode'], hourly14['weatherCode'], hourly15['weatherCode'], hourly16['weatherCode'], hourly17['weatherCode'], hourly18['weatherCode']],
        ['weatherDesc', 'Clear ', 'Clear ', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Clear '],
        ['winddir16Point', hourly11['winddir16Point'], hourly12['winddir16Point'], hourly13['winddir16Point'], hourly14['winddir16Point'], hourly15['winddir16Point'], hourly16['winddir16Point'], hourly17['winddir16Point'], hourly18['winddir16Point']],
        ['winddirDegree', hourly11['winddirDegree'], hourly12['winddirDegree'], hourly13['winddirDegree'], hourly14['winddirDegree'], hourly15['winddirDegree'], hourly16['winddirDegree'], hourly17['winddirDegree'], hourly18['winddirDegree']],
        ['windspeedKmph', hourly11['windspeedKmph'], hourly12['windspeedKmph'], hourly13['windspeedKmph'], hourly14['windspeedKmph'], hourly15['windspeedKmph'], hourly16['windspeedKmph'], hourly17['windspeedKmph'], hourly18['windspeedKmph']],
        ['windspeedMiles', hourly11['windspeedMiles'], hourly12['windspeedMiles'], hourly13['windspeedMiles'], hourly14['windspeedMiles'], hourly15['windspeedMiles'], hourly16['windspeedMiles'], hourly17['windspeedMiles'], hourly18['windspeedMiles']]
    ]
    
    # Insert data into the treeview
    for item in data:
        tree.insert("", "end", values=item)
        
def populate_table1(tree):
    data = [
        ['DewPointC', hourly21['DewPointC'], hourly22['DewPointC'], hourly23['DewPointC'], hourly24['DewPointC'], hourly25['DewPointC'], hourly26['DewPointC'], hourly27['DewPointC'], hourly28['DewPointC']],
        ['DewPointF', hourly21['DewPointF'], hourly22['DewPointF'], hourly23['DewPointF'], hourly24['DewPointF'], hourly25['DewPointF'], hourly26['DewPointF'], hourly27['DewPointF'], hourly28['DewPointF']],
        ['FeelsLikeC', hourly21['FeelsLikeC'], hourly22['FeelsLikeC'], hourly23['FeelsLikeC'], hourly24['FeelsLikeC'], hourly25['FeelsLikeC'], hourly26['FeelsLikeC'], hourly27['FeelsLikeC'], hourly28['FeelsLikeC']],
        ['FeelsLikeF', hourly21['FeelsLikeF'], hourly22['FeelsLikeF'], hourly23['FeelsLikeF'], hourly24['FeelsLikeF'], hourly25['FeelsLikeF'], hourly26['FeelsLikeF'], hourly27['FeelsLikeF'], hourly28['FeelsLikeF']],
        ['HeatIndexC', hourly21['HeatIndexC'], hourly22['HeatIndexC'], hourly23['HeatIndexC'], hourly24['HeatIndexC'], hourly25['HeatIndexC'], hourly26['HeatIndexC'], hourly27['HeatIndexC'], hourly28['HeatIndexC']],
        ['HeatIndexF', hourly21['HeatIndexF'], hourly22['HeatIndexF'], hourly23['HeatIndexF'], hourly24['HeatIndexF'], hourly25['HeatIndexF'], hourly26['HeatIndexF'], hourly27['HeatIndexF'], hourly28['HeatIndexF']],
        ['WindChillC', hourly21['WindChillC'], hourly22['WindChillC'], hourly23['WindChillC'], hourly24['WindChillC'], hourly25['WindChillC'], hourly26['WindChillC'], hourly27['WindChillC'], hourly28['WindChillC']],
        ['WindChillF', hourly21['WindChillF'], hourly22['WindChillF'], hourly23['WindChillF'], hourly24['WindChillF'], hourly25['WindChillF'], hourly26['WindChillF'], hourly27['WindChillF'], hourly28['WindChillF']],
        ['WindGustKmph', hourly21['WindGustKmph'], hourly22['WindGustKmph'], hourly23['WindGustKmph'], hourly24['WindGustKmph'], hourly25['WindGustKmph'], hourly26['WindGustKmph'], hourly27['WindGustKmph'], hourly28['WindGustKmph']],
        ['WindGustMiles', hourly21['WindGustMiles'], hourly22['WindGustMiles'], hourly23['WindGustMiles'], hourly24['WindGustMiles'], hourly25['WindGustMiles'], hourly26['WindGustMiles'], hourly27['WindGustMiles'], hourly28['WindGustMiles']],
        ['chanceoffog', hourly21['chanceoffog'], hourly22['chanceoffog'], hourly23['chanceoffog'], hourly24['chanceoffog'], hourly25['chanceoffog'], hourly26['chanceoffog'], hourly27['chanceoffog'], hourly28['chanceoffog']],
        ['chanceoffrost', hourly21['chanceoffrost'], hourly22['chanceoffrost'], hourly23['chanceoffrost'], hourly24['chanceoffrost'], hourly25['chanceoffrost'], hourly26['chanceoffrost'], hourly27['chanceoffrost'], hourly28['chanceoffrost']],
        ['chanceofhightemp', hourly21['chanceofhightemp'], hourly22['chanceofhightemp'], hourly23['chanceofhightemp'], hourly24['chanceofhightemp'], hourly25['chanceofhightemp'], hourly26['chanceofhightemp'], hourly27['chanceofhightemp'], hourly28['chanceofhightemp']],
        ['chanceofovercast', hourly21['chanceofovercast'], hourly22['chanceofovercast'], hourly23['chanceofovercast'], hourly24['chanceofovercast'], hourly25['chanceofovercast'], hourly26['chanceofovercast'], hourly27['chanceofovercast'], hourly28['chanceofovercast']],
        ['chanceofrain', hourly21['chanceofrain'], hourly22['chanceofrain'], hourly23['chanceofrain'], hourly24['chanceofrain'], hourly25['chanceofrain'], hourly26['chanceofrain'], hourly27['chanceofrain'], hourly28['chanceofrain']],
        ['chanceofremdry', hourly21['chanceofremdry'], hourly22['chanceofremdry'], hourly23['chanceofremdry'], hourly24['chanceofremdry'], hourly25['chanceofremdry'], hourly26['chanceofremdry'], hourly27['chanceofremdry'], hourly28['chanceofremdry']],
        ['chanceofsnow', hourly21['chanceofsnow'], hourly22['chanceofsnow'], hourly23['chanceofsnow'], hourly24['chanceofsnow'], hourly25['chanceofsnow'], hourly26['chanceofsnow'], hourly27['chanceofsnow'], hourly28['chanceofsnow']],
        ['chanceofsunshine', hourly21['chanceofsunshine'], hourly22['chanceofsunshine'], hourly23['chanceofsunshine'], hourly24['chanceofsunshine'], hourly25['chanceofsunshine'], hourly26['chanceofsunshine'], hourly27['chanceofsunshine'], hourly28['chanceofsunshine']],
        ['chanceofthunder', hourly21['chanceofthunder'], hourly22['chanceofthunder'], hourly23['chanceofthunder'], hourly24['chanceofthunder'], hourly25['chanceofthunder'], hourly26['chanceofthunder'], hourly27['chanceofthunder'], hourly28['chanceofthunder']],
        ['chanceofwindy', hourly21['chanceofwindy'], hourly22['chanceofwindy'], hourly23['chanceofwindy'], hourly24['chanceofwindy'], hourly25['chanceofwindy'], hourly26['chanceofwindy'], hourly27['chanceofwindy'], hourly28['chanceofwindy']],
        ['cloudcover', hourly21['cloudcover'], hourly22['cloudcover'], hourly23['cloudcover'], hourly24['cloudcover'], hourly25['cloudcover'], hourly26['cloudcover'], hourly27['cloudcover'], hourly28['cloudcover']],
        ['diffRad', hourly21['diffRad'], hourly22['diffRad'], hourly23['diffRad'], hourly24['diffRad'], hourly25['diffRad'], hourly26['diffRad'], hourly27['diffRad'], hourly28['diffRad']],
        ['humidity', hourly21['humidity'], hourly22['humidity'], hourly23['humidity'], hourly24['humidity'], hourly25['humidity'], hourly26['humidity'], hourly27['humidity'], hourly28['humidity']],
        ['precipInches', hourly21['precipInches'], hourly22['precipInches'], hourly23['precipInches'], hourly24['precipInches'], hourly25['precipInches'], hourly26['precipInches'], hourly27['precipInches'], hourly28['precipInches']],
        ['precipMM', hourly21['precipMM'], hourly22['precipMM'], hourly23['precipMM'], hourly24['precipMM'], hourly25['precipMM'], hourly26['precipMM'], hourly27['precipMM'], hourly28['precipMM']],
        ['pressure', hourly21['pressure'], hourly22['pressure'], hourly23['pressure'], hourly24['pressure'], hourly25['pressure'], hourly26['pressure'], hourly27['pressure'], hourly28['pressure']],
        ['pressureInches', hourly21['pressureInches'], hourly22['pressureInches'], hourly23['pressureInches'], hourly24['pressureInches'], hourly25['pressureInches'], hourly26['pressureInches'], hourly27['pressureInches'], hourly28['pressureInches']],
        ['shortRad', hourly21['shortRad'], hourly22['shortRad'], hourly23['shortRad'], hourly24['shortRad'], hourly25['shortRad'], hourly26['shortRad'], hourly27['shortRad'], hourly28['shortRad']],
        ['tempC', hourly21['tempC'], hourly22['tempC'], hourly23['tempC'], hourly24['tempC'], hourly25['tempC'], hourly26['tempC'], hourly27['tempC'], hourly28['tempC']],
        ['tempF', hourly21['tempF'], hourly22['tempF'], hourly23['tempF'], hourly24['tempF'], hourly25['tempF'], hourly26['tempF'], hourly27['tempF'], hourly28['tempF']],
        ['time', '0', '300', '600', '900', '1200', '1500', '1800', '2100'],
        ['uvIndex', hourly21['uvIndex'], hourly22['uvIndex'], hourly23['uvIndex'], hourly24['uvIndex'], hourly25['uvIndex'], hourly26['uvIndex'], hourly27['uvIndex'], hourly28['uvIndex']],
        ['visibility', hourly21['visibility'], hourly22['visibility'], hourly23['visibility'], hourly24['visibility'], hourly25['visibility'], hourly26['visibility'], hourly27['visibility'], hourly28['visibility']],
        ['visibilityMiles', hourly21['visibilityMiles'], hourly22['visibilityMiles'], hourly23['visibilityMiles'], hourly24['visibilityMiles'], hourly25['visibilityMiles'], hourly26['visibilityMiles'], hourly27['visibilityMiles'], hourly28['visibilityMiles']],
        ['weatherCode', hourly21['weatherCode'], hourly22['weatherCode'], hourly23['weatherCode'], hourly24['weatherCode'], hourly25['weatherCode'], hourly26['weatherCode'], hourly27['weatherCode'], hourly28['weatherCode']],
        ['weatherDesc', 'Clear ', 'Clear ', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Clear '],
        ['winddir16Point', hourly21['winddir16Point'], hourly22['winddir16Point'], hourly23['winddir16Point'], hourly24['winddir16Point'], hourly25['winddir16Point'], hourly26['winddir16Point'], hourly27['winddir16Point'], hourly28['winddir16Point']],
        ['winddirDegree', hourly21['winddirDegree'], hourly22['winddirDegree'], hourly23['winddirDegree'], hourly24['winddirDegree'], hourly25['winddirDegree'], hourly26['winddirDegree'], hourly27['winddirDegree'], hourly28['winddirDegree']],
        ['windspeedKmph', hourly21['windspeedKmph'], hourly22['windspeedKmph'], hourly23['windspeedKmph'], hourly24['windspeedKmph'], hourly25['windspeedKmph'], hourly26['windspeedKmph'], hourly27['windspeedKmph'], hourly28['windspeedKmph']],
        ['windspeedMiles', hourly21['windspeedMiles'], hourly22['windspeedMiles'], hourly23['windspeedMiles'], hourly24['windspeedMiles'], hourly25['windspeedMiles'], hourly26['windspeedMiles'], hourly27['windspeedMiles'], hourly28['windspeedMiles']]
    ]
    
    # Insert data into the treeview
    for item in data:
        tree.insert("", "end", values=item)
        
def populate_table2(tree):
    data = [
        ['DewPointC', hourly31['DewPointC'], hourly32['DewPointC'], hourly33['DewPointC'], hourly34['DewPointC'], hourly35['DewPointC'], hourly36['DewPointC'], hourly37['DewPointC'], hourly38['DewPointC']],
        ['DewPointF', hourly31['DewPointF'], hourly32['DewPointF'], hourly33['DewPointF'], hourly34['DewPointF'], hourly35['DewPointF'], hourly36['DewPointF'], hourly37['DewPointF'], hourly38['DewPointF']],
        ['FeelsLikeC', hourly31['FeelsLikeC'], hourly32['FeelsLikeC'], hourly33['FeelsLikeC'], hourly34['FeelsLikeC'], hourly35['FeelsLikeC'], hourly36['FeelsLikeC'], hourly37['FeelsLikeC'], hourly38['FeelsLikeC']],
        ['FeelsLikeF', hourly31['FeelsLikeF'], hourly32['FeelsLikeF'], hourly33['FeelsLikeF'], hourly34['FeelsLikeF'], hourly35['FeelsLikeF'], hourly36['FeelsLikeF'], hourly37['FeelsLikeF'], hourly38['FeelsLikeF']],
        ['HeatIndexC', hourly31['HeatIndexC'], hourly32['HeatIndexC'], hourly33['HeatIndexC'], hourly34['HeatIndexC'], hourly35['HeatIndexC'], hourly36['HeatIndexC'], hourly37['HeatIndexC'], hourly38['HeatIndexC']],
        ['HeatIndexF', hourly31['HeatIndexF'], hourly32['HeatIndexF'], hourly33['HeatIndexF'], hourly34['HeatIndexF'], hourly35['HeatIndexF'], hourly36['HeatIndexF'], hourly37['HeatIndexF'], hourly38['HeatIndexF']],
        ['WindChillC', hourly31['WindChillC'], hourly32['WindChillC'], hourly33['WindChillC'], hourly34['WindChillC'], hourly35['WindChillC'], hourly36['WindChillC'], hourly37['WindChillC'], hourly38['WindChillC']],
        ['WindChillF', hourly31['WindChillF'], hourly32['WindChillF'], hourly33['WindChillF'], hourly34['WindChillF'], hourly35['WindChillF'], hourly36['WindChillF'], hourly37['WindChillF'], hourly38['WindChillF']],
        ['WindGustKmph', hourly31['WindGustKmph'], hourly32['WindGustKmph'], hourly33['WindGustKmph'], hourly34['WindGustKmph'], hourly35['WindGustKmph'], hourly36['WindGustKmph'], hourly37['WindGustKmph'], hourly38['WindGustKmph']],
        ['WindGustMiles', hourly31['WindGustMiles'], hourly32['WindGustMiles'], hourly33['WindGustMiles'], hourly34['WindGustMiles'], hourly35['WindGustMiles'], hourly36['WindGustMiles'], hourly37['WindGustMiles'], hourly38['WindGustMiles']],
        ['chanceoffog', hourly31['chanceoffog'], hourly32['chanceoffog'], hourly33['chanceoffog'], hourly34['chanceoffog'], hourly35['chanceoffog'], hourly36['chanceoffog'], hourly37['chanceoffog'], hourly38['chanceoffog']],
        ['chanceoffrost', hourly31['chanceoffrost'], hourly32['chanceoffrost'], hourly33['chanceoffrost'], hourly34['chanceoffrost'], hourly35['chanceoffrost'], hourly36['chanceoffrost'], hourly37['chanceoffrost'], hourly38['chanceoffrost']],
        ['chanceofhightemp', hourly31['chanceofhightemp'], hourly32['chanceofhightemp'], hourly33['chanceofhightemp'], hourly34['chanceofhightemp'], hourly35['chanceofhightemp'], hourly36['chanceofhightemp'], hourly37['chanceofhightemp'], hourly38['chanceofhightemp']],
        ['chanceofovercast', hourly31['chanceofovercast'], hourly32['chanceofovercast'], hourly33['chanceofovercast'], hourly34['chanceofovercast'], hourly35['chanceofovercast'], hourly36['chanceofovercast'], hourly37['chanceofovercast'], hourly38['chanceofovercast']],
        ['chanceofrain', hourly31['chanceofrain'], hourly32['chanceofrain'], hourly33['chanceofrain'], hourly34['chanceofrain'], hourly35['chanceofrain'], hourly36['chanceofrain'], hourly37['chanceofrain'], hourly38['chanceofrain']],
        ['chanceofremdry', hourly31['chanceofremdry'], hourly32['chanceofremdry'], hourly33['chanceofremdry'], hourly34['chanceofremdry'], hourly35['chanceofremdry'], hourly36['chanceofremdry'], hourly37['chanceofremdry'], hourly38['chanceofremdry']],
        ['chanceofsnow', hourly31['chanceofsnow'], hourly32['chanceofsnow'], hourly33['chanceofsnow'], hourly34['chanceofsnow'], hourly35['chanceofsnow'], hourly36['chanceofsnow'], hourly37['chanceofsnow'], hourly38['chanceofsnow']],
        ['chanceofsunshine', hourly31['chanceofsunshine'], hourly32['chanceofsunshine'], hourly33['chanceofsunshine'], hourly34['chanceofsunshine'], hourly35['chanceofsunshine'], hourly36['chanceofsunshine'], hourly37['chanceofsunshine'], hourly38['chanceofsunshine']],
        ['chanceofthunder', hourly31['chanceofthunder'], hourly32['chanceofthunder'], hourly33['chanceofthunder'], hourly34['chanceofthunder'], hourly35['chanceofthunder'], hourly36['chanceofthunder'], hourly37['chanceofthunder'], hourly38['chanceofthunder']],
        ['chanceofwindy', hourly31['chanceofwindy'], hourly32['chanceofwindy'], hourly33['chanceofwindy'], hourly34['chanceofwindy'], hourly35['chanceofwindy'], hourly36['chanceofwindy'], hourly37['chanceofwindy'], hourly38['chanceofwindy']],
        ['cloudcover', hourly31['cloudcover'], hourly32['cloudcover'], hourly33['cloudcover'], hourly34['cloudcover'], hourly35['cloudcover'], hourly36['cloudcover'], hourly37['cloudcover'], hourly38['cloudcover']],
        ['diffRad', hourly31['diffRad'], hourly32['diffRad'], hourly33['diffRad'], hourly34['diffRad'], hourly35['diffRad'], hourly36['diffRad'], hourly37['diffRad'], hourly38['diffRad']],
        ['humidity', hourly31['humidity'], hourly32['humidity'], hourly33['humidity'], hourly34['humidity'], hourly35['humidity'], hourly36['humidity'], hourly37['humidity'], hourly38['humidity']],
        ['precipInches', hourly31['precipInches'], hourly32['precipInches'], hourly33['precipInches'], hourly34['precipInches'], hourly35['precipInches'], hourly36['precipInches'], hourly37['precipInches'], hourly38['precipInches']],
        ['precipMM', hourly31['precipMM'], hourly32['precipMM'], hourly33['precipMM'], hourly34['precipMM'], hourly35['precipMM'], hourly36['precipMM'], hourly37['precipMM'], hourly38['precipMM']],
        ['pressure', hourly31['pressure'], hourly32['pressure'], hourly33['pressure'], hourly34['pressure'], hourly35['pressure'], hourly36['pressure'], hourly37['pressure'], hourly38['pressure']],
        ['pressureInches', hourly31['pressureInches'], hourly32['pressureInches'], hourly33['pressureInches'], hourly34['pressureInches'], hourly35['pressureInches'], hourly36['pressureInches'], hourly37['pressureInches'], hourly38['pressureInches']],
        ['shortRad', hourly31['shortRad'], hourly32['shortRad'], hourly33['shortRad'], hourly34['shortRad'], hourly35['shortRad'], hourly36['shortRad'], hourly37['shortRad'], hourly38['shortRad']],
        ['tempC', hourly31['tempC'], hourly32['tempC'], hourly33['tempC'], hourly34['tempC'], hourly35['tempC'], hourly36['tempC'], hourly37['tempC'], hourly38['tempC']],
        ['tempF', hourly31['tempF'], hourly32['tempF'], hourly33['tempF'], hourly34['tempF'], hourly35['tempF'], hourly36['tempF'], hourly37['tempF'], hourly38['tempF']],
        ['time', '0', '300', '600', '900', '1200', '1500', '1800', '2100'],
        ['uvIndex', hourly31['uvIndex'], hourly32['uvIndex'], hourly33['uvIndex'], hourly34['uvIndex'], hourly35['uvIndex'], hourly36['uvIndex'], hourly37['uvIndex'], hourly38['uvIndex']],
        ['visibility', hourly31['visibility'], hourly32['visibility'], hourly33['visibility'], hourly34['visibility'], hourly35['visibility'], hourly36['visibility'], hourly37['visibility'], hourly38['visibility']],
        ['visibilityMiles', hourly31['visibilityMiles'], hourly32['visibilityMiles'], hourly33['visibilityMiles'], hourly34['visibilityMiles'], hourly35['visibilityMiles'], hourly36['visibilityMiles'], hourly37['visibilityMiles'], hourly38['visibilityMiles']],
        ['weatherCode', hourly31['weatherCode'], hourly32['weatherCode'], hourly33['weatherCode'], hourly34['weatherCode'], hourly35['weatherCode'], hourly36['weatherCode'], hourly37['weatherCode'], hourly38['weatherCode']],
        ['weatherDesc', 'Clear ', 'Clear ', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Clear '],
        ['winddir16Point', hourly31['winddir16Point'], hourly32['winddir16Point'], hourly33['winddir16Point'], hourly34['winddir16Point'], hourly35['winddir16Point'], hourly36['winddir16Point'], hourly37['winddir16Point'], hourly38['winddir16Point']],
        ['winddirDegree', hourly31['winddirDegree'], hourly32['winddirDegree'], hourly33['winddirDegree'], hourly34['winddirDegree'], hourly35['winddirDegree'], hourly36['winddirDegree'], hourly37['winddirDegree'], hourly38['winddirDegree']],
        ['windspeedKmph', hourly31['windspeedKmph'], hourly32['windspeedKmph'], hourly33['windspeedKmph'], hourly34['windspeedKmph'], hourly35['windspeedKmph'], hourly36['windspeedKmph'], hourly37['windspeedKmph'], hourly38['windspeedKmph']],
        ['windspeedMiles', hourly31['windspeedMiles'], hourly32['windspeedMiles'], hourly33['windspeedMiles'], hourly34['windspeedMiles'], hourly35['windspeedMiles'], hourly36['windspeedMiles'], hourly37['windspeedMiles'], hourly38['windspeedMiles']]
    ]
    
    # Insert data into the treeview
    for item in data:
        tree.insert("", "end", values=item)

def tab2info():
    global tab2canvas
    global inner2_frame
    tab2canvas=Canvas(tab2,bg='tan')
    tab2canvas.pack(side=LEFT, fill=BOTH, expand=True) 
    global scrollbar1
    scrollbar1 = Scrollbar(tab2, orient=VERTICAL, command=tab2canvas.yview)
    scrollbar1.pack(side=RIGHT, fill=Y)
    tab2canvas.config(yscrollcommand=scrollbar1.set)
    inner2_frame = Frame(tab2canvas,bg="tan")
    tab2canvas.create_window((0,0), window=inner2_frame, anchor=NW)
    inner2_frame.bind("<Configure>", on_frame_configure1)
    tab2canvas.bind("<Configure>", on_canvas_configure1)
    blanlbl=Label(inner2_frame,text="      ",bg="tan")
    blanlbl.grid(row=0,column=0)
    
    day1desc=Label(inner2_frame,text="\nDATE: "+daydesc1['date']+"\nAVERAGE TEMPERATURE: "+daydesc1['avgtempC']+"°C ("+daydesc1['avgtempF']+"°F)\nMAXIMUM TEMPERATURE: "+daydesc1['maxtempC']+"°C ("+daydesc1['maxtempF']+"°F)\nMINIMUM TEMPERATURE: "+daydesc1['mintempC']+"°C ("+daydesc1['mintempF']+"°F)\nSUN TIME: "+daydesc1['sunHour']+" hours\n",font=("times new roman",20,"bold"),bg="tan")
    day1desc.grid(row=0,column=1)
    
    tree = ttk.Treeview(inner2_frame, columns=("time(24h)", "00", "03", "06" , "09", "12", "15", "18", "21"), show="headings")
    tree.heading("time(24h)", text="time(24h)")
    tree.heading("00", text="00")
    tree.heading("03", text="03")
    tree.heading("06", text="06")
    tree.heading("09", text="09")
    tree.heading("12", text="12")
    tree.heading("15", text="15")
    tree.heading("18", text="18")
    tree.heading("21", text="21")
    tree.column("time(24h)", width=100)
    tree.column("00", width=50)
    tree.column("03", width=50)
    tree.column("06", width=50)
    tree.column("09", width=50)
    tree.column("12", width=50)
    tree.column("15", width=50)
    tree.column("18", width=50)
    tree.column("21", width=50)
    populate_table(tree)
    tree.grid(row=1,column=1)
    
    day2desc=Label(inner2_frame,text="\nDATE: "+daydesc2['date']+"\nAVERAGE TEMPERATURE: "+daydesc2['avgtempC']+"°C ("+daydesc2['avgtempF']+"°F)\nMAXIMUM TEMPERATURE: "+daydesc2['maxtempC']+"°C ("+daydesc2['maxtempF']+"°F)\nMINIMUM TEMPERATURE: "+daydesc2['mintempC']+"°C ("+daydesc2['mintempF']+"°F)\nSUN TIME: "+daydesc2['sunHour']+" hours\n",font=("times new roman",20,"bold"),bg="tan")
    day2desc.grid(row=2,column=1)
    
    tree1 = ttk.Treeview(inner2_frame, columns=("time(24h)", "00", "03", "06", "09", "12", "15", "18", "21"), show="headings")
    tree1.heading("time(24h)", text="time(24h)")
    tree1.heading("00", text="00")
    tree1.heading("03", text="03")
    tree1.heading("06", text="06")
    tree1.heading("09", text="09")
    tree1.heading("12", text="12")
    tree1.heading("15", text="15")
    tree1.heading("18", text="18")
    tree1.heading("21", text="21")
    tree1.column("time(24h)", width=100)
    tree1.column("00", width=50)
    tree1.column("03", width=50)
    tree1.column("06", width=50)
    tree1.column("09", width=50)
    tree1.column("12", width=50)
    tree1.column("15", width=50)
    tree1.column("18", width=50)
    tree1.column("21", width=50)
    populate_table1(tree1)
    tree1.grid(row=3,column=1)
    
    day3desc=Label(inner2_frame,text="\nDATE: "+daydesc3['date']+"\nAVERAGE TEMPERATURE: "+daydesc3['avgtempC']+"°C ("+daydesc3['avgtempF']+"°F)\nMAXIMUM TEMPERATURE: "+daydesc3['maxtempC']+"°C ("+daydesc3['maxtempF']+"°F)\nMINIMUM TEMPERATURE: "+daydesc3['mintempC']+"°C ("+daydesc3['mintempF']+"°F)\nSUN TIME: "+daydesc3['sunHour']+" hours\n",font=("times new roman",20,"bold"),bg="tan")
    day3desc.grid(row=4,column=1)
    
    tree2 = ttk.Treeview(inner2_frame, columns=("time(24h)", "00", "03", "06", "09", "12", "15", "18", "21"), show="headings")
    tree2.heading("time(24h)", text="time(24h)")
    tree2.heading("00", text="00")
    tree2.heading("03", text="03")
    tree2.heading("06", text="06")
    tree2.heading("09", text="09")
    tree2.heading("12", text="12")
    tree2.heading("15", text="15")
    tree2.heading("18", text="18")
    tree2.heading("21", text="21")
    tree2.column("time(24h)", width=100)
    tree2.column("00", width=50)
    tree2.column("03", width=50)
    tree2.column("06", width=50)
    tree2.column("09", width=50)
    tree2.column("12", width=50)
    tree2.column("15", width=50)
    tree2.column("18", width=50)
    tree2.column("21", width=50)
    populate_table2(tree2)
    tree2.grid(row=5,column=1)
    
    day3desc=Label(inner2_frame,text="\n",bg="tan")
    day3desc.grid(row=6,column=1)
    

def tab3info():
    global tab3canvas
    global inner_frame
    tab3canvas=Canvas(tab3,bg='cyan')
    tab3canvas.pack(side=LEFT, fill=BOTH, expand=True) 
    global scrollbar
    scrollbar = Scrollbar(tab3, orient=VERTICAL, command=tab3canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    tab3canvas.config(yscrollcommand=scrollbar.set)
    inner_frame = Frame(tab3canvas,bg="cyan")
    tab3canvas.create_window((0,0), window=inner_frame, anchor=NW)
    inner_frame.bind("<Configure>", on_frame_configure)
    tab3canvas.bind("<Configure>", on_canvas_configure)
    
    timeline = ['0', '3', '6', '9', '12', '15', '18', '21', '0', '3', '6', '9', '12', '15', '18', '21', '0', '3', '6', '9', '12', '15', '18', '21']
    degree = [hourly11['tempC'],hourly12['tempC'],hourly13['tempC'],hourly14['tempC'],hourly15['tempC'],hourly16['tempC'],hourly17['tempC'],hourly18['tempC'],hourly21['tempC'],hourly22['tempC'],hourly23['tempC'],hourly24['tempC'],hourly25['tempC'],hourly26['tempC'],hourly27['tempC'],hourly28['tempC'],hourly31['tempC'],hourly32['tempC'],hourly33['tempC'],hourly34['tempC'],hourly35['tempC'],hourly36['tempC'],hourly37['tempC'],hourly38['tempC']]
    degree= [int(x) for x in degree]
    faran = [hourly11['tempF'],hourly12['tempF'],hourly13['tempF'],hourly14['tempF'],hourly15['tempF'],hourly16['tempF'],hourly17['tempF'],hourly18['tempF'],hourly21['tempF'],hourly22['tempF'],hourly23['tempF'],hourly24['tempF'],hourly25['tempF'],hourly26['tempF'],hourly27['tempF'],hourly28['tempF'],hourly31['tempF'],hourly32['tempF'],hourly33['tempF'],hourly34['tempF'],hourly35['tempF'],hourly36['tempF'],hourly37['tempF'],hourly38['tempF']]
    faran= [int(x) for x in faran]
    humidity = [hourly11['humidity'],hourly12['humidity'],hourly13['humidity'],hourly14['humidity'],hourly15['humidity'],hourly16['humidity'],hourly17['humidity'],hourly18['humidity'],hourly21['humidity'],hourly22['humidity'],hourly23['humidity'],hourly24['humidity'],hourly25['humidity'],hourly26['humidity'],hourly27['humidity'],hourly28['humidity'],hourly31['humidity'],hourly32['humidity'],hourly33['humidity'],hourly34['humidity'],hourly35['humidity'],hourly36['humidity'],hourly37['humidity'],hourly38['humidity']]
    humidity= [int(x) for x in humidity]
    precimm = [hourly11['precipMM'],hourly12['precipMM'],hourly13['precipMM'],hourly14['precipMM'],hourly15['precipMM'],hourly16['precipMM'],hourly17['precipMM'],hourly18['precipMM'],hourly21['precipMM'],hourly22['precipMM'],hourly23['precipMM'],hourly24['precipMM'],hourly25['precipMM'],hourly26['precipMM'],hourly27['precipMM'],hourly28['precipMM'],hourly31['precipMM'],hourly32['precipMM'],hourly33['precipMM'],hourly34['precipMM'],hourly35['precipMM'],hourly36['precipMM'],hourly37['precipMM'],hourly38['precipMM']]
    precimm= [float(x) for x in precimm]
    preciin = [hourly11['precipInches'],hourly12['precipInches'],hourly13['precipInches'],hourly14['precipInches'],hourly15['precipInches'],hourly16['precipInches'],hourly17['precipInches'],hourly18['precipInches'],hourly21['precipInches'],hourly22['precipInches'],hourly23['precipInches'],hourly24['precipInches'],hourly25['precipInches'],hourly26['precipInches'],hourly27['precipInches'],hourly28['precipInches'],hourly31['precipInches'],hourly32['precipInches'],hourly33['precipInches'],hourly34['precipInches'],hourly35['precipInches'],hourly36['precipInches'],hourly37['precipInches'],hourly38['precipInches']]
    preciin= [float(x) for x in preciin]
    cldcvr=[hourly11['cloudcover'],hourly12['cloudcover'],hourly13['cloudcover'],hourly14['cloudcover'],hourly15['cloudcover'],hourly16['cloudcover'],hourly17['cloudcover'],hourly18['cloudcover'],hourly21['cloudcover'],hourly22['cloudcover'],hourly23['cloudcover'],hourly24['cloudcover'],hourly25['cloudcover'],hourly26['cloudcover'],hourly27['cloudcover'],hourly28['cloudcover'],hourly31['cloudcover'],hourly32['cloudcover'],hourly33['cloudcover'],hourly34['cloudcover'],hourly35['cloudcover'],hourly36['cloudcover'],hourly37['cloudcover'],hourly38['cloudcover']]
    cldcvr= [int(x) for x in cldcvr]
    viskm=[hourly11['visibility'],hourly12['visibility'],hourly13['visibility'],hourly14['visibility'],hourly15['visibility'],hourly16['visibility'],hourly17['visibility'],hourly18['visibility'],hourly21['visibility'],hourly22['visibility'],hourly23['visibility'],hourly24['visibility'],hourly25['visibility'],hourly26['visibility'],hourly27['visibility'],hourly28['visibility'],hourly31['visibility'],hourly32['visibility'],hourly33['visibility'],hourly34['visibility'],hourly35['visibility'],hourly36['visibility'],hourly37['visibility'],hourly38['visibility']]
    viskm= [int(x) for x in viskm]
    vismi=[hourly11['visibilityMiles'],hourly12['visibilityMiles'],hourly13['visibilityMiles'],hourly14['visibilityMiles'],hourly15['visibilityMiles'],hourly16['visibilityMiles'],hourly17['visibilityMiles'],hourly18['visibilityMiles'],hourly21['visibilityMiles'],hourly22['visibilityMiles'],hourly23['visibilityMiles'],hourly24['visibilityMiles'],hourly25['visibilityMiles'],hourly26['visibilityMiles'],hourly27['visibilityMiles'],hourly28['visibilityMiles'],hourly31['visibilityMiles'],hourly32['visibilityMiles'],hourly33['visibilityMiles'],hourly34['visibilityMiles'],hourly35['visibilityMiles'],hourly36['visibilityMiles'],hourly37['visibilityMiles'],hourly38['visibilityMiles']]
    vismi= [int(x) for x in vismi]
    uvindx=[hourly11['uvIndex'],hourly12['uvIndex'],hourly13['uvIndex'],hourly14['uvIndex'],hourly15['uvIndex'],hourly16['uvIndex'],hourly17['uvIndex'],hourly18['uvIndex'],hourly21['uvIndex'],hourly22['uvIndex'],hourly23['uvIndex'],hourly24['uvIndex'],hourly25['uvIndex'],hourly26['uvIndex'],hourly27['uvIndex'],hourly28['uvIndex'],hourly31['uvIndex'],hourly32['uvIndex'],hourly33['uvIndex'],hourly34['uvIndex'],hourly35['uvIndex'],hourly36['uvIndex'],hourly37['uvIndex'],hourly38['uvIndex']]
    uvindx= [int(x) for x in uvindx]
    prsurmb=[hourly11['pressure'],hourly12['pressure'],hourly13['pressure'],hourly14['pressure'],hourly15['pressure'],hourly16['pressure'],hourly17['pressure'],hourly18['pressure'],hourly21['pressure'],hourly22['pressure'],hourly23['pressure'],hourly24['pressure'],hourly25['pressure'],hourly26['pressure'],hourly27['pressure'],hourly28['pressure'],hourly31['pressure'],hourly32['pressure'],hourly33['pressure'],hourly34['pressure'],hourly35['pressure'],hourly36['pressure'],hourly37['pressure'],hourly38['pressure']]
    prsurmb= [int(x) for x in prsurmb]
    fog=[hourly11['chanceoffog'],hourly12['chanceoffog'],hourly13['chanceoffog'],hourly14['chanceoffog'],hourly15['chanceoffog'],hourly16['chanceoffog'],hourly17['chanceoffog'],hourly18['chanceoffog'],hourly21['chanceoffog'],hourly22['chanceoffog'],hourly23['chanceoffog'],hourly24['chanceoffog'],hourly25['chanceoffog'],hourly26['chanceoffog'],hourly27['chanceoffog'],hourly28['chanceoffog'],hourly31['chanceoffog'],hourly32['chanceoffog'],hourly33['chanceoffog'],hourly34['chanceoffog'],hourly35['chanceoffog'],hourly36['chanceoffog'],hourly37['chanceoffog'],hourly38['chanceoffog']]
    fog= [int(x) for x in fog]
    frost=[hourly11['chanceoffrost'],hourly12['chanceoffrost'],hourly13['chanceoffrost'],hourly14['chanceoffrost'],hourly15['chanceoffrost'],hourly16['chanceoffrost'],hourly17['chanceoffrost'],hourly18['chanceoffrost'],hourly21['chanceoffrost'],hourly22['chanceoffrost'],hourly23['chanceoffrost'],hourly24['chanceoffrost'],hourly25['chanceoffrost'],hourly26['chanceoffrost'],hourly27['chanceoffrost'],hourly28['chanceoffrost'],hourly31['chanceoffrost'],hourly32['chanceoffrost'],hourly33['chanceoffrost'],hourly34['chanceoffrost'],hourly35['chanceoffrost'],hourly36['chanceoffrost'],hourly37['chanceoffrost'],hourly38['chanceoffrost']]
    frost= [int(x) for x in frost]
    hightemp=[hourly11['chanceofhightemp'],hourly12['chanceofhightemp'],hourly13['chanceofhightemp'],hourly14['chanceofhightemp'],hourly15['chanceofhightemp'],hourly16['chanceofhightemp'],hourly17['chanceofhightemp'],hourly18['chanceofhightemp'],hourly21['chanceofhightemp'],hourly22['chanceofhightemp'],hourly23['chanceofhightemp'],hourly24['chanceofhightemp'],hourly25['chanceofhightemp'],hourly26['chanceofhightemp'],hourly27['chanceofhightemp'],hourly28['chanceofhightemp'],hourly31['chanceofhightemp'],hourly32['chanceofhightemp'],hourly33['chanceofhightemp'],hourly34['chanceofhightemp'],hourly35['chanceofhightemp'],hourly36['chanceofhightemp'],hourly37['chanceofhightemp'],hourly38['chanceofhightemp']]
    hightemp= [int(x) for x in hightemp]
    ocsk=[hourly11['chanceofovercast'],hourly12['chanceofovercast'],hourly13['chanceofovercast'],hourly14['chanceofovercast'],hourly15['chanceofovercast'],hourly16['chanceofovercast'],hourly17['chanceofovercast'],hourly18['chanceofovercast'],hourly21['chanceofovercast'],hourly22['chanceofovercast'],hourly23['chanceofovercast'],hourly24['chanceofovercast'],hourly25['chanceofovercast'],hourly26['chanceofovercast'],hourly27['chanceofovercast'],hourly28['chanceofovercast'],hourly31['chanceofovercast'],hourly32['chanceofovercast'],hourly33['chanceofovercast'],hourly34['chanceofovercast'],hourly35['chanceofovercast'],hourly36['chanceofovercast'],hourly37['chanceofovercast'],hourly38['chanceofovercast']]
    ocsk= [int(x) for x in ocsk]
    crain=[hourly11['chanceofrain'],hourly12['chanceofrain'],hourly13['chanceofrain'],hourly14['chanceofrain'],hourly15['chanceofrain'],hourly16['chanceofrain'],hourly17['chanceofrain'],hourly18['chanceofrain'],hourly21['chanceofrain'],hourly22['chanceofrain'],hourly23['chanceofrain'],hourly24['chanceofrain'],hourly25['chanceofrain'],hourly26['chanceofrain'],hourly27['chanceofrain'],hourly28['chanceofrain'],hourly31['chanceofrain'],hourly32['chanceofrain'],hourly33['chanceofrain'],hourly34['chanceofrain'],hourly35['chanceofrain'],hourly36['chanceofrain'],hourly37['chanceofrain'],hourly38['chanceofrain']]
    crain= [int(x) for x in crain]
    remdry=[hourly11['chanceofremdry'],hourly12['chanceofremdry'],hourly13['chanceofremdry'],hourly14['chanceofremdry'],hourly15['chanceofremdry'],hourly16['chanceofremdry'],hourly17['chanceofremdry'],hourly18['chanceofremdry'],hourly21['chanceofremdry'],hourly22['chanceofremdry'],hourly23['chanceofremdry'],hourly24['chanceofremdry'],hourly25['chanceofremdry'],hourly26['chanceofremdry'],hourly27['chanceofremdry'],hourly28['chanceofremdry'],hourly31['chanceofremdry'],hourly32['chanceofremdry'],hourly33['chanceofremdry'],hourly34['chanceofremdry'],hourly35['chanceofremdry'],hourly36['chanceofremdry'],hourly37['chanceofremdry'],hourly38['chanceofremdry']]
    remdry= [int(x) for x in remdry]
    csnow=[hourly11['chanceofsnow'],hourly12['chanceofsnow'],hourly13['chanceofsnow'],hourly14['chanceofsnow'],hourly15['chanceofsnow'],hourly16['chanceofsnow'],hourly17['chanceofsnow'],hourly18['chanceofsnow'],hourly21['chanceofsnow'],hourly22['chanceofsnow'],hourly23['chanceofsnow'],hourly24['chanceofsnow'],hourly25['chanceofsnow'],hourly26['chanceofsnow'],hourly27['chanceofsnow'],hourly28['chanceofsnow'],hourly31['chanceofsnow'],hourly32['chanceofsnow'],hourly33['chanceofsnow'],hourly34['chanceofsnow'],hourly35['chanceofsnow'],hourly36['chanceofsnow'],hourly37['chanceofsnow'],hourly38['chanceofsnow']]
    csnow= [int(x) for x in csnow]
    thndr=[hourly11['chanceofthunder'],hourly12['chanceofthunder'],hourly13['chanceofthunder'],hourly14['chanceofthunder'],hourly15['chanceofthunder'],hourly16['chanceofthunder'],hourly17['chanceofthunder'],hourly18['chanceofthunder'],hourly21['chanceofthunder'],hourly22['chanceofthunder'],hourly23['chanceofthunder'],hourly24['chanceofthunder'],hourly25['chanceofthunder'],hourly26['chanceofthunder'],hourly27['chanceofthunder'],hourly28['chanceofthunder'],hourly31['chanceofthunder'],hourly32['chanceofthunder'],hourly33['chanceofthunder'],hourly34['chanceofthunder'],hourly35['chanceofthunder'],hourly36['chanceofthunder'],hourly37['chanceofthunder'],hourly38['chanceofthunder']]
    thndr= [int(x) for x in thndr]
    sunsh=[hourly11['chanceofsunshine'],hourly12['chanceofsunshine'],hourly13['chanceofsunshine'],hourly14['chanceofsunshine'],hourly15['chanceofsunshine'],hourly16['chanceofsunshine'],hourly17['chanceofsunshine'],hourly18['chanceofsunshine'],hourly21['chanceofsunshine'],hourly22['chanceofsunshine'],hourly23['chanceofsunshine'],hourly24['chanceofsunshine'],hourly25['chanceofsunshine'],hourly26['chanceofsunshine'],hourly27['chanceofsunshine'],hourly28['chanceofsunshine'],hourly31['chanceofsunshine'],hourly32['chanceofsunshine'],hourly33['chanceofsunshine'],hourly34['chanceofsunshine'],hourly35['chanceofsunshine'],hourly36['chanceofsunshine'],hourly37['chanceofsunshine'],hourly38['chanceofsunshine']]
    sunsh= [int(x) for x in sunsh]
    windy=[hourly11['chanceofwindy'],hourly12['chanceofwindy'],hourly13['chanceofwindy'],hourly14['chanceofwindy'],hourly15['chanceofwindy'],hourly16['chanceofwindy'],hourly17['chanceofwindy'],hourly18['chanceofwindy'],hourly21['chanceofwindy'],hourly22['chanceofwindy'],hourly23['chanceofwindy'],hourly24['chanceofwindy'],hourly25['chanceofwindy'],hourly26['chanceofwindy'],hourly27['chanceofwindy'],hourly28['chanceofwindy'],hourly31['chanceofwindy'],hourly32['chanceofwindy'],hourly33['chanceofwindy'],hourly34['chanceofwindy'],hourly35['chanceofwindy'],hourly36['chanceofwindy'],hourly37['chanceofwindy'],hourly38['chanceofwindy']]
    windy= [int(x) for x in windy]
    
    secondary_ticks = [0, 8, 16, 23]  
    daylis = [daydesc1['date'],daydesc2['date'], daydesc3['date'], '']
    
    fig1 = Figure(figsize=(6, 4.5), dpi=100,facecolor="cyan")
    df = fig1.add_subplot(111)
    df.plot(range(len(timeline)), faran, label='°F')
    df.plot(range(len(timeline)), degree, label='°C')
    df.set_xticks(range(len(timeline)))
    df.set_xticklabels(timeline)
    for tick, label in zip(secondary_ticks, daylis):
        df.axvline(x=tick, color='lightgrey', linestyle='--')
    df.set_xlabel('time')
    df.set_ylabel('temperature')
    df.set_title('temperature span for 3 days\n  '+daylis[0]+"         "+daylis[1]+"        "+daylis[2])
    df.legend()
    dfcanvas = FigureCanvasTkAgg(fig1, master=inner_frame)
    dfcanvas.draw()
    dfcanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    fig2 = Figure(figsize=(6, 4.5), dpi=100,facecolor="cyan")
    hm= fig2.add_subplot(111)
    hm.plot(range(len(timeline)), humidity)
    hm.set_xticks(range(len(timeline)))
    hm.set_xticklabels(timeline)
    for tick, label in zip(secondary_ticks, daylis):
        hm.axvline(x=tick, color='lightgrey', linestyle='--')
    hm.set_xlabel('time')
    hm.set_ylabel('humidity(%)')
    hm.set_title('humidity span for 3 days\n  '+daylis[0]+"         "+daylis[1]+"        "+daylis[2])
    hm.legend()
    hmcanvas = FigureCanvasTkAgg(fig2, master=inner_frame)
    hmcanvas.draw()
    hmcanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    fig3 = Figure(figsize=(6, 4.5), dpi=100,facecolor="cyan")
    cc= fig3.add_subplot(111)
    cc.plot(range(len(timeline)), cldcvr)
    cc.set_xticks(range(len(timeline)))
    cc.set_xticklabels(timeline)
    for tick, label in zip(secondary_ticks, daylis):
        cc.axvline(x=tick, color='lightgrey', linestyle='--')
    cc.set_xlabel('time')
    cc.set_ylabel('cloud cover(%)')
    cc.set_title('cloud coverage span for 3 days\n  '+daylis[0]+"         "+daylis[1]+"        "+daylis[2])
    cc.legend()
    cccanvas = FigureCanvasTkAgg(fig3, master=inner_frame)
    cccanvas.draw()
    cccanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    fig4 = Figure(figsize=(6, 4.5), dpi=100,facecolor="cyan")
    pr = fig4.add_subplot(111)
    pr.plot(range(len(timeline)), precimm, label='millimeters')
    pr.plot(range(len(timeline)), preciin, label='inches')
    pr.set_xticks(range(len(timeline)))
    pr.set_xticklabels(timeline)
    for tick, label in zip(secondary_ticks, daylis):
        pr.axvline(x=tick, color='lightgrey', linestyle='--')
    pr.set_xlabel('time')
    pr.set_ylabel('precipitation(%)')
    pr.set_title('precipitation span for 3 days\n  '+daylis[0]+"         "+daylis[1]+"        "+daylis[2])
    pr.legend()
    prcanvas = FigureCanvasTkAgg(fig4, master=inner_frame)
    prcanvas.draw()
    prcanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    fig5 = Figure(figsize=(6, 4.5), dpi=100,facecolor="cyan")
    vs = fig5.add_subplot(111)
    vs.plot(range(len(timeline)), viskm, label='kilometers')
    vs.plot(range(len(timeline)), vismi, label='miles')
    vs.set_xticks(range(len(timeline)))
    vs.set_xticklabels(timeline)
    for tick, label in zip(secondary_ticks, daylis):
        vs.axvline(x=tick, color='lightgrey', linestyle='--')
    vs.set_xlabel('time')
    vs.set_ylabel('visibility')
    vs.set_title('visibility span for 3 days\n  '+daylis[0]+"         "+daylis[1]+"        "+daylis[2])
    vs.legend()
    vscanvas = FigureCanvasTkAgg(fig5, master=inner_frame)
    vscanvas.draw()
    vscanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    fig6 = Figure(figsize=(6, 4.5), dpi=100,facecolor="cyan")
    uv= fig6.add_subplot(111)
    uv.plot(range(len(timeline)), uvindx)
    uv.set_xticks(range(len(timeline)))
    uv.set_xticklabels(timeline)
    for tick, label in zip(secondary_ticks, daylis):
        uv.axvline(x=tick, color='lightgrey', linestyle='--')
    uv.set_xlabel('time')
    uv.set_ylabel('UV index')
    uv.set_title('UV index span for 3 days\n  '+daylis[0]+"         "+daylis[1]+"        "+daylis[2])
    uv.legend()
    uvcanvas = FigureCanvasTkAgg(fig6, master=inner_frame)
    uvcanvas.draw()
    uvcanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    fig7 = Figure(figsize=(6, 4.5), dpi=100,facecolor="cyan")
    pe= fig7.add_subplot(111)
    pe.plot(range(len(timeline)), prsurmb)
    pe.set_xticks(range(len(timeline)))
    pe.set_xticklabels(timeline)
    for tick, label in zip(secondary_ticks, daylis):
        pe.axvline(x=tick, color='lightgrey', linestyle='--')
    pe.set_xlabel('time')
    pe.set_ylabel('pressure (millibars)')
    pe.set_title('pressure span for 3 days\n  '+daylis[0]+"         "+daylis[1]+"        "+daylis[2])
    pe.legend()
    pecanvas = FigureCanvasTkAgg(fig7, master=inner_frame)
    pecanvas.draw()
    pecanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    fig8 = Figure(figsize=(6, 4.5), dpi=100,facecolor="cyan")
    cs = fig8.add_subplot(111)
    cs.plot(range(len(timeline)), fog, label='fog')
    cs.plot(range(len(timeline)), frost, label='frost')
    cs.plot(range(len(timeline)), hightemp, label='higest temperature')
    cs.plot(range(len(timeline)), ocsk, label='overcast skies')
    cs.plot(range(len(timeline)), crain , label='rain')
    cs.plot(range(len(timeline)), remdry , label='remaining dry')
    cs.plot(range(len(timeline)), csnow , label='snow')
    cs.plot(range(len(timeline)), thndr , label='thunder')
    cs.plot(range(len(timeline)), sunsh , label='sunshine')
    cs.plot(range(len(timeline)), windy, label='windy')
    cs.set_xticks(range(len(timeline)))
    cs.set_xticklabels(timeline)
    for tick, label in zip(secondary_ticks, daylis):
        cs.axvline(x=tick, color='lightgrey', linestyle='--')
    cs.set_xlabel('time')
    cs.set_ylabel('Atmospheric(%)')
    cs.set_title('Atmospheric chances span for 3 days\n  '+daylis[0]+"         "+daylis[1]+"        "+daylis[2])
    cs.legend()
    cscanvas = FigureCanvasTkAgg(fig8, master=inner_frame)
    cscanvas.draw()
    cscanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
def tab4info():
    global tab4canvas
    tab4canvas=Canvas(tab4,bg='navy blue')
    tab4canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    if astro1['moon_phase']=="New Moon":
        moonlogo=Label(tab4canvas,text="🌑",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=30)
    elif astro1['moon_phase']=="Waxing Crescent":
        moonlogo=Label(tab4canvas,text="🌒",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=30)
    elif astro1['moon_phase']=="First Quarter":
        moonlogo=Label(tab4canvas,text="🌓",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=30)
    elif astro1['moon_phase']=="Waxing Gibbous":
        moonlogo=Label(tab4canvas,text="🌔",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=30)
    elif astro1['moon_phase']=="Full Moon":
        moonlogo=Label(tab4canvas,text="🌕",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=30)
    elif astro1['moon_phase']=="Waning Gibbous":
        moonlogo=Label(tab4canvas,text="🌖",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=30)
    elif astro1['moon_phase']=="Last Quarter":
        moonlogo=Label(tab4canvas,text="🌗",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=30)
    elif astro1['moon_phase']=="Waning Crescent":
        moonlogo=Label(tab4canvas,text="🌘",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=30)
        
    if astro2['moon_phase']=="New Moon":
        moonlogo=Label(tab4canvas,text="🌑",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=260)
    elif astro2['moon_phase']=="Waxing Crescent":
        moonlogo=Label(tab4canvas,text="🌒",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=260)
    elif astro2['moon_phase']=="First Quarter":
        moonlogo=Label(tab4canvas,text="🌓",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=260)
    elif astro2['moon_phase']=="Waxing Gibbous":
        moonlogo=Label(tab4canvas,text="🌔",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=260)
    elif astro2['moon_phase']=="Full Moon":
        moonlogo=Label(tab4canvas,text="🌕",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=260)
    elif astro2['moon_phase']=="Waning Gibbous":
        moonlogo=Label(tab4canvas,text="🌖",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=260)
    elif astro2['moon_phase']=="Last Quarter":
        moonlogo=Label(tab4canvas,text="🌗",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=260)
    elif astro2['moon_phase']=="Waning Crescent":
        moonlogo=Label(tab4canvas,text="🌘",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=260)
    
    if astro3['moon_phase']=="New Moon":
        moonlogo=Label(tab4canvas,text="🌑",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=480)
    elif astro3['moon_phase']=="Waxing Crescent":
        moonlogo=Label(tab4canvas,text="🌒",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=480)
    elif astro3['moon_phase']=="First Quarter":
        moonlogo=Label(tab4canvas,text="🌓",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=480)
    elif astro3['moon_phase']=="Waxing Gibbous":
        moonlogo=Label(tab4canvas,text="🌔",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=480)
    elif astro3['moon_phase']=="Full Moon":
        moonlogo=Label(tab4canvas,text="🌕",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=480)
    elif astro3['moon_phase']=="Waning Gibbous":
        moonlogo=Label(tab4canvas,text="🌖",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=480)
    elif astro3['moon_phase']=="Last Quarter":
        moonlogo=Label(tab4canvas,text="🌗",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=480)
    elif astro3['moon_phase']=="Waning Crescent":
        moonlogo=Label(tab4canvas,text="🌘",font=('Segoe UI Emoji', 100),bg="navy blue",fg="white")
        moonlogo.place(x=80,y=480)
    
    todaylabel=Label(tab4canvas,text="TODAY\nmoon illumination: "+astro1['moon_illumination']+"%\nmoon phase: "+astro1['moon_phase']+"\nmoonrise: "+astro1['moonrise']+"\nmoonset: "+astro1['moonset']+"\nsunrise: "+astro1['sunrise']+"\nsunset: "+astro1['sunset'],font=("times new roman",12,"bold"),bg="navy blue",fg="white")
    todaylabel.place(x=300,y=60)
    tomolabel=Label(tab4canvas,text="TOMMOROW\nmoon illumination: "+astro2['moon_illumination']+"%\nmoon phase: "+astro2['moon_phase']+"\nmoonrise: "+astro2['moonrise']+"\nmoonset: "+astro2['moonset']+"\nsunrise: "+astro2['sunrise']+"\nsunset: "+astro2['sunset'],font=("times new roman",12,"bold"),bg="navy blue",fg="white")
    tomolabel.place(x=300,y=290)
    dayafterlabel=Label(tab4canvas,text="DAY AFTER TOMORROW\nmoon illumination: "+astro3['moon_illumination']+"%\nmoon phase: "+astro3['moon_phase']+"\nmoonrise: "+astro3['moonrise']+"\nmoonset: "+astro3['moonset']+"\nsunrise: "+astro3['sunrise']+"\nsunset: "+astro3['sunset'],font=("times new roman",12,"bold"),bg="navy blue",fg="white")
    dayafterlabel.place(x=300,y=510)
    
def mainrun():
    root=Tk()
    root.title("MYWEATHER")
    root.geometry("600x800")
    root.maxsize(600,800)
    root.minsize(600,800)
    root.configure(bg="orange")
    
    style = ttk.Style()
    style.theme_create('custom_style', parent='alt', settings={
        "TNotebook.Tab": {
            "configure": {"background": "black", "font": ('times new roman', 15,"bold"),"foreground":"white"},
            "map": {"background": [("selected", "red")]}}})
    style.theme_use('custom_style')

    textcity=Label(root,text="search city",font=("times new roman",15,"bold"),fg="black",bg="orange")
    textcity.place(x=25,y=10)
    global entercity
    entercity=Entry(root,font=("times new roman",15,"bold"),width=29,bg="powder blue")
    entercity.place(x=130,y=10)
    citysearch=Button(root,text="SEARCH",font=("times new roman",15,"bold"),fg="white",bg="black",command=searchcity)
    citysearch.place(x=465,y=10,height=25,width=100)

    note=ttk.Notebook(root)
    note.place(x=0,y=50,height=750,width=600)
    global tab1,tab2,tab3,tab4
    tab1 = ttk.Frame(note)
    tab2 = ttk.Frame(note)
    tab3 = ttk.Frame(note)
    tab4 = ttk.Frame(note)
    note.add(tab1, text="     CURRENT     ")
    note.add(tab2, text="      HOURLY      ")
    note.add(tab3, text="     GRAPH       ")
    note.add(tab4, text="    ASTRONOMY    ")
    
    
    cityname("")
    root.mainloop()

mainrun()


