# Generated by Django 4.2.5 on 2023-10-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssingnedAuthority',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('members_name', models.CharField(max_length=45)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'assingned_authority',
                'managed': False,
            },
        ),
    ]