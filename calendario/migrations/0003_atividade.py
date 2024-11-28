# Generated by Django 5.1.1 on 2024-11-26 22:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0002_remove_tarefa_categoria_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('producao', 'Produção'), ('colheita', 'Colheita'), ('cuidados', 'Cuidados')], max_length=20)),
                ('descricao', models.TextField()),
                ('data_realizacao', models.DateField()),
                ('realizada', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]