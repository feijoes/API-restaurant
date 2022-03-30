# Generated by Django 4.0.3 on 2022-03-30 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('nome', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('info', models.CharField(max_length=255)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.IntegerField(default=0)),
                ('pratos', models.ManyToManyField(related_name='pedido_pratos', related_query_name='pedido_pratos', through='core.Count', to='core.prato')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('nome', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('pratos', models.ManyToManyField(related_name='pratos', related_query_name='pratos', to='core.prato')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='count',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pedido'),
        ),
        migrations.AddField(
            model_name='count',
            name='prato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.prato'),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pedido', to='core.pedido')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]