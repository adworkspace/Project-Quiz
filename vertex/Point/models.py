from django.db import models

#Creating models here

class Category(models.Model):
    sl_no=models.AutoField(primary_key=True)
    cat=models.CharField(max_length=50)
    cat_img=models.ImageField(upload_to="static/category_media",blank=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.sl_no) + " " +self.cat


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