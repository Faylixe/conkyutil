#!/usr/bin/python

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from conkyutil.writer import ConkyWriter

"""
This scripts display a list of open issues from
a Jira distant installation.
"""

# URL
JIRA_URL = "%s://%s/rest/api/2/search?jql=assignee=%s+and+status='%s'+order+by+updatedDate+desc&fields=%s"

def getJiraURL(host, user, protocol='https', status='Open', fields='key,summary'):
	""" Builds and returns a valid JIRA API url. """
	return JIRA_URL % (protocol, host, user, status, fields)

def getJiraTasks(host, user):
	""" Extracts task from Jira for the given user. """
	url = getJiraURL(host, user)
	response = requests.get(url, verify=False)
	json = response.json()
	issues = {}
	for issue in json['issues']:
		issues[issue['key']] = issue['fields']['summary']
	return issues

if __name__ == '__main__':
    # For ssl issues.
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    # Intializes writer.
    writer = ConkyWriter()
    # Retrieves tasks.
    user = 'your_username'
    host = 'you_jira_hostname'
    tasks = getJiraTasks(host, user)
    if len(tasks) > 0:
        keys = tasks.keys()
        keys.sort(key=len, reverse=True)
        longest = len(keys[0])
        for key in keys:
            padding = longest - len(key)
    		writer
                .offset(12)
                .color('ffa300')
                .font('ubuntu:bold:pixelsize=12')
                .write('[%s]%s' % (key, ' ' * padding))
                .color('white')
                .font('ubuntu:pixelsize=12')
                .offset(10)
                .write(tasks[key])
    			.newline()
