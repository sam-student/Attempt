# Generated by Django 2.0 on 2019-02-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two_GB_Mobiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Average_Rating',
            field=models.TextField(default=' 4'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Browser',
            field=models.TextField(default='HTML5'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Color',
            field=models.TextField(default='Silver, Space Gray, Gold'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='FourGBand',
            field=models.TextField(default='LTE'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='GPS',
            field=models.TextField(default='Yes + A-GPS support & Glonass, BDS, GALILEO'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Games',
            field=models.TextField(default='built-in + downloadable'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Messaging',
            field=models.TextField(default=', SMS (threaded view), MMS, Email, Push Email'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Ram',
            field=models.TextField(default='2GB'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Review_count',
            field=models.TextField(default='90'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='SIM',
            field=models.TextField(default='Single SIM (Nano-SIM)  '),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='ThreeGBand',
            field=models.TextField(default='HSDPA 850 / 900 / 1700(AWS) / 1900 / 2100 '),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Torch',
            field=models.TextField(default='Yes'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='USB',
            field=models.TextField(default='Yes'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Weight',
            field=models.TextField(default='148g'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Wifi',
            field=models.TextField(default='Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot'),
        ),
    ]
