# Generated by Django 4.0.1 on 2022-01-10 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_lead', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('fone_celular', models.CharField(max_length=20)),
                ('fone_whatsapp', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=200)),
                ('uf', models.CharField(max_length=2)),
                ('obs', models.TextField(blank=True, max_length=400)),
                ('cupon', models.CharField(max_length=20)),
                ('data_cadastro', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='leads',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='complemento',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='cupom',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='numero',
        ),
        migrations.AddField(
            model_name='leads',
            name='cliente_ativado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='leads',
            name='cidade',
            field=models.CharField(choices=[('1', 'Felipe Guerra'), ('2', 'Gov. Dix-Sept Rosado')], max_length=200),
        ),
        migrations.AlterField(
            model_name='leads',
            name='obs',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='leads',
            name='uf',
            field=models.CharField(choices=[('RN', 'RN')], max_length=2),
        ),
        migrations.AddField(
            model_name='leads',
            name='cupon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='form_lead.cupon'),
        ),
    ]
