# Generated by Django 3.2.3 on 2021-07-31 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserPanel', '0004_student_std_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='std_image',
            field=models.ImageField(upload_to='upload/'),
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('req_id', models.AutoField(primary_key=True, serialize=False)),
                ('req_reason', models.TextField()),
                ('req_date', models.DateField(auto_now_add=True)),
                ('req_time', models.TimeField(auto_now_add=True)),
                ('std_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserPanel.student')),
            ],
        ),
    ]