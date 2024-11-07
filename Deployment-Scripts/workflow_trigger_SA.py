
import os
import requests
import sys

TOKEN= str(sys.argv[1])
SolutionName= str(sys.argv[2])
SolutionType= str(sys.argv[3])
DeploymentType= str(sys.argv[4])
Workflow_Name= str(sys.argv[5])

print( "the toke value is")
def trigger_workflow(Workflow_Name,SolutionName,SolutionType,DeploymentType):

      headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {TOKEN}",
      }

      data = {
        "event_type": Workflow_Name,
        "client_payload": {
          'SolutionName': SolutionName,
          'SolutionType': SolutionType,
          'SolutionType': SolutionType
        }
      }

      responseValue=requests.post(f"https://api.github.com/repos/ShifaMittal050/ALMPowerAppsDemo/dispatches",json=data,headers=headers)
      print(responseValue.content)

      responsevalue=requests.post(f"https://api.github.com/repos/ShifaMittal050/ALMPowerAppsDemo/dispatches",json=data,headers=headers)
      print("The respoinse message is ",responsevalue.content)

trigger_workflow(Workflow_Name,SolutionName,SolutionType,SolutionType)
