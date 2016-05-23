#!/usr/bin/python

from conkyutil.writer import ConkyWriter

"""
Simple script that display a ToDo list from a
text file called .local_tasks.
"""

if __name__ == '__main__':
    writer = ConkyWriter()
	with open('.local_tasks', 'r') as file:
		for task in file.readlines():
		    writer
				.offset(12)
				.write(task.rstrip('\n'))
				.newline()
