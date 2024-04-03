#  The school Project

from tkinter import *
from PIL import ImageTk, Image, ImageGrab
import mysql.connector

def submit():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="voting"
    )
     #  Retrieve selected food items

    breakfast_selection = variable.get()
    breakfast_selection1 = variable1.get()
    breakfast_selection2 = variable2.get()
    breakfast_selection3 = variable3.get()
    breakfast_selection4 = variable4.get()
    breakfast_selection5 = variable5.get()
    breakfast_selection6 = variable6.get()
    lunch_selection = Lunch.get()
    lunch_selection1 = Lunch1.get()
    lunch_selection2 = Lunch3.get()
    lunch_selection3 = Lunch4.get()
    lunch_selection4 = Lunch5.get()
    lunch_selection5 = Lunch6.get()
    lunch_selection6 = Lunch7.get()
    supper_selection = supper.get()
    supper_selection1 = supper1.get()
    supper_selection2 = supper2.get()
    supper_selection3 = supper3.get()
    supper_selection4 = supper4.get()
    supper_selection5 = supper5.get()
    supper_selection6 = supper6.get()
    cursor = db.cursor()
    sql = "INSERT INTO daytinme (Monday_Breakfast,Monday_Lunch, Monday_Supper, Tuesday_Breakfast, Tuesday_Lunch, Tuesday_Supper, Wednesday_Breakfast, Wednesday_Lunch, Wednesday_Supper, Thursday_Breakfast,Thursday_Lunch, Thursday_Supper, Friday_Breakfast, Friday_Lunch, Friday_Supper, Saturday_Breakfast, Saturday_Lunch, Saturday_Supper,Sunday_Breakfast,Sunday_Lunch, Sunday_Supper) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val =(breakfast_selection, lunch_selection, supper_selection, breakfast_selection1, lunch_selection1,supper_selection1, breakfast_selection2, lunch_selection2, supper_selection2, breakfast_selection3, lunch_selection3, supper_selection3, breakfast_selection4, lunch_selection4, supper_selection4,  breakfast_selection5, lunch_selection5,  supper_selection5, breakfast_selection6, lunch_selection6, supper_selection6)


    try:
        cursor.execute(sql, val)

        db.commit()

        db.close()
        print("Data inserted successfully")

    except mysql.connector.Error as err:

        db.rollback()
        print("Error:", err)

    finally:
        cursor.close()
        db.close()

    return True
    # creating Animations




root = Tk()
root.title('School Menu')
root.configure(bg='#fffada')



# creating an animation



var = StringVar()

bg1_img =Image.open(r'C:\Users\ASA\Downloads\handy.jpg')

background1 = ImageTk.PhotoImage(bg1_img)
bg_lable1 = Label(root, image=background1)
bg_lable1.place(x=0, y=0, relwidth=1, relheight=1)

bg_img =Image.open(r'C:\Users\ASA\Downloads\th.jpeg')
bg_img = bg_img.resize((200, 170))
background = ImageTk.PhotoImage(bg_img)

bg1_img.paste(bg_img, (1390, 200))
background1_combined = ImageTk.PhotoImage(bg1_img)
combined_label = Label(root, image=background1_combined)
combined_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(root, text='AFRICAN SCIENCE ACADEMY WEEKLY MENU', font=('Impact', 35, 'bold'), fg='Darkblue').place(x=340, y=20)
label = Label(root, text="Please fill the forms", font=('Georgia', 15), fg='Darkblue')
label.place(x=670, y=90)



name = Label(root, text="Name  :", fg='Darkblue', font=('Gouldy old style', 15, 'bold'))
name.place(x=400, y=130)
email = Label(root, text="email  :", fg='Darkblue', font=('Gouldy old style', 15, 'bold'))
email.place(x=400, y=170)

namevalue = StringVar
emailvalue = StringVar


