#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  create_charts.py
#  
#  Copyright 2017  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 


import MySQLdb
import time
from matplotlib import use
use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as md
from datetime import datetime

def main():
    today_chart()
    time.sleep(.5)
    week_chart()
    time.sleep(.5)
    month_chart()

def today_chart():

    #return data from mysql query
    db = MySQLdb.connect(host = "localhost", user="python", passwd ="password", db="temps")
    cursor = db.cursor()
    
    query = "SELECT datetime, temperature, pressure, humidity FROM weatherdata where now() <= DATE_ADD(datetime, interval 1 day)"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    del cursor
    del db
    
    dates = []
    temps = []
    press = []
    humdty = []
    
    for record in result:
        dates.append(record[0])
        temps.append(record[1])
        press.append(record[2])
        humdty.append(record[3])

    #create figure
    plt.figure(1)
    
    #create temp subfigure
    plt.subplot(311)
    #plot data as linechart
    plt.plot(dates,temps,'r-')
    plt.title("Temperature last 24 hours")
    plt.ylabel("Temperature C")

    #plt.ylim(0,int(max(temps))*1.1)
    plt.margins(y=0.1)
    plt.grid(True)
    #plt.xticks(rotation=25)
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.xaxis.set_visible(True)

    #create humidity subplot
    plt.subplot(312)
    plt.plot(dates,humdty,'g-')
    plt.title("Humidity last 24 hours")
    plt.ylabel("Humidity %RH")
    #plt.xlabel("Time")
    #plt.ylim(0,int(max(humdty))*1.1)
    plt.margins(y=0.1)
    plt.grid(True)
    #plt.xticks(rotation=25)
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.xaxis.set_visible(True)
    

    
    #create barometric pressure subplob
    plt.subplot(313)
    #plot data as linechart
    plt.plot(dates, press, 'b-')
    plt.title("Pressure last 24 hours")
    plt.ylabel("Pressure (hPa)")
    plt.xlabel("Time")
    #plt.ylim(0,int(max(press))*1.1)
    plt.margins(y=0.1)
    plt.ticklabel_format(axis='y',useOffset=False)
    plt.xticks(rotation=15, ha='right')
    plt.grid(True)
    ax=plt.gca()
    xfmt = md.DateFormatter('%d.%b %H:%M')
    ax.xaxis.set_major_formatter(xfmt)
    plt.tight_layout()
    #plt.gcf().autofmt_xdate()
    #plt.show()
    F = plt.gcf()
    DPI = F.get_dpi()
    F.savefig('/var/www/html/plot.png',dpi = (150))
    plt.close()

def week_chart():
        #return data from mysql query
    db = MySQLdb.connect(host = "localhost", user="python", passwd ="password", db="temps")
    cursor = db.cursor()
    
    query = "SELECT datetime, temperature, pressure, humidity FROM weatherdata where now() <= DATE_ADD(datetime, interval 7 day)"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    del cursor
    del db
    
    
    
    dates = []
    temps = []
    press = []
    humdty = []
    

    
    for record in result:
        dates.append(record[0])
        temps.append(record[1])
        press.append(record[2])
        humdty.append(record[3])
    
    dates_slicew = dates[::5]
    temps_slicew = temps[::5]
    press_slicew = press[::5]
    humdty_slicew = humdty[::5]
    
    #create figure
    plt.figure(1)
    
    #create temp subfigure
    plt.subplot(311)
    #plot data as linechart
    plt.plot(dates_slicew,temps_slicew,'r-')
    plt.title("Temperature last week")
    plt.ylabel("Temperature C")

    #plt.ylim(0,int(max(temps))*1.1)
    plt.margins(y=0.1)
    plt.grid(True)
    #plt.xticks(rotation=25)
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.xaxis.set_visible(True)

    #create humidity subplot
    plt.subplot(312)
    plt.plot(dates_slicew,humdty_slicew,'g-')
    plt.title("Humidity last week")
    plt.ylabel("Humidity %RH")
    #plt.xlabel("Time")
    #plt.ylim(0,int(max(humdty))*1.1)
    plt.margins(y=0.1)
    plt.grid(True)
    #plt.xticks(rotation=25)
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.xaxis.set_visible(True)
    

    
    #create barometric pressure subplob
    plt.subplot(313)
    #plot data as linechart
    plt.plot(dates_slicew, press_slicew, 'b-')
    plt.title("Pressure last week")
    plt.ylabel("Pressure (hPa)")
    plt.xlabel("Days")
    #plt.ylim(0,int(max(press))*1.1)
    plt.margins(y=0.1)
    plt.ticklabel_format(axis='y',useOffset=False)
    plt.xticks(rotation=15, ha='right')
    plt.grid(True)
    ax=plt.gca()
    xfmt = md.DateFormatter('%d.%b')
    ax.xaxis.set_major_formatter(xfmt)
    plt.tight_layout()
    #plt.gcf().autofmt_xdate()
    #plt.show()
    F = plt.gcf()
    DPI = F.get_dpi()
    F.savefig('/var/www/html/plotweek.png',dpi = (150))
    plt.close()
    
def month_chart():
        #return data from mysql query
    db = MySQLdb.connect(host = "localhost", user="python", passwd ="password", db="temps")
    cursor = db.cursor()
    
    query = "SELECT datetime, temperature, pressure, humidity FROM weatherdata where now() <= DATE_ADD(datetime, interval 1 month)"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    del cursor
    del db

    dates = []
    temps = []
    press = []
    humdty = []
    
    for record in result:
        dates.append(record[0])
        temps.append(record[1])
        press.append(record[2])
        humdty.append(record[3])

    dates_slicem = dates[::15]
    temps_slicem = temps[::15]
    press_slicem = press[::15]
    humdty_slicem = humdty[::15]

    #create figure
    plt.figure(1)
    
    #create temp subfigure
    plt.subplot(311)
    #plot data as linechart
    plt.plot(dates_slicem,temps_slicem,'r-')
    plt.title("Temperature last month")
    plt.ylabel("Temperature degC")

    #plt.ylim(0,int(max(temps))*1.1)
    plt.margins(y=0.1)
    plt.grid(True)
    #plt.xticks(rotation=25)
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.xaxis.set_visible(True)

    #create humidity subplot
    plt.subplot(312)
    plt.plot(dates_slicem,humdty_slicem,'g-')
    plt.title("Humidity last month")
    plt.ylabel("Humidity %RH")
    #plt.xlabel("Time")
    #plt.ylim(0,int(max(humdty))*1.1)
    plt.margins(y=0.1)
    plt.grid(True)
    #plt.xticks(rotation=25)
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.xaxis.set_visible(True)
    
    #create barometric pressure subplot
    plt.subplot(313)
    #plot data as linechart
    plt.plot(dates_slicem, press_slicem, 'b-')
    plt.title("Pressure last month")
    plt.ylabel("Pressure (hPa)")
    plt.xlabel("Days")
    #plt.ylim(0,int(max(press))*1.1)
    plt.margins(y=0.1)
    plt.ticklabel_format(axis='y',useOffset=False)
    plt.xticks(rotation=15, ha='right')
    plt.grid(True)
    ax=plt.gca()
    xfmt = md.DateFormatter('%d.%b')
    ax.xaxis.set_major_formatter(xfmt)
    plt.tight_layout()
    #plt.gcf().autofmt_xdate()
    #plt.show()
    F = plt.gcf()
    DPI = F.get_dpi()
    F.savefig('/var/www/html/plotmonth.png',dpi = (150))
    plt.close()

    
if __name__ == '__main__':
    main()

