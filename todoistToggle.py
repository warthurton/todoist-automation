#!/usr/bin/python
import sys
import todoist
import json

with open('config.json') as data_file:
	data=json.load(data_file)

todoistKey = data["TodoistAPIKey"];

api = todoist.TodoistAPI(todoistKey)

personalProject = api.projects.get_by_id(data["PersonalProject"])
workProject = api.projects.get_by_id(data["WorkProject"])

if sys.argv[1] == "w":
    personalProject.update(collapsed=1)
    workProject.update(collapsed=0)
elif sys.argv[1] == "p":
    personalProject.update(collapsed=0)
    workProject.update(collapsed=1)

api.commit()