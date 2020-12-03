from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse


class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('quiz')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=200)
    answer2 = models.CharField(max_length=200)
    answer3 = models.CharField(max_length=200)
    answer4 = models.CharField(max_length=200)
    c_answer = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.answer1}, {self.answer2}, {self.answer3}, {self.answer4}"

    # def get_absolute_url(self):
    #     return reverse('quiz')
