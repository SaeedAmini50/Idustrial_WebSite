from django.db import models
import uuid

# Create your models here.


def get_product_image_filepath(self, filename):
    return 'textInfo/text_images/' + str(self.pk) + '/text_image.png'


def get_default_product_image():
    return "textInfo/text_default_images/default_text_image.png"




class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class TextEntry(models.Model):
    TITLE_SIZE_CHOICES = [
        ('1', 'عنوان خیلی بزرگ (h1)'),
        ('2', 'عنوان بزرگ (h2)'),
        ('3', 'عنوان متوسط (h3)'),
        ('4', 'عنوان کوچک (h4)'),
        ('5', 'عنوان خیلی کوچک (h5)'),
        ('6', 'عنوان خیلی خیلی کوچک (h6)'),
    ]

    id = models.AutoField(primary_key=True)
    unique_id = models.IntegerField(
    unique=True,
    help_text="شناسه یکتا برای کنترل ترتیب نمایش",
    blank=True,
    null=True
)
    entry_id = models.CharField(max_length=20, unique=True, help_text="شناسه یکتا برای هر متن")
    title = models.CharField(max_length=200, verbose_name="عنوان متن")
    content = models.TextField(verbose_name="محتوا")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='text_entries', verbose_name="دسته‌بندی")
    image = models.ImageField(
        upload_to=get_product_image_filepath,
        null=True, 
        blank=True,
        verbose_name="تصویر"
    )
    display_order = models.PositiveIntegerField(
        default=0, 
        help_text="ترتیب نمایش متن (0 = اول)",
        verbose_name="ترتیب نمایش"
    )
    is_visible = models.BooleanField(
        default=True, 
        help_text="آیا این متن در سایت نمایش داده شود؟",
        verbose_name="نمایش در سایت"
    )
    title_size = models.CharField(
        max_length=1, 
        choices=TITLE_SIZE_CHOICES, 
        default='1', 
        help_text="اندازه عنوان متن را انتخاب کنید",
        verbose_name="اندازه عنوان"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    def get_title_html(self):
        """Returns the title wrapped in appropriate HTML tag based on selected size"""
        tag = f'h{self.title_size}'
        return f'<{tag}>{self.title}</{tag}>'

    def save(self, *args, **kwargs):
        if not self.unique_id:
            # اگر unique_id خالی باشد، یک شماره جدید ایجاد می‌کنیم
            last_entry = TextEntry.objects.order_by('-unique_id').first()
            if last_entry and last_entry.unique_id:
                try:
                    # سعی می‌کنیم آخرین شماره را پیدا کنیم
                    last_number = int(last_entry.unique_id)
                    new_number = last_number + 1
                except ValueError:
                    new_number = 1
            else:
                new_number = 1
            
            # عدد را به عنوان شناسه ذخیره می‌کنیم
            self.unique_id = str(new_number)
        
        if not self.entry_id:
            # Get the last entry_id or start from 1
            last_entry = TextEntry.objects.order_by('-id').first()
            if last_entry:
                try:
                    last_number = int(last_entry.entry_id.split('-')[1])
                    new_number = last_number + 1
                except (IndexError, ValueError):
                    new_number = 1
            else:
                new_number = 1
            
            # Format: CAT-001, CAT-002, etc.
            self.entry_id = f"{self.category.name[:3].upper()}-{new_number:03d}"
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.unique_id} - {self.title}"

    class Meta:
        verbose_name = 'متن'
        verbose_name_plural = 'متن‌ها'
        ordering = ['unique_id']



class Number(models.Model):
    name = models.CharField(max_length=200, unique=True)
    value = models.IntegerField()
 
    def __str__(self):
        return f"{self.name}: {self.value}"

