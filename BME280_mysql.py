#!/usr/bin/env python

import bme280
import MySQLdb


    
def main():
    sql_write()
    
    
def sql_write():
    db = MySQLdb.connect(host = "localhost", user="python", passwd ="password", db="temps")
    
    curs = db.cursor()
    try:
        curs.execute("INSERT INTO weatherdata VALUES(NULL, NOW(), CURRENT_DATE(), NOW(), %s, %s, %s)",bme280.readBME280All())
        db.commit()
        print "Data committed"
        
    except:
        print "Error:the database is being rolled back"
        db.rollback()
         
    finally:
        db.close()
       
if __name__ == "__main__":
    main()
