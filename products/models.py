from django.db import models
from django.utils import timezone
# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField( max_digits=6 , decimal_places=2 )
    photo = models.ImageField(upload_to="photo/%Y/%M/%D")
    is_active = models.BooleanField( default=True )
    publish_date = models.DateTimeField(default =timezone.now)
    class Meta:
        ordering=["-publish_date"]
    def __str__(self):
        return self.name






'''

Strict Mode 
يخش علي ملف الاعدادات فنفس المكان الي كتب فيه اليوزر نيم و الباصورد يضيف تحتهم العنصر دا 
        'OPTIONS': {

            'init_command': 'SET default_storage_engine=INNODB',

            'sql_mode': 'traditional'

        }
الــ init_command
دي عباره عن امر SQL بيتكتب جواها وبينفذو الدجانجو كل ما يجي ينشئ جدول و الامر الي جواها بيغير الstorage engine ل innodb
و الــ sql_mode دا السبب في التحذير المشكله بتكون ان الmysql انت لو جيت تحط ف حقل معين مثلا عدد حروف 10 وهوا بياخد 5 حروف بس الي هيحصل ان الmysql مش بتلغي عمليه الاضافه دي لا بتضيفها عادي ولاكن بعد ما تعمل trancate للداتا دي يعني بتغير شكلها بما يتناسب مع الحقل يعني من الاخر الداتا مش هتتحط فالحقل زي ما انت كاتبها و الmysql بتطلعلك تحذير ولاكن التحذير دا الدجانجو مبيقدرش يوصلو عشان يتعامل معاه
ف الحل  في امر في الmysql 
set session sql_mode='traditional';
دا هيخلي الmysql ترفض اي داتا مش صحيحه او out-of-range values 
ف بدل ما تروح تنفذ الامر دا علي الmysql عندك فـ الــ OPTIONS هتضيف دا 
'sql_mode': 'traditional'

'''