nameentry = Entry(root, textvariable=namevalue, bg='#F8EFEC', fg='black', width=30, font=('Georgia', 15))
nameentry.place(x=500, y=130)

emailentry = Entry(root, textvariable=emailvalue, bg='#F8EFEC', fg='black', width=30, font=('Georgia', 15))
emailentry.place(x=500, y=170)


Lg_frame = Frame(root, bg='Pink', width=1500, height=2000)
Lg_frame.place(x=10, y=210)



# creating animation

imgb = Image.open(r"C:\Users\ASA\Downloads\Br5.jpg")
imgb = imgb.resize((1500, 2000))
bga = ImageTk.PhotoImage(imgb)

imgc = Image.open(r"C:\Users\ASA\Downloads\s1.jpg")
imgc = imgc.resize((1500, 2000))
bgb = ImageTk.PhotoImage(imgc)

imgd = Image.open(r"C:\Users\ASA\Downloads\s6.jpg")
imgd = imgd.resize((1500, 2000))
bgc = ImageTk.PhotoImage(imgd)

l =Label(Lg_frame)
l.pack()

x = 1

def move():
    global x
    if x == 4:
        x = 1
    if x == 1:
        l.config(image=bga)

    elif x== 2:
        l.config(image=bgb)
    elif x== 3:
        l.config(image=bgc)

    x = x+1

    root.after(2000, move)

move()


br_frame = Frame(Lg_frame, bg='#fbfcf7', width=100, height=150)
br_frame.place(x=0, y=60)
lc_frame = Frame(Lg_frame, bg='#faf3eb', width=180, height=150)
lc_frame.place(x=100, y=60)
sp_frame = Frame(Lg_frame, bg='#f8efec', width=180, height=150)
sp_frame.place(x=280, y=60)

sn_frame = Frame(Lg_frame, bg='#faf5df', width=180, height=150)
sn_frame.place(x=460, y=60)

se_frame = Frame(Lg_frame, bg='#fffefc', width=180, height=150)
se_frame.place(x=640, y=60)

sa_frame = Frame(Lg_frame, bg='#e7decc', width=180, height=150)
sa_frame.place(x=820, y=60)

st_frame = Frame(Lg_frame, bg='#fff1e6', width=180, height=150)
st_frame.place(x=1000, y=60)

sy_frame = Frame(Lg_frame, bg='#fbfcf7', width=180, height=150)
sy_frame.place(x=1180, y=60)


br1_frame = Frame(Lg_frame, bg='#edfcfc', width=100, height=150)
br1_frame.place(x=0, y=220)
lc1_frame = Frame(Lg_frame, bg='#f5fefc', width=180, height=150)
lc1_frame.place(x=100, y=220)
sp1_frame = Frame(Lg_frame, bg='#faf3eb', width=180, height=150)
sp1_frame.place(x=280, y=220)

sn1_frame = Frame(Lg_frame, bg='#f1ead3', width=180, height=150)
sn1_frame.place(x=460, y=220)

se1_frame = Frame(Lg_frame, bg='#fffada', width=180, height=150)
se1_frame.place(x=640, y=220)

sa1_frame = Frame(Lg_frame, bg='#faf5df', width=180, height=150)
sa1_frame.place(x=820, y=220)

st1_frame = Frame(Lg_frame, bg='#fbfcf7', width=180, height=150)
st1_frame.place(x=1000, y=220)

sy1_frame = Frame(Lg_frame, bg='#faf5df', width=180, height=150)
sy1_frame.place(x=1180, y=220)


br2_frame = Frame(Lg_frame, bg='#fbfcf7', width=100, height=150)
br2_frame.place(x=0, y=380)
lc2_frame = Frame(Lg_frame, bg='#f8efec', width=180, height=150)
lc2_frame.place(x=100, y=380)
sp2_frame = Frame(Lg_frame, bg='#faf3eb', width=180, height=150)
sp2_frame.place(x=280, y=380)

