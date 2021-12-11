from django.db import models

class Comment(models.Model):
    post_id = models.IntegerField()
    name_index = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '[{}] {}'.format(self.post_id, self.content)
