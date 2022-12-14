# Generated by Django 4.0.6 on 2022-10-02 00:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=10, null=True)),
                ('home_address', models.CharField(blank=True, max_length=50, null=True)),
                ('work_address', models.CharField(blank=None, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=None)),
                ('Specialization', models.CharField(max_length=20)),
                ('location', models.CharField(choices=[('Baghdad', 'BAGHDAD'), ('Basrah', 'BASRAH'), ('Mosul', 'MOSUL'), ('Other', 'OTHER')], max_length=255)),
                ('sex', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=255)),
                ('availability', models.CharField(choices=[('Available', 'AVAILABLE'), ('NotAvailable', 'NOTAVAILABLE')], max_length=255)),
                ('cv', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=20)),
                ('sunday', models.CharField(blank=True, default='Sunday ', max_length=20, null=True)),
                ('monday', models.CharField(blank=True, default='Monday ', max_length=20, null=True)),
                ('tuesday', models.CharField(blank=True, default='Tuesday ', max_length=20, null=True)),
                ('wednesday', models.CharField(blank=True, default='Wednesday ', max_length=20, null=True)),
                ('thursday', models.CharField(blank=True, default='Thursday ', max_length=20, null=True)),
                ('friday', models.CharField(blank=True, default='Friday ', max_length=20, null=True)),
                ('saturday', models.CharField(blank=True, default='Saturday ', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_qty', models.IntegerField(default=1, verbose_name='item_qty')),
                ('ordered', models.BooleanField(verbose_name='ordered')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('NEW', 'NEW'), ('PROCESSING', 'PROCESSING'), ('SHIPPED', 'SHIPPED'), ('COMPLETED', 'COMPLETED'), ('REFUNDED', 'REFUNDED')], max_length=255, verbose_name='title')),
                ('is_default', models.BooleanField(verbose_name='is default')),
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
                ('clothe_sub_category', models.CharField(blank=True, choices=[('Bijama', 'BIJAMA'), ('T_Shirt', 'T_SHIRT'), ('Underwaer', 'Underwaer')], max_length=255, null=True)),
                ('food_sub_category', models.CharField(blank=True, choices=[('Milk', 'MILK'), ('Instant_Cereal', 'INSTANT_CEREAL')], max_length=255, null=True)),
                ('food_tool_sub_category', models.CharField(blank=True, choices=[('Cup', 'CUP'), ('Baby_Bottle', 'BABY_BOTTLE')], max_length=255, null=True)),
                ('shower_tool_sub_category', models.CharField(blank=True, choices=[('Soap', 'SOAP'), ('Towel', 'TOWEL'), ('Loofah', 'LOOFAH'), ('Shampoo', 'SHAMPOO')], max_length=255, null=True)),
                ('vehicle_sub_category', models.CharField(blank=True, choices=[('Jogger', 'JOGGER'), ('Stroller', 'STROLLER')], max_length=255, null=True)),
                ('container_sub_category', models.CharField(blank=True, choices=[('Fixed', 'FIXED'), ('Movable', 'MOVABLE')], max_length=255, null=True)),
                ('furniture_sub_category', models.CharField(blank=True, choices=[('Cover', 'COVER'), ('Pillow', 'PILLOW'), ('Mattress', 'MATTRESS')], max_length=255, null=True)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=20, null=True)),
                ('size', models.CharField(blank=True, choices=[('Small', 'SMALL'), ('Medium', 'MEDIUM'), ('Large', 'LARGE')], max_length=20, null=True)),
                ('age', models.CharField(blank=True, choices=[('One_To_Six_Months', 'ONE_TO_SIX_MONTHS'), ('More_Than_Six_Months', 'MORE_THAN_SIX_MONTHS')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('comment', models.CharField(max_length=150)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='baby_care.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='note')),
                ('ref_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='ref code')),
                ('ordered', models.BooleanField(blank=True, default=False, null=True, verbose_name='ordered')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='baby_care.address')),
                ('items', models.ManyToManyField(related_name='order', to='baby_care.item', verbose_name='items')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='baby_care.orderstatus', verbose_name='status')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baby_care.product', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baby_care.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
