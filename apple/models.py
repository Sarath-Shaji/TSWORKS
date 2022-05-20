from django.db import models

# Create your models here.
class Apple(models.Model):
    date=models.CharField(max_length=45, primary_key=True)
    open=models.CharField(max_length=45)
    high=models.CharField(max_length=45)
    low=models.CharField(max_length=45)
    close=models.CharField(max_length=45)
    adjclose=models.CharField(max_length=45)
    volume=models.CharField(max_length=45)

    class Meta:
        db_table = 'apple'
        managed = False