sn2_frame = Frame(Lg_frame, bg='#e7decc', width=180, height=150)
sn2_frame.place(x=460, y=380)

se2_frame = Frame(Lg_frame, bg='#faf3eb', width=180, height=150)
se2_frame.place(x=640, y=380)

sa2_frame = Frame(Lg_frame, bg='#fbfcf7', width=180, height=150)
sa2_frame.place(x=820, y=380)

st2_frame = Frame(Lg_frame, bg='#f8efec', width=180, height=150)
st2_frame.place(x=1000, y=380)

sy2_frame = Frame(Lg_frame, bg='#faf3eb', width=180, height=150)
sy2_frame.place(x=1180, y=380)


img = Image.open(r'C:\Users\ASA\Downloads\OIF.jpeg')
img = img.resize((100, 120))
bg_img = ImageTk.PhotoImage(img)

bg_label = Label(br_frame, image=bg_img)
bg_label.place(x=5, y=5)

img1 = Image.open(r'C:\Users\ASA\Downloads\OIP (1).jpeg')
img1 = img1.resize((100, 120))
bg_img1 = ImageTk.PhotoImage(img1)

bg1_label = Label(br1_frame, image=bg_img1)
bg1_label.place(x=5, y=5)

imga = Image.open(r'C:\Users\ASA\Downloads\R.jpeg')
imga = imga.resize((100, 120))
bg_imga = ImageTk.PhotoImage(imga)

bga_label = Label(br2_frame, image=bg_imga)
bga_label.place(x=5, y=5)


br3_frame = Frame(Lg_frame, bg='#fbfcf7', width=100, height=50)
br3_frame.place(x=0, y=0)
lc3_frame = Frame(Lg_frame, bg='#faf3eb', width=180, height=50)
lc3_frame.place(x=100, y=0)
sp3_frame = Frame(Lg_frame, bg='#fbfcf7', width=180, height=50)
sp3_frame.place(x=280, y=0)

sn3_frame = Frame(Lg_frame, bg='#faf3eb', width=180, height=50)
sn3_frame.place(x=460, y=0)

se3_frame = Frame(Lg_frame, bg='#faf3eb', width=180, height=50)
se3_frame.place(x=640, y=0)

sa3_frame = Frame(Lg_frame, bg='#fbfcf7', width=180, height=50)
sa3_frame.place(x=820, y=0)

st3_frame = Frame(Lg_frame, bg='#fbfcf7', width=180, height=50)
st3_frame.place(x=1000, y=0)

sy3_frame = Frame(Lg_frame, bg='#fbfcf7', width=180, height=50)
sy3_frame.place(x=1180, y=0)

Day = Label(br3_frame, text='TIMING', font=('Georgia', 15, 'bold'))
Day.place(x=5, y=5)

Day1 = Label(br_frame, text='BREAKFAST', font=('Georgia', 10, 'bold'))
Day1.place(x=5, y=15)

Day2 = Label(br1_frame, text='LUNCH', font=('Georgia', 10, 'bold'))
Day2.place(x=10, y=15)

Day3 = Label(br2_frame, text='SUPPER', font=('Georgia', 10, 'bold'))
Day3.place(x=10, y=15)




Mon = Label(lc3_frame, text='Monday', font=('Georgia', 15, 'bold'))
Mon.place(x=35, y=5)

Tue = Label(sp3_frame, text='Tuesday', font=('Georgia', 15, 'bold'))
Tue.place(x=35, y=5)

Wed = Label(sn3_frame, text='Wednesday', font=('Georgia', 15, 'bold'))
Wed.place(x=35, y=5)

Thu = Label(se3_frame, text='Thursday', font=('Georgia', 15, 'bold'))
Thu.place(x=35, y=5)

fr = Label(sa3_frame, text='Friday', font=('Georgia', 15, 'bold'))
fr.place(x=35, y=5)

