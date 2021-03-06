# Generated by Django 3.1.3 on 2020-12-05 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0002_auto_20201204_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='dfegcn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dfegdp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dffcp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dffec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dffeme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dffemh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dfscs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dfseg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dfsem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dfsep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dfsvbt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dfsvcc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dfsvds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dfsvse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dsfda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dsfos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dsfpd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dsfps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dstca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dstdm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dstds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dstem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dtfcl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dtfds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dtfml',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dtftc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dtsai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dtscd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dtscn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dtsiot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]
