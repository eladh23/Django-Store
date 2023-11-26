# Generated by Django 3.2.21 on 2023-11-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supermarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Kids', 'Kids'), ('Fruits', 'Fruits'), ('Vegetables', 'Vegetables'), ('Home appliances', 'Home Appliances'), ('Other', 'Other')], default='Other', max_length=100),
        ),
    ]