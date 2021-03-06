from django.conf import settings
from django.contrib.auth.models import check_password
from django.utils import timezone

from models import Competition
from models import Team
from models import Admin

class TeamAuth(object):
	def authenticate(self, username = None, password = None, compid = None):
		try:
			team_obj = Team.objects.get(username = username, password = password, compid = compid)
			comp_obj = Competition.objects.get(compid = compid)
			# Prevents users from loggin into the competition before it starts
			if comp_obj.datetime_start > timezone.now():
				return None
			return team_obj
		except:
			return None

	def get_user(self, teamid):
		try:
			return Team.objects.get(teamid = teamid)
		except Team.DoesNotExist:
			return None

class AdminAuth(object):
	def authenticate(self, username = None, password = None):
		try:
			admin = Admin.objects.get(username = username, password = password)
			return admin
		except:
			return None

	def get_user(self, userid):
		try:
			return Admin.objects.get(userid = userid)
		except Admin.DoesNotExist:
			return None