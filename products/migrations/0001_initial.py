# Generated by Django 3.2.6 on 2021-11-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mid', models.CharField(max_length=16, null=True)),
                ('Mname', models.CharField(max_length=400, null=True)),
                ('Moverview', models.CharField(max_length=400, null=True)),
                ('Muses', models.CharField(max_length=800, null=True)),
                ('Mbenifits', models.CharField(max_length=800, null=True)),
                ('Msideeffects', models.CharField(max_length=800, null=True)),
                ('Mhowtouse', models.CharField(max_length=800, null=True)),
                ('Mhowdrugworks', models.CharField(max_length=800, null=True)),
                ('Msafetyadvise', models.CharField(max_length=800, null=True)),
                ('Mmisseddose', models.CharField(max_length=1000, null=True)),
                ('Mquicktips', models.CharField(max_length=1500, null=True)),
                ('Mmanufacturer', models.CharField(max_length=100, null=True)),
                ('Mexpiry', models.DateField(null=True)),
                ('Mmakingdate', models.DateField(null=True)),
                ('Mmarkedprice', models.IntegerField(null=True)),
                ('Mdiscount', models.IntegerField(null=True)),
                ('Msellingprice', models.IntegerField(null=True)),
                ('Mimage1', models.FileField(null=True, upload_to='')),
                ('Mimage2', models.FileField(null=True, upload_to='')),
                ('Mimage3', models.FileField(null=True, upload_to='')),
                ('Mimage4', models.FileField(null=True, upload_to='')),
                ('Mimage5', models.FileField(null=True, upload_to='')),
                ('Mimage6', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
