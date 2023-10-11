# Generated by Django 4.2.5 on 2023-10-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_admindata_delete_alerts_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Details',
            fields=[
                ('admin_id', models.IntegerField(db_column='Admin_ID', primary_key=True, serialize=False)),
                ('admin_name', models.CharField(db_column='Admin_Name', max_length=45)),
                ('admin_dept', models.CharField(db_column='Admin_Dept', max_length=45)),
                ('admin_contact', models.IntegerField(db_column='Admin_Contact', unique=True)),
                ('admin_email', models.CharField(db_column='Admin_Email', max_length=45, unique=True)),
                ('admin_address', models.CharField(db_column='Admin_Address', max_length=45)),
                ('admin_login_password', models.CharField(db_column='Admin_Login_Password', max_length=45, unique=True)),
            ],
            options={
                'db_table': 'admin_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('alert_id', models.IntegerField(db_column='Alert_ID', primary_key=True, serialize=False)),
                ('alert_dept', models.CharField(db_column='Alert_Dept', max_length=45)),
                ('alert_notification', models.CharField(db_column='Alert_Notification', max_length=150)),
                ('alert_state', models.CharField(db_column='Alert_State', max_length=45)),
                ('alert_type', models.CharField(db_column='Alert_Type', max_length=45)),
            ],
            options={
                'db_table': 'alerts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_id', models.CharField(db_column='Dept_id', max_length=45, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(db_column='Dept_Name', max_length=45)),
                ('dept_desc', models.CharField(db_column='Dept_Desc', max_length=45)),
            ],
            options={
                'db_table': 'dept',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Emergency_Contacts',
            fields=[
                ('emergency_contacts_id', models.IntegerField(db_column='Emergency_contacts_ID', primary_key=True, serialize=False)),
                ('emergency_contact_type', models.CharField(db_column='Emergency_Contact_Type', max_length=45)),
                ('emergency_number', models.IntegerField(db_column='Emergency_Number', unique=True)),
                ('emergency_precautions', models.CharField(db_column='Emergency_Precautions', max_length=150)),
            ],
            options={
                'db_table': 'emergency_contacts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News_and_Updates',
            fields=[
                ('news_id', models.IntegerField(db_column='News_ID', primary_key=True, serialize=False)),
                ('news_updates_dept', models.CharField(db_column='News&Updates_Dept', max_length=45)),
                ('news', models.CharField(blank=True, db_column='News', max_length=150, null=True)),
                ('updates', models.CharField(blank=True, db_column='Updates', max_length=150, null=True)),
                ('advisory', models.CharField(blank=True, db_column='Advisory', max_length=150, null=True)),
            ],
            options={
                'db_table': 'news&updates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Precautionary_Advisory',
            fields=[
                ('precautionary_advisory_id', models.IntegerField(db_column='Precautionary_advisory_ID', primary_key=True, serialize=False)),
                ('precautionary_advisory_state', models.CharField(db_column='Precautionary_advisory_State', max_length=45)),
                ('precautionary_advisory_dos', models.CharField(db_column='Precautionary_advisory_DOs', max_length=45)),
                ('precautionary_advisory_donts', models.CharField(db_column='Precautionary_advisory_DONTs', max_length=45)),
                ('precautionary_advisory', models.CharField(db_column='Precautionary_advisory', max_length=45)),
            ],
            options={
                'db_table': 'precautionary_advisory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Schemes',
            fields=[
                ('scheme_id', models.IntegerField(db_column='Scheme_ID', primary_key=True, serialize=False)),
                ('scheme_dept', models.CharField(db_column='Scheme_Dept', max_length=45)),
                ('scheme_type', models.CharField(db_column='Scheme_Type', max_length=45)),
                ('scheme_data', models.CharField(db_column='Scheme_Data', max_length=45)),
                ('scheme_location', models.CharField(db_column='Scheme_Location', max_length=45)),
            ],
            options={
                'db_table': 'schemes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Training_Data',
            fields=[
                ('training_id', models.IntegerField(db_column='Training_ID', primary_key=True, serialize=False)),
                ('training_type', models.CharField(db_column='Training_Type', max_length=45)),
                ('training_area', models.CharField(db_column='Training_Area', max_length=45)),
                ('training_dept', models.CharField(db_column='Training_Dept', max_length=45)),
                ('training_info', models.CharField(db_column='Training_Info', max_length=150)),
            ],
            options={
                'db_table': 'training_data',
                'managed': False,
            },
        ),
    ]
