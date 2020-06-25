from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Test(models.Model):
    category = models.ForeignKey(Category, related_name='tests', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='tests', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    questions_id = ArrayField(models.IntegerField(), null=True, blank=True)
    image = models.ImageField(upload_to='test_image')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} {self.user.username} {self.title}'
    
    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('test-detail', kwargs={'pk': self.pk})


class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    problem = models.TextField()

    def __str__(self):
        return self.problem
    

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f'{self.id} {self.text} {self.is_correct}'


class TestResult(models.Model):
    user = models.ForeignKey(User, related_name='test_results', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='test_results', on_delete=models.CASCADE)
    correct_answers = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} {self.test.title} result'


class UserAnswer(models.Model):
    user = models.ForeignKey(User, related_name='user_answers', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='user_answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='user_answers', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, related_name='user_answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' answer'


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}\'s likes on {self.test.title}'


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'comment: {self.text} of {self.user.username} on {self.test.title}'

