from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100) #필드1
    url = models.URLField('site URL') #필드2
    def __str__(self):
        #객체를 출력할 때 나타나는 값
        return 'name : ' + self.site_name +' ,addr: '  + self.url
    def get_absolute_url(self): #장고에서 사용하는 메서드 객체의 상세화면 주소를 반환하게 만든다.
        return reverse('detail',args =[str(self.id)])  # 이때 사용하는 리버스 메서드는 ㅕURL패턴의 이름과 추가인자를 전달받아URL을 생성
# Create your models here.
