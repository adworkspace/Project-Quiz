from django.db import models
from django.contrib.auth.models import User

#Creating models here
# Category model
class Category(models.Model):
    sl_no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default="No Name")
    number_of_questions=models.IntegerField(default=10)
    time=models.IntegerField(help_text="duration of the quiz in minutes.",default=1)
    required_score=models.IntegerField(help_text="required score to pass the quiz.",default=60)
    cat=models.CharField(max_length=50)
    cat_img=models.ImageField(upload_to="static/category_media",blank=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.sl_no) + " " +self.cat

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name_plural='Categories'


    

#Question model
class Question(models.Model):
    q_no=models.AutoField(primary_key=True)
    quest=models.TextField(max_length=500)
    op_1=models.CharField(max_length=50)
    op_2=models.CharField(max_length=50)
    op_3=models.CharField(max_length=50)
    op_4=models.CharField(max_length=50)
    ans=models.CharField(max_length=50)
    desc=models.TextField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return "Question "+str(self.q_no)

# Result model
class Result(models.Model):
    quiz=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    score=models.FloatField()

    def __str__(self):
        return str(self.pk)
