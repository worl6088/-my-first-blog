from django.contrib import admin
from .models import Post

admin.site.register(Post)
#post모델을 import하고 관리자 페이지에서 만든 모델을 보려면
#위 코드로 모델을 등록해야한다다