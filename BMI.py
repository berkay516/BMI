from tkinter import Tk,mainloop,Label,Text,Button
class deneme:
    def __init__(self):
       self.t=Tk()
       self.t.minsize(width=400,height=400)
       self.t.title("BMI Calculator")
       
       self.l1=Label(self.t,text="Enter your weight")
       self.l1.pack()
       self.t1=Text(self.t,height=5,width=10)
       self.t1.pack()


       
       self.l2=Label(self.t,text="Enter your height")
       self.l2.pack()
       self.t2=Text(self.t,height=5,width=10)
       self.t2.pack()


       Button(self.t,text="Calculate",command=self.calculate,activebackground="red").pack()

       self.sum=Label(self.t,text="")
       self.sum.pack()


    def calculate(self):
       
       if self.t1.get("1.0","end")=="\n" or self.t2.get("1.0","end")=="\n":
            print("One of values is empty")
       else:
           
        try:
          if not self.t1.get("1.0","end").strip().isdigit() or not self.t2.get("1.0","end").strip().isdigit():
            raise ValueError("type error")

          else:
            self.sum.config(text=f'{int(self.t1.get("1.0","end"))+int(self.t2.get("1.0","end"))}')
        except ValueError as h:
           print(h)
       


    



d=deneme()
mainloop()




