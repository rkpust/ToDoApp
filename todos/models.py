from django.db import models

# Create your models here.
class ToDo(models.Model):
    content = models.TextField()
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.content}'

    class Meta:
        verbose_name_plural = "ToDos"
        # db_table = 'ToDos'
