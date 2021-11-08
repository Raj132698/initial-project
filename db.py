

import boto3
from boto3.dynamodb.conditions import Attr, Key
from botocore.exceptions import ClientError






   #start


PRIMARY_KEY     = "email_id"
NAME            = "name"
REMAINING_LEAVE = "remaining_leave"
REGION          = "region"
LEAVE_TYPE      = "leave_type"
LEAVE_DURATION  = "leave_duration"
DATES_APPLIED   = "dates_applied"
LEAVE_STATUS    = "leave_status"
STATUS          = "status"

DATA_ATTRIBUTE = "LEAVE-PORTAL"

DB=boto3.resource('dynamodb')
table= DB.Table(DATA_ATTRIBUTE)

def put_leave():
    # Mainly to put the value after selecting in dynamodb

    items = {
        PRIMARY_KEY     :    f"{email_id}",
        NAME            :    f"{name}",
        REMAINING_LEAVE :    f"{remaining_leave}",
        REGION          :    f"{region}",
        LEAVE_TYPE      :    f"{leave_type}",
        LEAVE_DURATION  :    f"{leave_duration}",
        DATES_APPLIED   :    f"{dates_applied}",
        LEAVE_STATUS    :    f"{leave_status}",
        STATUS          :    f"{status}"
    }

    kwargs = {"Item": items, "ConditionExpression": Attr(PRIMARY_KEY).not_exists()}
    table.put_item(**kwargs)
    print("Items has been inserted")


def get_leave_details():
    primary_key_val=f"{email_id}"
    try:
        response = table.get_item(Key={PRIMARY_KEY: primary_key_val})


def mymethod():
   print("HeHe")

def delete_marked_leave():


    primary_key_val = f"{email_id}"
    kwargs = {"Key": {PRIMARY_KEY: primary_key_val}}
    table.delete_item(**kwargs)
    print("Item deleted")
   
 def resolve():

    primary_key_val = f"{email_id}"
    kwargs = {"Key": {PRIMARY_KEY: primary_key_val}}
    table.delete_item(**kwargs)
    print("Item deleted")
    
def login:

     pass;

def logout:
    pass;
