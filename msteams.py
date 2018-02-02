#!/usr/bin/python

import optparse
import requests

parser = optparse.OptionParser("usage: ./msteams.py -w webhook -s servicedesc -c servicestate -a hostalias -o serviceoutput -n notificationtype")
parser.add_option("-w","--webhook",dest = "webhook",help="Specify the webhook url")
parser.add_option("-s","--servicedesc",default=None,dest = "servicedesc",help="Specify the servicedesc")
parser.add_option("-c","--servicestate",default=None,dest = "servicestate",help="Specify the servicestate")
parser.add_option("-a","--hostalias",default=None,dest = "hostalias",help="Specify the hostalias")
parser.add_option("-x","--hoststate",default=None,dest = "hoststate",help="Specify the hoststate")
parser.add_option("-y","--hostoutput",default=None,dest = "hostoutput",help="Specify the hostoutput")
parser.add_option("-o","--serviceoutput",default=None,dest = "serviceoutput",help="Specify the serviceoutput")
parser.add_option("-n","--notificationtype",default=None,dest = "notificationtype",help="Specify the notificationtype")

(options, args) = parser.parse_args()

webhook = options.webhook
servicedesc = options.servicedesc
servicestate = options.servicestate
hostalias = options.hostalias
hoststate = options.hoststate
hostoutput = options.hostoutput
serviceoutput = options.serviceoutput
notificationtype = options.notificationtype


def main():
    if hoststate is None:
        print hostalias
        print servicedesc
        print servicestate
        sendServiceStateAlerts(webhook,hostalias,servicedesc,servicestate,serviceoutput,notificationtype)
    else:
        print hostalias
        print 'in else'
        sendHostStateAlerts(webhook,hostalias,hoststate,hostoutput,notificationtype)

def sendServiceStateAlerts(webhook,hostalias,servicedesc,servicestate,serviceoutput,notificationtype):
    stateColor = "#dddddd"
    exitState=3
    if (servicestate=="WARNING"):
        stateColor = "#ffff66"
        exitState=1
    elif (servicestate == "CRITICAL"):
        stateColor="#f40000"
        exitState=2
    elif(servicestate=="OK"):
        stateColor="#00b71a"
        exitState=0
    else:
        stateColor="#cc00de"
        exitState=exitState
    buildJson(webhook,servicedesc,hostalias,servicestate,exitState,stateColor)


def sendHostStateAlerts(webhook,hostalias,hoststate,hostoutput,notificationtype):
    stateColor = "#dddddd"
    exitState=3
    if (hoststate=="WARNING"):
        stateColor = "#ffff66"
        exitState=1
    elif (hoststate == "CRITICAL"):
        stateColor="#f40000"
        exitState=2
    elif(hoststate=="OK"):
        stateColor="#00b71a"
        exitState=0
    else:
        stateColor="#cc00de"
        exitState=exitState
        
    if ('dev' in hostalias):
        nagiosServer = "printingpress.phx.gapinc.dev"
    else:
        nagiosServer = "printingpress.phx.gapinc.com"
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": hostalias + ' is ' + hoststate,
        "themeColor": stateColor,
        "sections": [
            {
                "title": hostalias + ' is ' + hoststate,
                "facts": [
                    {
                        "name":"Reason",
                        "value":hostoutput
                    },
                    { 
                        "name": "Printing Press URL", 
                        "value": "[Thruk](http://%s/thruk/#cgi-bin/extinfo.cgi?type=%s&host=%s)"%(nagiosServer,exitState,hostalias)
                    }
                ]
            }
        ]
    }
    print payload["sections"][0]["facts"]
    #postToAlerts(webhook,payload)

def buildJson(webhook,servicedesc,hostalias,servicestate,exitState,stateColor):
    if ('dev' in hostalias):
        nagiosServer = "printingpress.phx.gapinc.dev"
    else:
        nagiosServer = "printingpress.phx.gapinc.com"
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": servicedesc + ' on ' + hostalias + ' is ' + servicestate,
        "themeColor": stateColor,
        "sections": [
            {
                "title": servicedesc + ' on ' + hostalias + ' is ' + servicestate,
                "facts": [
                    {
                        "name":"Reason",
                        "value":serviceoutput
                    },
                    { 
                        "name": "Printing Press URL", 
                        "value": "[Thruk](http://%s/thruk/#cgi-bin/extinfo.cgi?type=%s&host=%s&service=%s)"%(nagiosServer,exitState,hostalias,servicedesc)
                    }
                ]
            }
        ]
    }
    postToAlerts(webhook,payload)
    

def postToAlerts(webhook,payload):
    r = requests.post(webhook,json=payload)
    print r.status_code

main()