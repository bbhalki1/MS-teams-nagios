#!/usr/bin/python

import optparse
import sys

parser = optparse.OptionParser("usage: ./msteams.py -w webhook -s servicedesc -c servicestate -h hostalias -o serviceoutput -n notificationtype")
parser.add_option("-w","--webhook",dest = "webhook",help="Specify the webhook url")
parser.add_option("-s","--servicedesc",default=None,dest = "servicedesc",help="Specify the servicedesc")
parser.add_option("-c","--servicestate",default=None,dest = "servicestate",help="Specify the servicestate")
parser.add_option("-a","--hostalias",default=None,dest = "hostalias",help="Specify the hostalias")
parser.add_option("-x","--hoststate",default=None,dest = "hoststate",help="Specify the hoststate")
parser.add_option("-y","--hostoutput",default=None,dest = "hostoutput",help="Specify the hostoutput")
parser.add_option("-o","--serviceoutput",default=None,dest = "serviceoutput",help="Specify the serviceoutput")
parser.add_option("-n","--notificationtype",default=None,dest = "notificationtype",help="Specify the notificationtype")

(options, args) = parser.parse_args()

servicedesc = options.servicedesc
servicestate = options.servicestate
hostalias = options.hostalias
hoststate = options.hoststate
hostoutput = options.hostoutput
serviceoutput = options.serviceoutput
notificationtype = options.notificationtype


def main():
    #print servicedesc,servicestate,hostalias,hoststate,hostoutput,serviceoutput,notificationtype


main()