sat = Label(st3_frame, text='Saturday', font=('Georgia', 15, 'bold'))
sat.place(x=35, y=5)

su = Label(sy3_frame, text='Sunday', font=('Georgia', 15, 'bold'))
su.place(x=35, y=5)

# Creating the buttons
variable = StringVar(lc_frame)
variable.set('Menu')

option_menu = OptionMenu(lc_frame, variable,
                         'Wheat', 'Oat', 'Koko')
option_menu.place(x=50, y=5)

variable1 = StringVar(sp_frame)
variable1.set('Menu')

option_menu1 = OptionMenu(sp_frame, variable1,
                         'Wheat', 'Oat', 'Koko')
option_menu1.place(x=50, y=5)

variable2 = StringVar(sn_frame)
variable2.set('Menu')

option_menu2 = OptionMenu(sn_frame, variable2,
                         'Wheat', 'Oat', 'Koko')
option_menu2.place(x=50, y=5)


variable3 = StringVar(se_frame)
variable3.set('Menu')

option_menu3 = OptionMenu(se_frame, variable3,
                         'Wheat', 'Oat', 'Koko')
option_menu3.place(x=50, y=5)


variable4 = StringVar(sa_frame)
variable4.set('Menu')

option_menu4 = OptionMenu(sa_frame, variable4,
                         'Wheat', 'Oat', 'Koko')
option_menu4.place(x=50, y=5)


variable5 = StringVar(st_frame)
variable5.set('Menu')

option_menu5 = OptionMenu(st_frame, variable5,
                         'Wheat', 'Oat', 'Koko')
option_menu5.place(x=50, y=5)


variable6 = StringVar(sy_frame)
variable6.set('Menu')

option_menu6 = OptionMenu(sy_frame, variable6,
                         'Wheat', 'Oat', 'Koko')
option_menu6.place(x=50, y=5)

Lunch = StringVar(lc1_frame)
Lunch.set('Menu')

option_menu7 = OptionMenu(lc1_frame, Lunch,
                         'Tz', 'Fufu', 'Rice')
option_menu7.place(x=50, y=5)


Lunch1 = StringVar(sp1_frame)
Lunch1.set('Menu')

option_menu9 = OptionMenu(sp1_frame, Lunch1,
                         'Tz', 'Banku', 'Konkonte')
option_menu9.place(x=50, y=5)


Lunch3 = StringVar(sn1_frame)
Lunch3.set('Menu')

option_menu11 = OptionMenu(sn1_frame, Lunch3,
                         'Tz', 'Banku', 'Konkonte')
option_menu11.place(x=50, y=5)

Lunch4 = StringVar(se1_frame)
Lunch4.set('Menu')

option_menu12 = OptionMenu(se1_frame, Lunch4,
                         'Tz', 'Banku', 'Konkonte')
option_menu12.place(x=60, y=5)

Lunch5 = StringVar(sa1_frame)
Lunch5.set('Menu')

option_menu13 = OptionMenu(sa1_frame, Lunch5,
                         'Tz', 'Banku', 'Konkonte')
option_menu13.place(x=60, y=5)

Lunch6 = StringVar(st1_frame)
Lunch6.set('Menu')

option_menu14 = OptionMenu(st1_frame, Lunch6,
                         'Tz', 'Banku', 'Konkonte')
option_menu14.place(x=60, y=5)

Lunch7 = StringVar(sy1_frame)
Lunch7.set('Menu')

option_menu15 = OptionMenu(sy1_frame, Lunch7,
                         'Tz', 'Banku', 'Konkonte')
option_menu15.place(x=60, y=5)


supper = StringVar(lc2_frame)
supper.set('Menu')

option_menu16 = OptionMenu(lc2_frame, supper,
                         'Noodles', 'Yam', 'Hot chocolate')
option_menu16.place(x=60, y=5)

supper1 = StringVar(sp2_frame)
supper1.set('Menu')

