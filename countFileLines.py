#!/usr/bin/python

"Author: xy"

import sys, os

#extens = ['.c', '.cpp', '.h', '.hpp', '.java', '.py']
extens = ['.c', '.cpp', '.h', '.hpp', '.java', '.aidl']

linesCount = 0
filesCount = 0

def funCount(dirName):
	global extens, linesCount, filesCount

	for root, dirs, fileNames in os.walk(dirName):
		for f in fileNames:
			fname = os.path.join(root, f)
			
			try:
				ext = f[f.rindex('.'):]
				if (extens.count(ext) > 0):
					#print 'Support'
					filesCount += 1
					# print fname
					I_count = len(open(fname).readlines())
					print '\n', fname, ": ", I_count
					linesCount += I_count
				else:
					pass
					#print ext, ': not support'
			except:
				#print 'Error occur!'
				pass

if len(sys.argv) > 1:
	for m_dir in sys.argv[1:]:
		print m_dir
		funCount(m_dir)
else:
	funCount('.')

print '\n######################################################'
print 'Files count: ', filesCount
print 'Lines count: ', linesCount

raw_input('Press Enter to continue')
