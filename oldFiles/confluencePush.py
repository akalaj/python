import commands
import sys
import os
import re
import pprint
import sys, string, xmlrpclib, logging, json, time, socket
import argparse
import subprocess
import getpass
#Variables
ADDRESS_LIST1=commands.getstatusoutput("mysql --login-path=dba_tool -hdb-dev-20 cfg-bs-dev -Bse \"SELECT DISTINCT(address) FROM storage\"")
ADDRESS_LIST=ADDRESS_LIST1[1].split()
CLEARED=[]
#cleanup
os.system("rm HTML FINAL 2>/dev/null")

#Primary function
FILE=open('HTML', 'a')
#FILE.write("\"\"\"")
for NAME in ADDRESS_LIST:
        TEMP_C=commands.getstatusoutput("mysql --login-path=dba_tool -hdb-dev-20 cfg-bs-dev -Bse \"SELECT name FROM storage WHERE workingdirectory='/etc/bacula/bs-sd-2' AND address='%s'\"" % NAME)
        CLIENTS=TEMP_C[1].split()
        if not CLIENTS:
                pass
        else:
                FILE.write("\n<table><tbody><tr><th class=\"highlight-green\" data-highlight-colour=\"green\">%s</th></tr>" % NAME)
                for CLIENT_NAME in CLIENTS:
                        P=CLIENT_NAME.split('-')
                        try:
                                CHECK=P[2]
                        except IndexError:
                                CHECK=0
                        if CHECK is 0:
                                FINAL_VALUE=P[0]+"-"+P[1]
                                if FINAL_VALUE in CLEARED:
                                        pass
                                else:
                                        CLEARED.append(FINAL_VALUE)
                                        FILE.write("\n<tr><td>%s</td></tr>" % FINAL_VALUE)
                        else:
                                FINAL_VALUE=P[0]+"-"+P[1]+"-"+P[2]
                                if FINAL_VALUE in CLEARED:
                                        pass
                                else:
                                        CLEARED.append(FINAL_VALUE)
                                        FILE.write("\n<tr><td>%s</td></tr>" % FINAL_VALUE)
                FILE.write("\n</tbody></table>")
FILE.close()
def publish():
        print "Getting login.conf information"
        settings='''
        Client settings:
        this requires a file in the same path named login.conf in json format that contains the following:
        {
        "spaceKey" : "Spacekey",
        "pageTitle" : "Page Title",
        "confUser" : "username",
        "confPass" : "secretkey",
        "shortname" : "Shortname"
        }'''
        try:
                data = open("login.conf")
                conf = json.load(data)
                data.close()
        except:
                print settings
                sys.exit()

        print "Creating Confluence login token"
        server = xmlrpclib.Server('https://confluence.atlas.llnw.com/rpc/xmlrpc')
        token = server.confluence2.login(conf["confUser"], conf["confPass"])

        print "Token: %s" % token
        try:
                page = server.confluence2.getPage(token, conf["spaceKey"], conf["pageTitle"])
        except:
                exit("Could not find page " + conf["spaceKey"] + ":" + conf["pageTitle"])

        print "Creating HTML"
        content = open("HTML", "r").read()
        print "Publishing to Confluence"
        page['content'] = content
        server.confluence2.storePage(token, page)

        print "Go check confluence."
publish()
