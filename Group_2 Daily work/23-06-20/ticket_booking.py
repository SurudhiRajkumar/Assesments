import pymysql

class TicketBooking:
    def __init__(self):
        db = pymysql.Connect(host='localhost', user="root", passwd="root", db="sql1")
        self.db=db
        self.cursor=db.cursor()

    def ticket_available(self):
        try:
            self.cursor.execute("select screen_name,seats from ticket") #fetching  the details of booked tickets from ticket table
            f=self.cursor.fetchall()
            available_tickets_l1=[]
            available_tickets_l2 = []
            l1=[]
            l2=[]
            for i in f:
                if i[0]=="Luxe-1": # separating the tickets based on the screen_name
                    l1.append(i[1])
                else:
                    l2.append(i[1])

            for i in range(1,101):
                if i not in l1:
                    available_tickets_l1.append(i) # creating the list of seats which are avaiable for booking
                if i not in l2:
                    available_tickets_l2.append(i)

            print("Available tickets Luxe-1 ",available_tickets_l1)
            print("Available tickets Luxe-2 ", available_tickets_l2)

        except Exception as e:
            print(e)
        finally:
            self.db.close()

if __name__=="__main__":
    ticket=TicketBooking()
    ticket.ticket_available()

