from django.db import models

CHOICE = (('danger', 'High'), ('warning', 'normal'), ('primary', 'low'))  # 重要度の選択肢


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=50, choices=CHOICE)
    duedate = models.DateField()

    def __str__(self):
        return self.title
