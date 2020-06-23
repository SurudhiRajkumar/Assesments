import pymysql

''' input: Enter the year(2018/2019):2018
    output:
    (101, 11, 7.6333)
    (101, 12, 7.0968)
''' 

class AverageSwipeTime:
    def __init__(self):
        db = pymysql.Connect(host='localhost', user="root", passwd="root", db="sql1")
        self.db = db
        self.cursor = db.cursor()

    def avg_time_calc(self):
        try:
            year=int(input("Enter the year(2018/2019):"))
            sql="select id, month(swipe_date) as month, avg_time from (select id, swipe_date, round(avg(time_out-time_in) " \
                "over(partition by month(swipe_date) order by month(swipe_date)),4)avg_time from swipe " \
                "where year(swipe_date) = '{}')t group by month(swipe_date)".format(year)
            self.cursor.execute(sql)
            res=self.cursor.fetchall()
            for i in res:
                print(i)

        except ValueError as e:
            print("Enter only intergers",e)
        except Exception as e:
            print(e)
        finally:
            self.db.close()


if __name__=="__main__":
    obj=AverageSwipeTime()
    obj.avg_time_calc()
