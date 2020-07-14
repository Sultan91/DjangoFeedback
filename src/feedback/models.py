from django.db import models

# Create your models here.


class Feedback(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()


class Question(models.Model):
    type1 = 'TXT'
    type2 = 'single_choice'
    type3 = 'multiple_choice'
    CHOICES = [
        (type1, " Text question"),
        (type2, "Single choice"),
        (type3, "Multiple choice"),
    ]
    question = models.TextField(max_length=300)
    question_type = models.CharField(max_length=200,
                                     choices=CHOICES,
                                     default=type1)
    feedback = models.ForeignKey(to=Feedback, on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=400)
    respondent = models.CharField(max_length=100)
