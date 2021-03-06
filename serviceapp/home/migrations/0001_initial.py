# Generated by Django 2.2.5 on 2021-01-30 17:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('advert_id', models.CharField(db_column='ADVERTID', max_length=20, primary_key=True, serialize=False)),
                ('advert_name', models.CharField(db_column='ADVERTNAME', max_length=100)),
                ('price', models.IntegerField(db_column='PRICE', default=0)),
                ('summary', models.CharField(db_column='ADVSUMMARY', max_length=500)),
            ],
            options={
                'db_table': 'ADVERT',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('session_id', models.CharField(db_column='SESSIONID', max_length=20, primary_key=True, serialize=False)),
                ('session_date', models.DateField(db_column='SESSIONDATE')),
                ('hour', models.IntegerField(db_column='SESSIONHOUR')),
            ],
            options={
                'db_table': 'SCHEDULE',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_name', models.CharField(db_column='SERVICENAME', max_length=20, primary_key=True, serialize=False)),
                ('summary', models.CharField(db_column='SERVSUMMARY', max_length=500)),
                ('category', models.CharField(db_column='CATEGORY', default='Undefined', max_length=20)),
            ],
            options={
                'db_table': 'SERVICE',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(db_column='GUID', max_length=20, primary_key=True, serialize=False)),
                ('hashpass', models.BinaryField(db_column='HASHPASS', default=b'')),
                ('key', models.BinaryField(db_column='KEY', default=b'')),
                ('name', models.CharField(db_column='NAME', max_length=30)),
                ('surname', models.CharField(db_column='SURNAME', max_length=30)),
                ('mail', models.EmailField(db_column='MAIL', max_length=254, unique=True)),
                ('score', models.FloatField(db_column='USER_SCORE', default=0)),
                ('location', models.CharField(db_column='LOCATION', default='İstanbul', max_length=100)),
            ],
            options={
                'db_table': 'USER',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.OneToOneField(db_column='CUSID', max_length=20, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.User')),
            ],
            options={
                'db_table': 'CUSTOMER',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('provider_id', models.OneToOneField(db_column='PROID', max_length=20, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.User')),
                ('experience', models.IntegerField(db_column='EXP')),
                ('speciality', models.ForeignKey(db_column='SPECIALITY', default='', on_delete=django.db.models.deletion.CASCADE, to='home.Service')),
            ],
            options={
                'db_table': 'PROVIDER',
            },
        ),
        migrations.CreateModel(
            name='ServiceOffer',
            fields=[
                ('service_offer_id', models.CharField(db_column='SERVICEOFFID', max_length=20, primary_key=True, serialize=False)),
                ('customer_conditions', models.CharField(db_column='CUSTOMERCOND', max_length=1000)),
                ('status', models.CharField(db_column='STATUS', default='Undetermined', max_length=10)),
                ('customer_performance', models.IntegerField(db_column='CUSTOMERSCORE', null=True)),
                ('provider_performance', models.IntegerField(db_column='PROVIDERSCORE', null=True)),
                ('adv_id', models.ForeignKey(db_column='ADVERID', on_delete=django.db.models.deletion.CASCADE, to='home.Advert')),
                ('purchaser', models.ForeignKey(db_column='PURCHASERID', on_delete=django.db.models.deletion.CASCADE, to='home.Customer')),
            ],
            options={
                'db_table': 'SERVICEOFFER',
            },
        ),
        migrations.CreateModel(
            name='OfferSessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_id', models.ForeignKey(db_column='SOFFERID', on_delete=django.db.models.deletion.CASCADE, to='home.ServiceOffer')),
                ('session_id', models.ForeignKey(db_column='SESSID', on_delete=django.db.models.deletion.CASCADE, to='home.Schedule')),
            ],
            options={
                'db_table': 'OFFERSESSION',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.CharField(db_column='MESID', max_length=20, primary_key=True, serialize=False)),
                ('context', models.CharField(db_column='CONTEXT', max_length=100)),
                ('sendtime', models.DateTimeField(db_column='SENDTIME', default=django.utils.timezone.now)),
                ('mesoffid', models.ForeignKey(db_column='MESOFFID', max_length=20, on_delete=django.db.models.deletion.CASCADE, to='home.ServiceOffer')),
                ('sender', models.ForeignKey(db_column='SENDERID', on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
            options={
                'db_table': 'MESSAGE',
            },
        ),
        migrations.AddField(
            model_name='advert',
            name='advert_service',
            field=models.ForeignKey(db_column='ADVSERVICE', default='', on_delete=django.db.models.deletion.CASCADE, to='home.Service'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='customer_id',
            field=models.ForeignKey(db_column='CUSTID', max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Customer'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='expert_id',
            field=models.ForeignKey(db_column='EXPERTID', max_length=20, on_delete=django.db.models.deletion.CASCADE, to='home.Provider'),
        ),
        migrations.CreateModel(
            name='SatisfactionFails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failure', models.CharField(db_column='FAILURE', max_length=20)),
                ('satisfaction_id', models.ForeignKey(db_column='SATISFACID', max_length=20, on_delete=django.db.models.deletion.CASCADE, to='home.ServiceOffer')),
            ],
            options={
                'db_table': 'SATISFACTIONFAIL',
                'unique_together': {('satisfaction_id', 'failure')},
            },
        ),
        migrations.AddField(
            model_name='advert',
            name='prov_id',
            field=models.ForeignKey(db_column='PROVID', max_length=20, on_delete=django.db.models.deletion.CASCADE, to='home.Provider'),
        ),
    ]