option_menu17 = OptionMenu(sp2_frame, supper1,
                         'Noodles', 'Yam', 'Hot chocolate')
option_menu17.place(x=60, y=5)

supper2 = StringVar(sn2_frame)
supper2.set('Menu')

option_menu18 = OptionMenu(sn2_frame, supper2,
                         'Noodles', 'Yam', 'Hot chocolate')
option_menu18.place(x=60, y=5)

supper3 = StringVar(se2_frame)
supper3.set('Menu')

option_menu19 = OptionMenu(se2_frame, supper3,
                         'Noodles', 'Yam', 'Hot chocolate')
option_menu19.place(x=60, y=5)

supper4 = StringVar(sa2_frame)
supper4.set('Menu')

option_menu20 = OptionMenu(sa2_frame, supper4,
                         'Noodles', 'Yam', 'Hot chocolate')
option_menu20.place(x=60, y=5)

supper5 = StringVar(st2_frame)
supper5.set('Menu')

option_menu21 = OptionMenu(st2_frame, supper5,
                         'Noodles', 'Yam', 'Hot chocolate')
option_menu21.place(x=60, y=5)

supper6 = StringVar(sy2_frame)
supper6.set('Menu')

option_menu22 = OptionMenu(sy2_frame, supper6,
                         'Noodles', 'Yam', 'Hot chocolate')
option_menu22.place(x=60, y=5)


img2 = Image.open(r'C:\Users\ASA\Downloads\Br.jpg')
img2 = img2.resize((120, 100))
bg_img2 = ImageTk.PhotoImage(img2)

bg2_label = Label(lc_frame, image=bg_img2)
bg2_label.place(x=40, y=30)

img3 = Image.open(r'C:\Users\ASA\Downloads\Br3.jpg')
img3 = img3.resize((120, 100))
bg_img3 = ImageTk.PhotoImage(img3)

bg3_label = Label(sp_frame, image=bg_img3)
bg3_label.place(x=40, y=30)


img4 = Image.open(r'C:\Users\ASA\Downloads\Br2.jpg')
img4 = img4.resize((120, 100))
bg_img4 = ImageTk.PhotoImage(img4)

bg4_label = Label(sn_frame, image=bg_img4)
bg4_label.place(x=40, y=30)

img5 = Image.open(r'C:\Users\ASA\Downloads\Br3.jpg')
img5 = img5.resize((120, 100))
bg_img5 = ImageTk.PhotoImage(img5)

bg5_label = Label(se_frame, image=bg_img5)
bg5_label.place(x=40, y=30)

img6 = Image.open(r'C:\Users\ASA\Downloads\Br4.jpg')
img6 = img6.resize((120, 100))
bg_img6 = ImageTk.PhotoImage(img6)

bg6_label = Label(sa_frame, image=bg_img6)
bg6_label.place(x=40, y=30)


img7 = Image.open(r'C:\Users\ASA\Downloads\Br5.jpg')
img7 = img7.resize((120, 100))
bg_img7 = ImageTk.PhotoImage(img7)

bg7_label = Label(st_frame, image=bg_img7)
bg7_label.place(x=40, y=30)


img8 = Image.open(r'C:\Users\ASA\Downloads\Br4.jpg')
img8 = img8.resize((120, 100))
bg_img8 = ImageTk.PhotoImage(img8)

bg8_label = Label(sy_frame, image=bg_img8)
bg8_label.place(x=40, y=30)


img9 = Image.open(r'C:\Users\ASA\Downloads\L1.jpg')
img9 = img9.resize((120, 100))
bg_img9 = ImageTk.PhotoImage(img9)

bg9_label = Label(lc1_frame, image=bg_img9)
bg9_label.place(x=40, y=30)


img10 = Image.open(r'C:\Users\ASA\Downloads\L2.jpeg')
img10 = img10.resize((120, 100))
bg_img10 = ImageTk.PhotoImage(img10)

