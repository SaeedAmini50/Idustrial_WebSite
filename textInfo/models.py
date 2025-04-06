from django.db import models
import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class TextEntry(models.Model):
    SELECT_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    ]

    id = models.AutoField(primary_key=True)
    unique_id = models.CharField(
        max_length=50,
        unique=True,
        help_text="شناسه یکتا برای کنترل ترتیب نمایش (به صورت خودکار ایجاد می‌شود)",
        blank=True  # اجازه خالی بودن در فرم
    )
    entry_id = models.CharField(max_length=20, unique=True, help_text="Auto-generated unique identifier")
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='text_entries')
    image = models.ImageField(upload_to='text_entries/', null=True, blank=True)
    display_order = models.PositiveIntegerField(default=0, help_text="Order in which this entry should be displayed (0 = first)")
    is_visible = models.BooleanField(default=True, help_text="Whether this entry should be displayed on the site")
    select_option = models.CharField(max_length=1, choices=SELECT_CHOICES, default='1', help_text="Select an option from 1 to 6")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.unique_id:
            # اگر unique_id خالی باشد، یک شماره جدید ایجاد می‌کنیم
            last_entry = TextEntry.objects.order_by('-id').first()
            if last_entry and last_entry.unique_id:
                try:
                    # سعی می‌کنیم آخرین شماره را پیدا کنیم
                    last_number = int(last_entry.unique_id)
                    new_number = last_number + 1
                except ValueError:
                    new_number = 1
            else:
                new_number = 1
            
            # فقط عدد را به عنوان شناسه ذخیره می‌کنیم
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
        verbose_name = 'Text Entry'
        verbose_name_plural = 'Text Entries'
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
    logo = models.ImageField(upload_to='logos/', verbose_name='لوگو', null=True, blank=True)

    class Meta:
        verbose_name = 'اطلاعات هدر'
        verbose_name_plural = 'اطلاعات هدر'

    def __str__(self):
        return self.company_name




