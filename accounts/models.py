from django.db import models
from random import randint
from django.core.validators import RegexValidator #전화번호 입력을 위한 유효성검사
 
# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')
    user_pwd = models.CharField(max_length=128, verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length=32, unique=True, verbose_name='유저 이름')
    phoneNumRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    user_phone = models.CharField(validators = [phoneNumRegex], max_length=11, unique=True, verbose_name='유저 전화번호')
    #OneToOneField.. 어떻게 할지 생각해볼것
    
    def __str__(self):
        return self.user_name
    
    class Meta:
        db_table = 'user' #테이블 이름
        verbose_name = '유저' 
        verbose_name_plural = '유저'

class Authentication(models.Model):
    phone_number = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_phone')
    #FK로 User을 갖고 있는 phone_number 입장에서 Authentication은 확인용.. 그래서 related_name = user_phone
    auth_number = models.CharField('인증번호', max_length=10)
    
    class Meta:
        db_table = 'authenticaiton' 
        verbose_name_plural = "휴대폰 인증 관리 페이지" # admin 페이지에서 나타나는 설명
    
    def save(self, *args, **kwargs):
        self.auth_number = randint(1000, 10000) #4자리 랜덤 난수 생성
        super().save(*args, **kwargs)
        self.send_sms() # SMS 전송하기(인증번호 포함)
        
    #인증번호 전송
    def send_sms(self):
        timestamp = str