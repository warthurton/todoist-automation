#!/usr/bin/python

import todoist
import json

with open('config.json') as data_file:
	data=json.load(data_file)

todoistKey = data["TodoistAPIKey"];

api = todoist.TodoistAPI(todoistKey)


personalProject = api.projects.get_by_id(data["PersonalProject"])
personalProject.update(collapsed=0)

workProject = api.projects.get_by_id(data["WorkProject"])
workProject.update(collapsed=1)
api.commit()