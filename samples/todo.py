#!/usr/bin/python

from conkyutil.writer import ConkyWriter

def getLocalTasks(prefix, file):
	""" Extracts task from the given local task file. """
	issues = {}
	if exists(file):
		with open(file, 'r') as file:
			tasks = file.readlines()
			i = 0
			for task in tasks:
				key = '%s-%d' % (prefix, i)
				i += 1
				issues[key] = task.rstrip('\n')
	return issues

if __name__ == '__main__':
    writer = ConkyWriter()
    writer
		.offset(12)
		.
