import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	print "foo"
	try:
		DATABASE_URI = os.environ['DATABASE_URI']
	except (KeyError):
		DATABASE_URI = "postgres://kffjeqxcfybuqw:1f9b9331d78c00ea9732f930b5cd75b1e9bb950a8f5eaa5b0862b89e562bebb6@ec2-54-243-55-1.compute-1.amazonaws.com:5432/de1covhitb2945"
