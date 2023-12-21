# Generated by Django 3.2 on 2023-12-20 15:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(18)])),
                ('fond', models.FloatField(default=0)),
                ('register', models.IntegerField(default=0)),
                ('crypto', models.BooleanField(default=False)),
                ('coin', models.CharField(blank=None, default='Dollar', max_length=20, null=True)),
                ('valoration', models.IntegerField(default=2)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(50)])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('coin', models.CharField(default='Dollar', max_length=20)),
                ('dest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_transactions', to='transactions.client')),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_transactions', to='transactions.client')),
            ],
        ),
    ]
