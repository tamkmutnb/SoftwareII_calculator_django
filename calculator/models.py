from django.db import models

class UserInput(models.Model):
	#topic = models.ForeignKey(topic, on_delete=models.DO_NOTHING,)
	objects = None
	user_x = models.TextField(max_length=200, blank=True, null=True)
	user_y = models.TextField(max_length=200, blank=True, null=True)
	user_operator = models.CharField(max_length=200, blank=True, null=True)
	result = models.TextField(max_length=200, blank=True, null=True)


'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''