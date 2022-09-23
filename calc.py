import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib, Pango

# Variables
input1 = []
input2 = []
calculation = []
modifier = False
div = False
multi = False

one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"
zero = "0"

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(300, 400)
        self.set_title("GTK Calc")


# Widgets
    
    # Header Bar
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)

    # Boxes
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box14 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box15 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box16 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
    # Button One

        self.button1 = Gtk.Button(label = 1)
        self.button1.connect('clicked', self.one)

        self.set_child(self.box1)
        self.box1.append(self.box2)
        self.box2.append(self.button1)

    # Button Two
        self.button2 = Gtk.Button(label = 2)
        self.button2.connect('clicked', self.two)

        self.set_child(self.box1)
        self.box1.append(self.box3)
        self.box2.append(self.button2)

    # Button Three
        self.button3 = Gtk.Button(label = 3)
        self.button3.connect('clicked', self.three)

        self.set_child(self.box1)
        self.box1.append(self.box5)
        self.box2.append(self.button3)

    # Button Four

        self.button4 = Gtk.Button(label = 4)
        self.button4.connect('clicked', self.four)

        self.set_child(self.box1)
        self.box1.append(self.box6)
        self.box2.append(self.button4)

    # Button Five

        self.button5 = Gtk.Button(label = 5)
        self.button5.connect('clicked', self.five)

        self.set_child(self.box1)
        self.box1.append(self.box7)
        self.box2.append(self.button5)

    # Button Six

        self.button6 = Gtk.Button(label = 6)
        self.button6.connect('clicked', self.six)

        self.set_child(self.box1)
        self.box1.append(self.box8)
        self.box2.append(self.button6)

    # Button Seven

        self.button7 = Gtk.Button(label = 7)
        self.button7.connect('clicked', self.seven)

        self.set_child(self.box1)
        self.box1.append(self.box9)
        self.box2.append(self.button7)

    # Button Eight

        self.button8 = Gtk.Button(label = 8)
        self.button8.connect('clicked', self.eight)

        self.set_child(self.box1)
        self.box1.append(self.box10)
        self.box2.append(self.button8)

    # Button Nine

        self.button9 = Gtk.Button(label = 9)
        self.button9.connect('clicked', self.nine)

        self.set_child(self.box1)
        self.box1.append(self.box11)
        self.box2.append(self.button9)

    # Button Zero

        self.button0 = Gtk.Button(label = 0)
        self.button0.connect('clicked', self.zero)

        self.set_child(self.box1)
        self.box1.append(self.box12)
        self.box2.append(self.button0)

    # Button *
        self.buttonmulti = Gtk.Button(label = "*")
        self.buttonmulti.connect('clicked', self.multi)

        self.set_child(self.box1)
        self.box1.append(self.box13)
        self.box2.append(self.buttonmulti)

    # Button /
        self.buttondivide = Gtk.Button(label = "/")
        self.buttondivide.connect('clicked', self.divide)

        self.set_child(self.box1)
        self.box1.append(self.box14)
        self.box2.append(self.buttondivide)

    # Button -
        self.buttonsub = Gtk.Button(label = "-")
        self.buttonsub.connect('clicked', self.sub)
        
        self.set_child(self.box1)
        self.box1.append(self.box15)
        self.box2.append(self.buttonsub)

    # Button +
        self.buttonplus = Gtk.Button(label = "+")
        self.buttonplus.connect('clicked', self.plus)
        
        self.set_child(self.box1)
        self.box1.append(self.box16)
        self.box2.append(self.buttonplus)

    # Button =
        self.buttone = Gtk.Button(label = "=")
        self.buttone.connect('clicked', self.equals)

        self.set_child(self.box1)
        self.box1.append(self.box4)
        self.box2.append(self.buttone)


# Widget Functions

    def one(self, button):
        global input1, input2, modifier
        if modifier == False:
            input1.append(one)
        elif modifier == True:
            input2.append(one)
            input2 = ''.join(input2)

    def two(self, button):
        global input1, input2, modifier
        if modifier == False:
            input1.append(two)
        elif modifier == True:
            input2.append(two)
            input2 = ''.join(input2)

    def three(self, button):
        global input1, input2, modifier
        if modifier == False:
            input1.append(three)
        elif modifier == True:
            input2.append(three)
            input2 = ''.join(input2)

    def four(self, button):
        global input1, input2, modifier
        if modifier == False:
            input1.append(four)
        elif modifier == True:
            input2.append(four)
            input2 = ''.join(input2)

    def five(self, button):
        global input1, input2, modifier
        if modifier == False:
            input1.append(five)
        elif modifier == True:
            input2.append(five)
            input2 = ''.join(input2)

    def six(self, button):
        global input1, input2, modifier
        if modifier == False:
            input1.append(six)
        elif modifier == True:
            input2.append(six)
            input2 = ''.join(input2)

    def seven(self, button):
        global input1, input2, modifier
        if modifier == False:
            input1.append(seven)
        elif modifier == True:
            input2.append(seven)
            input2 = ''.join(input2)

    def eight(self, button):
        global input1, input2, modifier
        if modifier == False:
            input1.append(eight)
        elif modifier == True:
            input2.append(eight)
            input2 = ''.join(input2)

    def nine(self, button):
        global input1, input2, modifier
        if modifier == False:
            input1.append(nine)
        elif modifier == True:
            input2.append(nine)
            input2 = ''.join(input2)

    def zero(self, button):
        global input1, input2, modifier
        if modifier == False:
            input1.append(zero)
        elif modifier == True:
            input2.append(zero)
            input2 = ''.join(input2)
    
    def equals(self, button):
        global calculation, input1, input2, div, modifier, multi, sub, plus
        if input2 == "0":
            print("Error")
            input1 = []
            input2 = []
            modifier = False
        elif div == True:
            input2 = ''.join(input2)
            input2 = int(input2)
            calculation = input1 / input2
            print(calculation)
            input1 = []
            input2 = []
            modifier = False
            div = False
        elif multi == True:
            input2 = ''.join(input2)
            input2 = int(input2)
            calculation = input1 * input2
            print(calculation)
            input1 = []
            input2 = []
            modifier = False
            multi = False
        elif sub == True:
            input2 = ''.join(input2)
            input2 = int(input2)
            calculation = input1 - input2
            print(calculation)
            input1 = []
            input2 = []
            modifier = False
            sub = False
        elif plus == True:
            input2 = ''.join(input2)
            input2 = int(input2)
            calculation = input1 + input2
            print(calculation)
            input1 = []
            input2 = []
            modifier = False
            plus = False
        else:
            print("CRITICAL ERROR")

    def divide(self, button):
        global calculation, input1, input2, modifier, div, multi
        modifier = True
        div = True
        input1 = ''.join(input1)
        input1 = int(input1)
    
    def multi(self, button):
        global calcuation, input1, input2, modifier, multi
        modifier = True
        multi = True
        input1 = ''.join(input1)
        input1 = int(input1)
    
    def sub(self, button):
        global calcuation, input1, input2, modifier, sub
        modifier = True
        sub = True
        input1 = ''.join(input1)
        input1 = int(input1)
    
    def plus(self, button):
        global calculation, input1, input2, modifier, plus
        modifier = True
        plus = True
        input1 = ''.join(input1)
        input1 = int(input1)



class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.soup.gtkcalc")
app.run(sys.argv)