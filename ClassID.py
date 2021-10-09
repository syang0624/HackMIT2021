#This code returns Class ID for the students

import os
from pprint import pprint
os.system('pip install notion-database')
os.system('pip install requests')
from notion_database.database import Database
import requests
import json

def dictionary():

  notion_key = 'secret_JufIrkzsH7EJaHqd1BLL3TpaP7RfPIteoycWi9nsmON'
  D = Database(integrations_token=notion_key)
  databaseid = '81a17757cdbc4f84a83d399fa76d7230'
  D.find_all_page(database_id=databaseid)
  pprint(D.result['results'])
  
  lst = []
  for res in D.result['results']:
    _dict = {
    "class_topics": [],
    "class_foundational_topics": []
  }
    _dict["class_id"] = res['properties']['class_id']['title'][0]['text']['content']
    _dict["Class Name"] = res['properties']["Class Name"]['rich_text'][0]['text']['content']
    for topic in res['properties']['class_topics']['multi_select']:
      _dict['class_topics'].append(topic['name'])
    _dict['course_name'] = res['properties']['course_name']['select']['name']

    for ftopic in res['properties']['class_foundational_topics']['multi_select']:
      _dict['class_foundational_topics'].append(ftopic['name'])
      lst.append(_dict)
 
  return lst

pprint(dictionary())
