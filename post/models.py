from django.db import models
from utils.models import BaseModel


class Most(BaseModel):
    ti = models.CharField(max_length=30)
    bo = models.TextField()

    def __str__(self) -> str:
        return self.ti

class Post(BaseModel):
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to="post/%d/", blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
