# Generated by Django 4.0.6 on 2022-09-07 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicOpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sunday', models.CharField(blank=True, default='Sunday', max_length=20, null=True)),
                ('monday', models.CharField(blank=True, default='Monday', max_length=20, null=True)),
                ('tuesday', models.CharField(blank=True, default='Tuesday', max_length=20, null=True)),
                ('wednesday', models.CharField(blank=True, default='Wednesday', max_length=20, null=True)),
                ('thursday', models.CharField(blank=True, default='Thursday', max_length=20, null=True)),
                ('friday', models.CharField(blank=True, default='Friday', max_length=20, null=True)),
                ('saturday', models.CharField(blank=True, default='Saturday', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=7)),
                ('image', models.ImageField(upload_to=None)),
                ('stars', models.CharField(max_length=1)),
                ('category', models.CharField(choices=[('Shoe', 'SHOE'), ('Diaper', 'DIAPER'), ('Clothe', 'CLOTHE'), ('Vehicle', 'VEHICLE'), ('Nutrition', 'NUTRITION'), ('Equipment', 'EQUIPMENT'), ('Container', 'CONTAINER'), ('Shower_Tool', 'SHOWER_TOOL')], max_length=20)),
                ('product_sub_category', models.CharField(blank=True, choices=[("<class 'baby_care.models.ProductSubCategoryChoices.ClotheSubCategoryChoices'>", 'Clothesubcategorychoices'), ("<class 'baby_care.models.ProductSubCategoryChoices.FoodSubCategoryChoices'>", 'Foodsubcategorychoices'), ("<class 'baby_care.models.ProductSubCategoryChoices.FoodToolSubCategoryChoices'>", 'Foodtoolsubcategorychoices'), ("<class 'baby_care.models.ProductSubCategoryChoices.ShowerToolSubCategoryChoices'>", 'Showertoolsubcategorychoices'), ("<class 'baby_care.models.ProductSubCategoryChoices.VehicleSubCategoryChoices'>", 'Vehiclesubcategorychoices'), ("<class 'baby_care.models.ProductSubCategoryChoices.ContainerSubCategoryChoices'>", 'Containersubcategorychoices'), ("<class 'baby_care.models.ProductSubCategoryChoices.FurnitureSubCategoryChoices'>", 'Furnituresubcategorychoices')], max_length=255, null=True)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=20, null=True)),
                ('size', models.CharField(blank=True, choices=[('Small', 'SMALL'), ('Medium', 'MEDIUM'), ('Large', 'LARGE')], max_length=20, null=True)),
                ('age', models.CharField(blank=True, choices=[('One_To_Six_Months', 'ONE_TO_SIX_MONTHS'), ('More_Than_Six_Months', 'MORE_THAN_SIX_MONTHS')], max_length=20, null=True)),
                ('is_favourite', models.BooleanField(default=False)),
                ('it_bought', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=None)),
                ('Specialization', models.CharField(max_length=20)),
                ('Working_hours', models.CharField(max_length=20)),
                ('cv', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=20)),
                ('clinic_opening_hours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baby_care.clinicopeninghours')),
            ],
        ),
    ]