# Generated by Django 4.2.5 on 2023-10-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_admin_details_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.CharField(db_column='Dept_id', max_length=45, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(db_column='Dept_Name', max_length=45)),
                ('dept_desc', models.CharField(db_column='Dept_Desc', max_length=45)),
            ],
            options={
                'verbose_name_plural': 'Department',
                'db_table': 'dept',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Dept',
        ),
        migrations.AlterModelOptions(
            name='admin_details',
            options={'managed': False, 'verbose_name_plural': 'Admin Details'},
        ),
        migrations.AlterModelOptions(
            name='alerts',
            options={'managed': False, 'verbose_name_plural': 'Alerts'},
        ),
        migrations.AlterModelOptions(
            name='emergency_contacts',
            options={'managed': False, 'verbose_name_plural': 'Emergency Contacts'},
        ),
        migrations.AlterModelOptions(
            name='news_and_updates',
            options={'managed': False, 'verbose_name_plural': 'News and Updates'},
        ),
        migrations.AlterModelOptions(
            name='precautionary_advisory',
            options={'managed': False, 'verbose_name_plural': 'Precautionary Advisory'},
        ),
        migrations.AlterModelOptions(
            name='schemes',
            options={'managed': False, 'verbose_name_plural': 'Schemes'},
        ),
        migrations.AlterModelOptions(
            name='training_data',
            options={'managed': False, 'verbose_name_plural': 'Training Data'},
        ),
    ]
