from tkinter import *
from PIL import ImageTk,Image
from datetime import date
import requests
import json

root = Tk()
root.title("Weather App")
root.geometry("350x600")
color_primary = "#0d0b2e"
color_white = "white"
root.configure(background=color_primary)



def search():

    #connecting to api
    apikey = f"http://api.weatherapi.com/v1/current.json?key=a5b634c8339b46b5a60161317203110&q=f'{city.get()}'"

    api_request = requests.get(apikey)
    api_response = json.loads(api_request.content)
    city_name = api_response["location"]["name"]
    country_name = api_response["location"]["country"]
    temp_c = api_response["current"]["temp_c"]


    city.delete(0,END)

    

    #day
    today = date.today()
    #images
    night_img = ImageTk.PhotoImage(Image.open("Night.jpg"))
    celsius_icon =  ImageTk.PhotoImage(Image.open("celsius.png"))
    rain_icon = ImageTk.PhotoImage(Image.open("rain.png"))
    # sun_icon = ImageTk.PhotoImage(Image.open("sun.png"))



    #labels
    #images
    night_img_label = Label(image=night_img)
    celsius_icon_label = Label(bg=color_primary,image=celsius_icon)
    rain_icon_label = Label(bg=color_primary,image=rain_icon)
    # sun_icon_label = Label(bg=color_primary,image=sun_icon)


    #texts
    Today_label = Label(root,text="Today",fg=color_white,bg=color_primary,font=30)
    today_label = Label(root,fg=color_white,bg=color_primary,text=today.strftime("%a, %d %b"))
    temp_label = Label(root,bg=color_primary,fg=color_white,text=temp_c,)
    cityAndCountry_label = Label(root,fg=color_white,bg=color_primary,text=f"{city_name}, {country_name} ")
    #images display
    night_img_label.place(x=49,y=280)
    rain_icon_label.place(x=116,y=100)
    Today_label.place(x=150,y=100)
    today_label.place(x=150,y=120)
    temp_label.place(x=116,y=170)
    celsius_icon_label.place(x=200,y=170)
    cityAndCountry_label.place(x=116,y=250)



#setup

#search box and button
city = Entry(root,width=45)
city.grid(row=0,column=0,pady=5,padx=2,columnspan=2)
search_btn = Button(root,text='Search',command=search)
search_btn.grid(row=0,column=2,pady=5)



root.mainloop()