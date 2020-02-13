from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model): #괄호안의 models.Model 을통해 Post클래가 장고모델임을 의미
    #이 코드 덕에 장고는 Post가 데이터 베이스에 저장되어야 한다고 알게됌
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #models. ForeignKey -> 다른 모델에 대한 링크를 의미
    #title, text, created_date, published_date, author 등 속성정의
    title = models.CharField(max_length=200) #글자수가 제한된 텍스트를 정의
    text = models.TextField() #글자수에 제한이 없는 긴 텍스트를 담기위한 속성
    created_data = models.DateTimeField(  #날짜와 시간을 의미
        default=timezone.now)
    published_data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title