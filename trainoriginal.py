class train:
    def __init__(self,name,price,seat):
        self.name=name
        self.price=price
        self.seat=seat
        self.b=seat
        print(f"Name of the train is { self.name}")

    def status(self):
        print(f"Price of the one seat is { self.price}")
        print(f"Total seats in the train is { self.seat}")
    
    def book(self):
        
        if(self.seat>0):
            print(f"Your seat is booked !!!! /n Your seat no. is {self.seat}")
            self.seat=self.seat-1
            # for b in range(1,301):
                
                # print(b)
        else:
            print("SORRY !!! seats are fulll ")
    def cancel(self):
        
        if self.b==self.seat:
            print("you haved not book any seat")

        else:
            print("Your seat is cancel!!")
            self.seat=self.seat+1


p=train("Janta Express : 14407",50,300)