class HeaderInfo(models.Model):
    company_name = models.CharField(max_length=200, verbose_name='نام شرکت')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=20, verbose_name='شماره تماس')
    working_hours = models.CharField(max_length=100, verbose_name='ساعت کاری')
    logo = models.ImageField(
        upload_to=get_product_image_filepath,
        default=get_default_product_image,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'اطلاعات هدر'
        verbose_name_plural = 'اطلاعات هدر'

    def __str__(self):
        return self.company_name

class FooterInfo(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=20, verbose_name='شماره تماس')
    location = models.TextField(verbose_name='موقعیت')
    telegram_link = models.URLField(verbose_name='لینک تلگرام', blank=True, null=True)
    aparat_link = models.URLField(verbose_name='لینک آپارات', blank=True, null=True)
    whatsapp_link = models.URLField(verbose_name='لینک واتساپ', blank=True, null=True)
    facebook_link = models.URLField(verbose_name='لینک فیسبوک', blank=True, null=True)
    instagram_link = models.URLField(verbose_name='لینک اینستاگرام', blank=True, null=True)

    class Meta:
        verbose_name = 'اطلاعات فوتر'
        verbose_name_plural = 'اطلاعات فوتر'

    def __str__(self):
        return "اطلاعات فوتر"



class CompanyInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    content = models.TextField(verbose_name='متن')
    image = models.ImageField(
        upload_to=get_product_image_filepath,
        default=get_default_product_image,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'اطلاعات معرفی شرکت'
        verbose_name_plural = 'اطلاعات معرفی شرکت'

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان خدمت')
    content = models.TextField(verbose_name='توضیحات خدمت')
    image = models.ImageField(
        upload_to=get_product_image_filepath,
        default=get_default_product_image,
        null=True,
        blank=True
    )
    service_link = models.URLField(verbose_name='لینک خدمت', blank=True, null=True)
    is_visible = models.BooleanField(default=True, verbose_name='نمایش در سایت')

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'

    def __str__(self):
        return self.title

class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    job_title = models.CharField(max_length=200, verbose_name='عنوان شغلی')
    email = models.EmailField(verbose_name='ایمیل', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='شماره تماس', blank=True, null=True)
    whatsapp_link = models.URLField(verbose_name='لینک واتساپ', blank=True, null=True)
    telegram_link = models.URLField(verbose_name='لینک تلگرام', blank=True, null=True)
    image = models.ImageField(
        upload_to=get_product_image_filepath,
        default=get_default_product_image,
        null=True,
        blank=True
    )
    is_visible = models.BooleanField(default=True, verbose_name='نمایش در سایت')

    class Meta:
        verbose_name = 'کارمند'
        verbose_name_plural = 'کارمندان'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_title}"

class MainPageImage(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات", blank=True)
    image = models.ImageField(
        upload_to='main_page_images/',
        verbose_name="تصویر"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="ترتیب نمایش (0 = اول)",
        verbose_name="ترتیب نمایش"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="آیا این تصویر در صفحه اصلی نمایش داده شود؟",
        verbose_name="فعال"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر صفحه اصلی'
        verbose_name_plural = 'تصاویر صفحه اصلی'
        ordering = ['display_order']

class Project(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'در حال اجرا'),
        ('completed', 'تکمیل شده'),
        ('planned', 'برنامه‌ریزی شده'),
    ]

    title = models.CharField(max_length=200, verbose_name="عنوان پروژه")
    description = models.TextField(verbose_name="توضیحات پروژه")
    image = models.ImageField(
        upload_to='projects/',
        verbose_name="تصویر پروژه"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='projects',
        verbose_name="دسته‌بندی"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_progress',
        verbose_name="وضعیت پروژه"
    )
    project_id = models.CharField(
        max_length=20,
        unique=True,
        help_text="شناسه یکتا برای پروژه",
        verbose_name="شناسه پروژه"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="ترتیب نمایش (0 = اول)",
        verbose_name="ترتیب نمایش"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="آیا این پروژه در سایت نمایش داده شود؟",
        verbose_name="فعال"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    def __str__(self):
        return f"{self.project_id} - {self.title}"

    def get_status_display(self):
        return dict(self.STATUS_CHOICES)[self.status]

    def save(self, *args, **kwargs):
        if not self.project_id:
            # Get the last project_id or start from 1
            last_project = Project.objects.order_by('-id').first()
            if last_project:
                try:
                    last_number = int(last_project.project_id.split('-')[1])
                    new_number = last_number + 1
                except (IndexError, ValueError):
                    new_number = 1
            else:
                new_number = 1
            
            # Format: PRJ-001, PRJ-002, etc.
            self.project_id = f"PRJ-{new_number:03d}"
        
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه‌ها'
        ordering = ['display_order']
