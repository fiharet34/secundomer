from tkinter import *

root = Tk()

class Stopwatch(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.widgets()
        self.running = False
        self.timer = [0,0,0]
        self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2])
        self.update_time()

    def widgets(self):
        self.timeFrame = LabelFrame(root,
                                    text='Time Frame',
                                    width=1200)
        
        self.timeFrame.grid(row=0,
                            column=0,
                            sticky=W)

        self.resetButton = Button(self.timeFrame,
                                  text='Reset',
                                  command=self.resetTime)
        
        self.resetButton.grid(row=2,
                              column=1)

        self.pauseButton = Button(self.timeFrame,
                                  text='Pause',
                                  command=self.pause)
        
        self.pauseButton.grid(row=1,
                              column=1)

        self.startButton = Button(self.timeFrame,
                                  text='Start',
                                  command=self.start)
        
        self.startButton.grid(row=0,
                              column=1)

        self.show = Label(self.timeFrame,
                          text='00:00:00',
                          font=30)
        
        self.show.grid(row=0,
                       column=0)

    def update_time(self):

        if self.running == True:      

            self.timer[2] += 1

            if (self.timer[2] >= 100):  
                self.timer[2] = 0
                self.timer[1] += 1      

            if (self.timer[1] >= 60):   
                self.timer[0] += 1
                self.timer[1] = 0

            self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2])
            self.show.config(text=self.timeString)
        root.after(10, self.update_time)


    def start(self):           
        self.running = True

    def pause(self):         
        self.running = False    

    def resetTime(self):   
        self.running = False
        self.timer = [0,0,0]
        self.show.config(text='00:00:00')



Stopwatch(root)

root.mainloop()