bg10_label = Label(sp1_frame, image=bg_img10)
bg10_label.place(x=40, y=30)


img11 = Image.open(r'C:\Users\ASA\Downloads\L3.jpeg')
img11 = img11.resize((120, 100))
bg_img11 = ImageTk.PhotoImage(img11)

bg11_label = Label(sn1_frame, image=bg_img11)
bg11_label.place(x=40, y=30)


img12 = Image.open(r'C:\Users\ASA\Downloads\L4.jpeg')
img12 = img12.resize((120, 100))
bg_img12 = ImageTk.PhotoImage(img12)

bg12_label = Label(se1_frame, image=bg_img12)
bg12_label.place(x=40, y=30)


img13 = Image.open(r'C:\Users\ASA\Downloads\L5.jpg')
img13 = img13.resize((120, 100))
bg_img13 = ImageTk.PhotoImage(img13)

bg13_label = Label(sa1_frame, image=bg_img13)
bg13_label.place(x=40, y=30)


img14 = Image.open(r'C:\Users\ASA\Downloads\L6.jpg')
img14 = img14.resize((120, 100))
bg_img14 = ImageTk.PhotoImage(img14)

bg14_label = Label(st1_frame, image=bg_img14)
bg14_label.place(x=40, y=30)

img15 = Image.open(r'C:\Users\ASA\Downloads\L7.jpeg')
img15 = img15.resize((120, 100))
bg_img15 = ImageTk.PhotoImage(img15)

bg15_label = Label(sy1_frame, image=bg_img15)
bg15_label.place(x=40, y=30)

#  Images of supper

img16 = Image.open(r'C:\Users\ASA\Downloads\s1.jpg')
img16 = img16.resize((120, 100))
bg_img16 = ImageTk.PhotoImage(img16)

bg16_label = Label(lc2_frame, image=bg_img16)
bg16_label.place(x=40, y=30)


img17 = Image.open(r'C:\Users\ASA\Downloads\s2.jpeg')
img17 = img17.resize((120, 100))
bg_img17 = ImageTk.PhotoImage(img17)

bg17_label = Label(sp2_frame, image=bg_img17)
bg17_label.place(x=40, y=30)


img18 = Image.open(r'C:\Users\ASA\Downloads\s3.jpeg')
img18 = img18.resize((120, 100))
bg_img18 = ImageTk.PhotoImage(img18)

bg18_label = Label(sn2_frame, image=bg_img18)
bg18_label.place(x=40, y=30)

img19 = Image.open(r'C:\Users\ASA\Downloads\s4.jpeg')
img19 = img19.resize((120, 100))
bg_img19 = ImageTk.PhotoImage(img8)

bg19_label = Label(se2_frame, image=bg_img19)
bg19_label.place(x=40, y=30)


img20 = Image.open(r'C:\Users\ASA\Downloads\s5.jpg')
img20 = img20.resize((120, 100))
bg_img20 = ImageTk.PhotoImage(img20)

bg20_label = Label(sa2_frame, image=bg_img20)
bg20_label.place(x=40, y=30)


img21 = Image.open(r'C:\Users\ASA\Downloads\s6.jpg')
img21 = img21.resize((120, 100))
bg_img21 = ImageTk.PhotoImage(img21)

bg21_label = Label(st2_frame, image=bg_img21)
bg21_label.place(x=40, y=30)


img22 = Image.open(r'C:\Users\ASA\Downloads\s7.jpeg')
img22 = img22.resize((120, 100))
bg_img22 = ImageTk.PhotoImage(img22)

bg22_label = Label(sy2_frame, image=bg_img22)
bg22_label.place(x=40, y=30)


Btn = Button(root, text='Submit', font=('Arial', 20, 'bold'), bd=5, borderwidth=5, border=5, width=8, bg='#f8efec',
             command=submit)
Btn.place(x=1230, y=140)


root.mainloop()