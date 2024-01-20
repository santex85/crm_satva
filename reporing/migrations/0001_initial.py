# Generated by Django 4.2.7 on 2024-01-20 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('report_type', models.CharField(choices=[('INCOME', 'По доходам'), ('EXPENSE', 'Расходам'), ('CLIENT_PROFITABILITY', 'Доходности клиентов')], max_length=50)),
                ('report_date', models.DateTimeField(auto_now_add=True)),
                ('report_content', models.TextField()),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
            },
        ),
    ]
