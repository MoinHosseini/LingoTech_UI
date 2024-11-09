from django.db import models
from datetime import timedelta

class Listening_Exam(models.Model):
    #pk
    name = models.CharField(max_length=31)
    description = models.TextField()
    duration = models.DurationField(default=timedelta(minutes=40))
    questions = models.JSONField()
    

    def duration_in_seconds(self):
        return int(self.duration.total_seconds()) if self.duration else 0



# Create your models here.
class Question(models.Model):
    # answer = models.CharField(max_length=63)
    description = models.TextField()
    category = models.CharField(max_length=12)
    tags = models.CharField(max_length=12)
    score = models.PositiveIntegerField()
    answerCount =  models.PositiveIntegerField()
    class Meta:
        abstract = True



##################################################

class Questions(models.Model):
    question = models.CharField(max_length=127)
    def __str__(self):
        return self.question

class check_table(Question):
    answer = models.JSONField()
    map = models.ImageField(upload_to='table_pics/')
    questions = models.ManyToManyField(Questions, related_name="checktable") 
    
##################################################

class Steps(models.Model):
    step = models.CharField(max_length=127)
    def __str__(self):
        return self.step

class Answers(models.Model):
    answer = models.CharField(max_length=127)
    def __str__(self):
        return self.answer

class flow_chart(Question):
    steps = models.ManyToManyField(Steps, related_name="flowcharts")
    answers = models.ManyToManyField(Answers, related_name="flowcharts")
    answer = models.JSONField()


##################################################


class pair_q(models.Model):
    question = models.CharField(max_length=127)
    def __str__(self):
        return self.question


class pair_a(models.Model):
    answer = models.CharField(max_length=127)
    def __str__(self):
        return self.answer

class Pairs(Question):
    title_q = models.CharField(max_length=63)
    title_a = models.CharField(max_length=63)
    questions = models.ManyToManyField(pair_q, related_name="pairs")
    answers = models.ManyToManyField(pair_a, related_name="pairs")
    answer = models.JSONField()

##################################################


class Points(models.Model):
    point = models.CharField(max_length=15)
    def __str__(self):
        return self.point

class Options(models.Model):
    option = models.CharField(max_length=127)
    def __str__(self):
        return self.option


class Map(Question):
    map = models.ImageField(upload_to='map_pics/')
    points = models.ManyToManyField(Points, related_name="map")
    options = models.ManyToManyField(Options, related_name="map")
    answer = models.JSONField()

##################################################

class Table(Question):
    file = models.FileField(upload_to="table_code/")
    
    answer = models.JSONField()


#####################################################
class Choice(models.model):
    choice = models.CharField(max_length=127)

    def __str__(self):
        return self.choice

class MultipleChoice(Question):
    choices = models.ManyToManyField(Choice, related_name="multiplechoice")
    
##################################################
