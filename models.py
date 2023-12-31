# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Admin_Details(models.Model):
    admin_id = models.IntegerField(verbose_name="Admin", db_column='Admin_ID', primary_key=True)  # Field name made lowercase.
    admin_name = models.CharField(db_column='Admin_Name', max_length=45)  # Field name made lowercase.
    admin_dept = models.CharField(db_column='Admin_Dept', max_length=45)  # Field name made lowercase.
    admin_contact = models.IntegerField(db_column='Admin_Contact', unique=True)  # Field name made lowercase.
    admin_email = models.CharField(db_column='Admin_Email', unique=True, max_length=45)  # Field name made lowercase.
    admin_address = models.CharField(db_column='Admin_Address', max_length=45)  # Field name made lowercase.
    admin_Login_Password = models.CharField(db_column='Admin_Login_Password', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_details'
        verbose_name_plural = "Admin_Details"


class Alerts(models.Model):
    alert_id = models.IntegerField(db_column='Alert_ID', primary_key=True)  # Field name made lowercase.
    alert_dept = models.CharField(db_column='Alert_Dept', max_length=45)  # Field name made lowercase.
    alert_notification = models.CharField(db_column='Alert_Notification', max_length=150)  # Field name made lowercase.
    alert_state = models.CharField(db_column='Alert_State', max_length=45)  # Field name made lowercase.
    alert_type = models.CharField(db_column='Alert_Type', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alerts'

class Dept(models.Model):
    dept_id = models.CharField(db_column='Dept_id', primary_key=True, max_length=45)  # Field name made lowercase.
    dept_name = models.CharField(db_column='Dept_Name', max_length=45)  # Field name made lowercase.
    dept_desc = models.CharField(db_column='Dept_Desc', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dept'

class Emergency_Contacts(models.Model):
    emergency_contacts_id = models.IntegerField(db_column='Emergency_contacts_ID', primary_key=True)  # Field name made lowercase.
    emergency_contact_type = models.CharField(db_column='Emergency_Contact_Type', max_length=45)  # Field name made lowercase.
    emergency_number = models.IntegerField(db_column='Emergency_Number', unique=True)  # Field name made lowercase.
    emergency_precautions = models.CharField(db_column='Emergency_Precautions', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emergency_contacts'


class News_and_Updates(models.Model):
    news_id = models.IntegerField(db_column='News_ID', primary_key=True)  # Field name made lowercase.
    news_updates_dept = models.CharField(db_column='News&Updates_Dept', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    news = models.CharField(db_column='News', max_length=150, blank=True, null=True)  # Field name made lowercase.
    updates = models.CharField(db_column='Updates', max_length=150, blank=True, null=True)  # Field name made lowercase.
    advisory = models.CharField(db_column='Advisory', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news&updates'


class Precautionary_Advisory(models.Model):
    precautionary_advisory_id = models.IntegerField(db_column='Precautionary_advisory_ID', primary_key=True)  # Field name made lowercase.
    precautionary_advisory_state = models.CharField(db_column='Precautionary_advisory_State', max_length=45)  # Field name made lowercase.
    precautionary_advisory_dos = models.CharField(db_column='Precautionary_advisory_DOs', max_length=45)  # Field name made lowercase.
    precautionary_advisory_donts = models.CharField(db_column='Precautionary_advisory_DONTs', max_length=45)  # Field name made lowercase.
    precautionary_advisory = models.CharField(db_column='Precautionary_advisory', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'precautionary_advisory'


class Schemes(models.Model):
    scheme_id = models.IntegerField(db_column='Scheme_ID', primary_key=True)  # Field name made lowercase.
    scheme_dept = models.CharField(db_column='Scheme_Dept', max_length=45)  # Field name made lowercase.
    scheme_type = models.CharField(db_column='Scheme_Type', max_length=45)  # Field name made lowercase.
    scheme_data = models.CharField(db_column='Scheme_Data', max_length=45)  # Field name made lowercase.
    scheme_location = models.CharField(db_column='Scheme_Location', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schemes'


class Training_Data(models.Model):
    training_id = models.IntegerField(db_column='Training_ID', primary_key=True)  # Field name made lowercase.
    training_type = models.CharField(db_column='Training_Type', max_length=45)  # Field name made lowercase.
    training_area = models.CharField(db_column='Training_Area', max_length=45)  # Field name made lowercase.
    training_dept = models.CharField(db_column='Training_Dept', max_length=45)  # Field name made lowercase.
    training_info = models.CharField(db_column='Training_Info', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'training_data'
