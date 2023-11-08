# Generated by Django 4.2.7 on 2023-11-08 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('unidade', models.CharField(max_length=256)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ValorNutricional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('calorias', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('ingredientes', models.ManyToManyField(to='app.ingrediente')),
            ],
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='valor_nutricional',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.valornutricional'),
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrelas', models.IntegerField()),
                ('receita', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.receita')),
            ],
        ),
    ]