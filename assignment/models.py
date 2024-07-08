from django.db import models

class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Paragraph(models.Model):
    id=models.AutoField(primary_key=True)
    text=models.TextField()

class Word(models.Model):
    word=models.CharField(max_length=200)
    paragraph=models.ForeignKey(Paragraph,on_delete=models.CASCADE,related_name="word")

    class Meta:
        unique_together=('paragraph','word')


