# Generated by Django 3.2.8 on 2021-11-03 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instruments', '0002_auto_20211103_2007'),
        ('referencies', '0003_alter_contragent_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerificationScheduleEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(error_messages={'required': 'Event date is requred'}, help_text='Event date', verbose_name='Event date')),
                ('sweep_mark', models.BooleanField(default=False, help_text='Set if item no more be applyable', verbose_name='Hidden')),
                ('instrument', models.ForeignKey(error_messages={'required': 'Instrument is requred'}, help_text='Verifiable instrument', limit_choices_to={'sweep_mark': False}, on_delete=django.db.models.deletion.CASCADE, related_name='instrument', to='instruments.instrument', verbose_name='Instrument')),
                ('validator', models.ForeignKey(error_messages={'required': 'Validator is requred'}, help_text='Validator', limit_choices_to={'sweep_mark': False}, on_delete=django.db.models.deletion.CASCADE, related_name='validator', to='referencies.validator', verbose_name='Validator')),
            ],
        ),
        migrations.CreateModel(
            name='VerificationEvent',
            fields=[
                ('schedule_event', models.OneToOneField(error_messages={'required': 'Event is requred'}, help_text='Planned event for realization', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='verifications.verificationscheduleevent', verbose_name='Shedule event')),
                ('date', models.DateField(error_messages={'required': 'Event date is requred'}, help_text='Event date', verbose_name='Event date')),
                ('result', models.PositiveSmallIntegerField(choices=[(1, 'Exploitation'), (2, 'Preservation'), (3, 'Repairation'), (4, 'Not validated')], error_messages={'required': 'Result is requred'})),
                ('sweep_mark', models.BooleanField(default=False, help_text='Set if item no more be applyable', verbose_name='Hidden')),
            ],
        ),
    ]
