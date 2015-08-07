#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *
import sys

from icalendar import Calendar
from prettytable import PrettyTable
        
def main():
    if len(sys.argv) > 1:
        file_name = r'' + sys.argv[1]
        cal = Calendar.from_ical(open(file_name,'rb').read())        
        event = cal.walk('vevent')[0]
        SUMMARY = unicode(event['SUMMARY']).encode('utf-8')
        
        DTSTART = str(event['DTSTART'].dt)
        DTEND = str(event['DTEND'].dt)
        
        LOCATION = unicode(event['LOCATION']).encode('utf-8')
        ORGANIZER = unicode(event['ORGANIZER'].params['CN']).encode('utf-8')
        DESCRIPTION = unicode(event['DESCRIPTION']).encode('utf-8')

        oo = str()
        ooo = event['ATTENDEE']
        if isinstance(ooo, basestring):
            oo = ooo
        else:
            for o in ooo:
                name = o.params['CN']
                mail = unicode(o).encode('utf-8').split(':')[1]
                oo += '%s <%s>\n' % (name, mail)
                
        
        x = PrettyTable(["Key", "Value"])
        x.max_width['Value'] = 80
        x.header = False            
        x.align["Key"] = "l"
        x.padding_width = 1            
        x.add_row(['Организатор:', ORGANIZER])
        x.add_row(['Название:', SUMMARY])
        x.add_row(['Место:', LOCATION])
        x.add_row(['Начало:', DTSTART])
        x.add_row(['Окончание:', DTEND])
        x.add_row(['Описание:', DESCRIPTION])
        x.add_row(['Участники:', oo])
        print x
    else:
        print "Use mutt_cal.py <file.ics>"
if __name__ == '__main__':
    main()
