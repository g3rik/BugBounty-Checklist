# Generated by Django 4.1.6 on 2023-10-12 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_checklistpoint_testresult_website_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterChecklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('payload', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output', models.TextField()),
                ('test_date', models.DateField()),
                ('checkpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklist.masterchecklist')),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklist.website')),
            ],
        ),
        migrations.RemoveField(
            model_name='checklistpoint',
            name='checklist',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='checklist',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='checklist_point',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='website',
        ),
        migrations.DeleteModel(
            name='Checklist',
        ),
        migrations.DeleteModel(
            name='ChecklistPoint',
        ),
        migrations.DeleteModel(
            name='TestResult',
        ),
    ]
