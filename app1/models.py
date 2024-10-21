from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    image = models.ImageField('', upload_to='article_img/', blank=True)
    title = models.CharField('', max_length=20, blank=True, null=True)
    content = models.TextField('', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일자 필드
    updated_at = models.DateTimeField(auto_now=True)  # 작성일자 필드

    def save(self, *args, **kwargs):
        # title이 비어있을 경우 작성일자에 맞춰 기본값 설정
        if not self.title:
            self.title = datetime.now().strftime("%y년 %m월 %d일")
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title