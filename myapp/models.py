from django.db import models

# Create your models here.

class AssingnedAuthority(models.Model):
    id = models.IntegerField(primary_key=True)
    members_name = models.CharField(max_length=45)
    phone = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'assingned_authority'

    def __str__(self):
        return self.members_name
    
class Admin_Details(models.Model):
        
    DEPARTMENT_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )

    admin_id = models.IntegerField(verbose_name="Admin Id", db_column='Admin_ID', primary_key=True)  # Field name made lowercase.
    admin_name = models.CharField(db_column='Admin_Name', max_length=45)  # Field name made lowercase.
    admin_dept = models.CharField(verbose_name="Admin Department", db_column='Admin_Dept', max_length=45)  # Field name made lowercase.
    admin_contact = models.IntegerField(db_column='Admin_Contact', unique=True)  # Field name made lowercase.
    admin_email = models.CharField(db_column='Admin_Email', unique=True, max_length=45)  # Field name made lowercase.
    admin_address = models.CharField(db_column='Admin_Address', max_length=45)  # Field name made lowercase.
    admin_login_password = models.CharField(verbose_name="Password", db_column='Admin_Login_Password', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_details'
        verbose_name_plural = "Admin Details"

    def __str__(self):
        return self.admin_name

class Alerts(models.Model):
    DEPARTMENT_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )

    STATE_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )

    TYPE_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )
    alert_id = models.IntegerField(db_column='Alert_ID', primary_key=True)  # Field name made lowercase.
    alert_dept = models.CharField(db_column='Alert_Dept', max_length=45)  # Field name made lowercase.
    alert_notification = models.CharField(db_column='Alert_Notification', max_length=150)  # Field name made lowercase.
    alert_state = models.CharField(db_column='Alert_State', max_length=45)  # Field name made lowercase.
    alert_type = models.CharField(db_column='Alert_Type', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alerts'
        verbose_name_plural = "Alerts"

    def __str__(self):
        return self.alert_type

class Department(models.Model):

    DEPARTMENT_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )

    dept_id = models.CharField(db_column='Dept_id', primary_key=True, max_length=45)  # Field name made lowercase.
    dept_name = models.CharField(db_column='Dept_name', max_length=45, choices=DEPARTMENT_CHOICES)  # Field name made lowercase.
    dept_desc = models.CharField(db_column='Dept_Desc', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dept'
        verbose_name_plural = "Department"

    def __str__(self):
        return self.dept_name

class Schemes(models.Model):

    DEPARTMENT_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )

    TYPE_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )

    LOCATION_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )
    scheme_id = models.IntegerField(db_column='Scheme_ID', primary_key=True)  # Field name made lowercase.
    scheme_dept = models.CharField(db_column='Scheme_Dept', max_length=45)  # Field name made lowercase.
    scheme_type = models.CharField(db_column='Scheme_Type', max_length=45)  # Field name made lowercase.
    scheme_data = models.CharField(db_column='Scheme_Data', max_length=45)  # Field name made lowercase.
    scheme_location = models.CharField(db_column='Scheme_Location', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schemes'
        verbose_name_plural = "Schemes"

    def __str__(self):
        return self.scheme_type

class News_and_Updates(models.Model):
   
    DEPARTMENT_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )
        
    news_id = models.IntegerField(db_column='News_ID', primary_key=True)  # Field name made lowercase.
    news_updates_dept = models.CharField(db_column='News&Updates_Dept', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    news = models.CharField(db_column='News', max_length=150, blank=True, null=True)  # Field name made lowercase.
    updates = models.CharField(db_column='Updates', max_length=150, blank=True, null=True)  # Field name made lowercase.
    advisory = models.CharField(db_column='Advisory', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news&updates'
        verbose_name_plural = "News and Updates"

    def __str__(self):
        return self.members_name
    
class Training_Data(models.Model):

    DEPARTMENT_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )

    TYPE_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )

    training_id = models.IntegerField(db_column='Training_ID', primary_key=True)  # Field name made lowercase.
    training_type = models.CharField(db_column='Training_Type', max_length=45)  # Field name made lowercase.
    training_area = models.CharField(db_column='Training_Area', max_length=45)  # Field name made lowercase.
    training_dept = models.CharField(db_column='Training_Dept', max_length=45)  # Field name made lowercase.
    training_info = models.CharField(db_column='Training_Info', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'training_data'
        verbose_name_plural = "Training Data"

    def __str__(self):
        return self.training_type

class Emergency_Contacts(models.Model):

    TYPE_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )

    emergency_contacts_id = models.IntegerField(db_column='Emergency_contacts_ID', primary_key=True)  # Field name made lowercase.
    emergency_contact_type = models.CharField(db_column='Emergency_Contact_Type', max_length=45)  # Field name made lowercase.
    emergency_number = models.IntegerField(db_column='Emergency_Number', unique=True)  # Field name made lowercase.
    emergency_precautions = models.CharField(db_column='Emergency_Precautions', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emergency_contacts'
        verbose_name_plural = "Emergency Contacts"

    def __str__(self):
        return self.emergency_contacts_id

class Precautionary_Advisory(models.Model):

    STATE_CHOICES = (
        ('1', 'Freshman'),
        ('2', 'sophomore'),
    )

    precautionary_advisory_id = models.IntegerField(db_column='Precautionary_advisory_ID', primary_key=True)  # Field name made lowercase.
    precautionary_advisory_state = models.CharField(db_column='Precautionary_advisory_State', max_length=45)  # Field name made lowercase.
    precautionary_advisory_dos = models.CharField(verbose_name="DOS", db_column='Precautionary_advisory_DOs', max_length=45)  # Field name made lowercase.
    precautionary_advisory_donts = models.CharField(verbose_name="Donts", db_column='Precautionary_advisory_DONTs', max_length=45)  # Field name made lowercase.
    precautionary_advisory = models.CharField(db_column='Precautionary_advisory', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'precautionary_advisory'
        verbose_name_plural = "Precautionary Advisory"

    def __str__(self):
        return self.members_name

