# Serial-data-reader
Serial data reader is basically a Python based software that reads the COM port and displays the data on a laptop screen. The data used in this project is the values of current, voltage and power coming from a micro-controller (AVR or simply arduino). The software reads the values with the help of serial module of Python and displays it using tkinker.

# How is the data coming to COM port?
In this project Arduino UNO is used to send data on the COM port so it is easier to understand that how the data is coming to COM port for those who have worked with arduino or AVR. 

Let's assume that our microcontroller board (arduino UNO) is connected on COM port 4 of our PC and take the following dummy arduino code:

    void setup() {
      Serial.begin(9600);
      }
    void loop() {
        Serial.print("Hamza Bin Khalid Data ---> Voltage: 128V Current: 128A Load: 128W");
        Serial.print("\n ");
        delay(3000);
        Serial.print("Hamza Bin Khalid Data ---> Voltage: 133V Current: 166A Load: 157W");
        Serial.print("\n ");
        delay(3000);
        Serial.print("Hamza Bin Khalid Data ---> Voltage: 112V Current: 123A Load: 188W");
        Serial.print("\n ");
        delay(3000);
    }

So, the output on the Serial monitor will be:

    Hamza Bin Khalid Data ---> Voltage: 128V Current: 128A Load: 128W
    Hamza Bin Khalid Data ---> Voltage: 133V Current: 166A Load: 157W
    Hamza Bin Khalid Data ---> Voltage: 112V Current: 123A Load: 188W (... continue)


# How is the software processing data?
The following line (Line 121) in our Python file allows you to type the port name on which the data is coming. As our arduino is connected to the port No. 4 so we will write 'COM4' in the input box:

Labelh=Label(root,text='Enter port Name. E.g: COM4',font=("Arial","14")).place(x=120,y=40)

The python program now starts reading COM4 and saves every line in a string with the help of following lines (Line 67,68):

    thing = self.ser.readline().decode('ascii')
            string = str(thing)

The program now does string parsing to separate the values of voltage, current and load with the help of follwing lines (Line 72-83):

        for i in range(37, len(string)):
            if string[i] == 'V':
                break
        v=string[36:i]
        for j in range(48, len(string)):
            if string[j] == 'A':
                break
        c= string[i + 11:j]
        for k in range(60, len(string)):
            if string[k] == 'W':
                break
        p=string[j + 8:k]
        
The values of voltage, current and load are stored in variables v,c an p respectively and are then displayed on the software screen.

# How to make changings for your custom data?
You need to make two changes for your custom data:

1. You need to change the arduino code which is sending data to COM port. 
*Note that your source of sending data to the COM port can be anything so make changes accordingly.

2. Make changes in the lines (72-83) of python program which are used for string parsing to seperate values from the string (in our case numeric values if voltage, current and power).
*If you are using other than three variables, you need to make changes in lines 34-61 and 84-91 too.
