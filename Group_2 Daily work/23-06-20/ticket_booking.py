import pymysql

'''
Booked tickets data:
+-------------+-------+
| screen_name | seats |
+-------------+-------+
| Luxe-1      |     5 |
| Luxe-1      |    20 |
| Luxe-1      |    77 |
| Luxe-1      |    97 |
| Luxe-1      |    99 |
| Luxe-2      |     5 |
+-------------+-------+

Available tickets Luxe-1  [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 
32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 100]

Available tickets Luxe-2  [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 
65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 
99, 100]

'''

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

