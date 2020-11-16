#!/usr/bin/env python3

#VMWare Horizon Prometheus Exporter

#GS - Creation : Nov 16 2020

#USAGE : vmhopromexp.py --horizon_endpoint="https://horizon_endpoint.fqdn/" --horizon_user="user@vspehere_domain" --horizon_password="*********"

import sys
import getopt

def main(argv):

    horizon_endpoint=""
    horizon_user=""
    horizon_password=""

    try:
            opts, args = getopt.getopt(argv,"e:u:p:",["horizon_endpoint=","horizon_user=","horizon_password="])
    except getopt.GetoptError:
            print 'Usage : vmhopromexp.py --horizon_endpoint="https://horizon_endpoint.fqdn/" --horizon_user="user@vspehere_domain" --horizon_password="*********"'
            sys.exit(2)
    for opt, arg in opts:
        if opt in ("-e","--horizon_endpoint"):
            horizon_endpoint=arg
        elif opt in ("-u","--horizon_user"):
            horizon_user=arg
        elif opt in ("-p","--horizon_password"):
            horizon_password=arg

    connect_horizon_endpoint(horizon_endpoint,horizon_user,horizon_password)

main(sys.argv[1:])

def connect_horizon_endpoint(horizon_endpoint,horizon_user,horizon_password):
    print("Connexion au serveur : "+horizon_endpoint+" "+horizon_user+"/"+horizon_password)

    
