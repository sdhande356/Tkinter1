##Temperature converter using Tkinter
##Fahrenheit to degree celcius
import tkinter
window=tkinter.Tk() #created window
window.geometry("400x500")#set dimension
window.title("Temperature Converter")#giben title
def fahren_to_cels():#function
    fahren=temp_entry.get()
    cels=(5/9)*(float(fahren)-32)
    result_label.config(text=round(cels,2))

temp_label=tkinter.Label(text="Temperatute in fahrenheit: ")
temp_entry=tkinter.Entry(width=10,font="Arial")
unit_of_label=tkinter.Label(text="\N{DEGREE FAHRENHEIT}")
cels_label=tkinter.Label(text="Temperatute to celesius: ")
result_label=tkinter.Label()
unit_c_label=tkinter.Label(text="\N{DEGREE CELSIUS}")
convert_btn=tkinter.Button(text="convert to \N{DEGREE CELSIUS}",command=fahren_to_cels)

temp_label.grid(row=0,column=0,pady=2)
temp_entry.grid(row=0,column=1,pady=2)
unit_of_label.grid(row=0,column=2,pady=2)
cels_label.grid(row=1,column=0,pady=2)
result_label.grid(row=1,column=1,pady=2)
unit_c_label.grid(row=1,column=2,pady=2)
convert_btn.grid(row=2,column=1,pady=2)
window.mainloop()