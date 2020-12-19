import click
#import util
import awsutil
import json

chs=True
myip = "PrivateIpAddress"
#myip = "PublicIpAddress"

#print ("HELLO")


@click.group()
def cli():
   """ This script will work on instances """
   pass
@cli.command()
def status():
   """ prints and running instances """
   #print("STATUS")
   jsonData = awsutil.ec2status()
   jsonBlob = json.loads(jsonData)
   mynew = jsonBlob.get("Reservations")

   for myDict in mynew:
      print ('-'*60)
      ids = myDict["Instances"]
      for id in ids:
         tagName = awsutil.get_tag_name(id)
         iState = id["State"]
         iType = id["InstanceType"]
         #print (iState["Name"])
         print ("The INSTANCE %s is %s -- %s" % (tagName, iState["Name"], iType))
         iState = id["State"]
         #print (iState["Name"])
         realState = iState["Name"]
         if (realState == "running"):
            if myip in id.keys():
                print (id[myip])


   
@cli.command()
@click.option('--tag', default='bulkHelper', help="This is the name of the EC2 Instance (tag)", required=True)
def start(tag):
   """ starts an instance """
   jsonData = awsutil.ec2status()
   jsonBlob = json.loads(jsonData)
   mynew = jsonBlob.get("Reservations")

   for myDict in mynew:
      ids = myDict["Instances"]
      for id in ids:
         tagName = awsutil.get_tag_name(id)

         instanceId = id["InstanceId"]
         iState = id["State"]
         if (tagName == tag):
            print ("The INSTANCE %s is %s " % (tagName, iState["Name"]))
            print ("Starting instance ID %s " % instanceId)
            print("START YOUR Engines %s" % tag)
            awsutil.ec2start(id=instanceId)


@cli.command()
@click.option('--tag', default='bulkHelper', help="This is the name of the EC2 Instance (tag)", required=True)
def stop(tag):
   """ stops an instance """
   jsonData = awsutil.ec2status()
   jsonBlob = json.loads(jsonData)
   mynew = jsonBlob.get("Reservations")

   for myDict in mynew:
      ids = myDict["Instances"]
      for id in ids:
         #print (id["InstanceType"])
         #print (id["InstanceId"])
         instanceId = id["InstanceId"]
         tagName = awsutil.get_tag_name(id)

         instanceId = id["InstanceId"]
         iState = id["State"]
         if (tagName == tag):
            print ("Stopping instance ID %s " % instanceId)
            print ("The INSTANCE %s is %s " % (tagName, iState["Name"]))
            print ("KILL YOUR Engines %s" % tag)
            awsutil.ec2stop(id=instanceId)

@cli.command()
@click.option('--tag', default='bulkHelper', help="This is the name of the EC2 Instance (tag)", required=True)
def getip(tag):
   """ gets the public ip of an instance """
   jsonData = awsutil.ec2status()
   #print (json.dumps(jsonData, indent=2))
   jsonBlob = json.loads(jsonData)
   mynew = jsonBlob.get("Reservations")

   for myDict in mynew:
      ids = myDict["Instances"]
      for id in ids:
         #print (id["InstanceType"])
         #print (id["InstanceId"])
         iState = id["State"]
         #print (iState["Name"])
         #print ("The INSTANCE is %s " % iState["Name"])
         tagName = awsutil.get_tag_name(id)

         if (tagName == tag):
            realState = iState["Name"]
            if (realState == "running"):
               print (id[myip])
            else:
               print ("ERROR the instance MUST be running to get its IP Address")
