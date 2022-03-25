from django.db import models
from utils.models import BaseModel
from post.models import Post

class Cost(BaseModel):
    ti = models.CharField(max_length=30)
    bo = models.TextField()

    def __str__(self) -> str:
        return self.ti

class Bost(BaseModel):
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to="post/%d/", blank=True)
    ma = models.ForeignKey(Post, on_delete=models.DO_NOTHING, db_constraint=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
