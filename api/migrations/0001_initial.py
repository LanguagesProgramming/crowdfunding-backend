# Generated by Django 5.1.5 on 2025-01-29 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignTable',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('TECHNOLOGY', 'TECHNOLOGY'), ('ART', 'ART'), ('FASHION', 'FASHION')], max_length=25)),
                ('description', models.TextField()),
                ('goal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_money', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'campaign',
            },
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('email', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('phone', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='CampaignMediaTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.TextField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.campaigntable')),
            ],
            options={
                'db_table': 'campaign_media',
            },
        ),
        migrations.CreateModel(
            name='ProductTable',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.campaigntable')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductMediaTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.producttable')),
            ],
            options={
                'db_table': 'product_media',
            },
        ),
        migrations.CreateModel(
            name='PurchaseTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.producttable')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usertable')),
            ],
            options={
                'db_table': 'purchase',
            },
        ),
        migrations.CreateModel(
            name='DonationTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.campaigntable')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usertable')),
            ],
            options={
                'db_table': 'donation',
            },
        ),
        migrations.AddField(
            model_name='campaigntable',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usertable'),
        ),
    ]
