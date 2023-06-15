from django.db import models

class InputTable(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    exception = models.CharField(max_length=255, null=False)
    cluster = models.CharField(max_length=255)
    step = models.CharField(max_length=255)
    time_taken = models.TimeField()
    exception_label = models.CharField(max_length=255)

    def __str__(self):
        return f"InputTable - ID: {self.id}, Exception: {self.exception}, Cluster: {self.cluster}, Step: {self.step}"

class FeedbackDatabase(models.Model):
    id = models.AutoField(primary_key=True)
    exception = models.CharField(max_length=255)
    solution = models.CharField(max_length=255)

    def __str__(self):
        return f"FeedbackDatabase - ID: {self.id}, Exception: {self.exception}"
