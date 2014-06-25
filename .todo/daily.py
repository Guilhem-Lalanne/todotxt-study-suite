import datetime
import sys
import os

accepted = ['wake', 'eat', 'lift', 'bed']

def usage():
	print """usage"""
	pass

def add_data(args, today):
	"""add the following data to report"""
	if len(args) > 1 and args[0] in accepted:
		# combine all other arguments but seperatae by ,
		lines = '\n'.join([args[0] + ':\t' + k.strip()
				for k in (' '.join(args[1:])).split(',')])
		print lines
		
		try:
			with open('reports/' + today, 'a') as f:
				f.write(lines + '\n')
		except IOError:
			'Error in writing file.'


if __name__ == '__main__':
	os.chdir('/cygdrive/d/Dropbox/.todo/')

	args = sys.argv[1:]
	today = datetime.date.today().strftime('%Y-%m-%d')
	
	while len(args) > 0 and args[0] in ['-d', '-b']:
		if args[0] == '-d':
			today = args[1]

		if args[0] == '-b':
			today = (datetime.date.today() - 
				     datetime.timedelta(int(args[1]))).strftime('%Y-%m-%d')
			
		# process next args
		args = args[2:]


	if len(args) == 0 or args[0] == 'show':
		try:
			with open('reports/' + today) as f:
				print today
				print ''.join(f.readlines())
				print '\n'
		except IOError:
			print 'No file Exists yet for %s.' % today
			args = ['wake']
			args.extend(raw_input('when did you wake up today? ').split(' '))
			add_data(args, today)
			args = ['eat']
			args.extend(raw_input('what did you eat so far today? ').split(' '))
			add_data(args, today)

	elif args[0] == 'clear':
		if raw_input('remove file? [y/n] ') == 'y':
			os.remove('reports/' + today)
		args = args[1:]

	add_data(args, today)
	
