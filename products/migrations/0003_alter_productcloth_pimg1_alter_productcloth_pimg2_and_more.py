# Generated by Django 4.0 on 2022-01-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productcloth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcloth',
            name='pimg1',
            field=models.FileField(null=True, upload_to='products/clothes/'),
        ),
        migrations.AlterField(
            model_name='productcloth',
            name='pimg2',
            field=models.FileField(null=True, upload_to='products/clothes/'),
        ),
        migrations.AlterField(
            model_name='productcloth',
            name='pimg3',
            field=models.FileField(null=True, upload_to='products/clothes/'),
        ),
        migrations.AlterField(
            model_name='productcloth',
            name='pimg4',
            field=models.FileField(null=True, upload_to='products/clothes/'),
        ),
        migrations.AlterField(
            model_name='productcloth',
            name='pimg5',
            field=models.FileField(null=True, upload_to='products/clothes/'),
        ),
        migrations.AlterField(
            model_name='productcloth',
            name='pimg6',
            field=models.FileField(null=True, upload_to='products/clothes/'),
        ),
        migrations.AlterField(
            model_name='productcloth',
            name='pimg7',
            field=models.FileField(null=True, upload_to='products/clothes/'),
        ),
        migrations.AlterField(
            model_name='productcloth',
            name='pimg8',
            field=models.FileField(null=True, upload_to='products/clothes/'),
        ),
    ]
