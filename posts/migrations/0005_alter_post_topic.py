# Generated by Django 4.0.6 on 2022-08-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_post_post_topic_post_topic_delete_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.CharField(blank=True, choices=[('LIFE', '가정 / 생활'), ('HEALTH / COOK', '건강 / 요리'), ('ECONOMY / MANAGEMENT', '경제 / 경영'), ('LANGUAGE', '국어 / 외국어'), ('COMPUTER / IT', '컴퓨터 / IT'), ('POLITICS / SOCIETY', '정치 / 사회'), ('LITERATURE', '문학'), ('CHILD', '유아 / 아동'), ('TRAVEL', '여행'), ('HISTORY', '역사'), ('ART', '예술'), ('HUMANITIES', '인문'), ('PEOPLE', '인물'), ('SELF-IMPROVEMENT', '자기계발'), ('SCIENCE', '과학'), ('RELIGION', '종교'), ('CULTURE', '문화'), ('ENGINEERING', '공학')], default=None, max_length=50, null=True),
        ),
    ]
