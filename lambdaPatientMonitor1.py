# import the JSON utility package since we will be working with a JSON object
import json
import sys
import os
import logging
import pymysql

host="mm-xpand1.mdb0001358.db.skysql.net"
port="5002"
user="DB00006940"
password="Admin777!"
database="patientDB"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host='mm-xpand1.mdb0001358.db.skysql.net', port=5002, user='DB00006940',
                           passwd="Admin777!", db='patientDB', ssl={'ca':'/opt/python/skysql_chainXpand.pem'}, connect_timeout=10)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):
    
    # extract values from the event object we got from the Lambda service
    serialNumber = event['serialNumber']
    heartRate = event['heartRate']
    
    #serialNumber = '6745R522'
    #heartRate = '90'
    
    logger.info ("Serial Number is " + serialNumber)
    logger.info ("Heart Rate is " + heartRate)
    
    sqlString = "select serial_number, json_extract(info,'$.info.beatsPerMinute') as BPM from heartMonitors where serial_number like '%" + serialNumber + "%'" + " and json_extract(info,'$.info.beatsPerMinute') > " + heartRate + ";"
    with conn.cursor() as cur:
        cur.execute(sqlString)
        res1 = cur.fetchone()
    
# return a properly formatted JSON object
    return {
        
        'statusCode': 200,
        'body': json.dumps('The serial # is ' + str(res1[0]) + ' and the beats per minute are ' + str(res1[1]))
    }