from django.contrib import admin

from .models import Bookmark as BM


#현재폴더에 있는 models.py파일에 BookMark 클래스를 사용할 수 있도록 추가
#bookmark 폴더에 있는 models.py 파일에 BookMark 클래스를 추가
# Register your models here.
#관리자사이트에서 BookMark 모델 클래스에 데이터를 추가/수정/삭제/열람을 할수있도록 등록
admin.site.register(BM)