# Generated by Django 5.0.4 on 2024-04-22 14:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSaude', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='locais/')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='localatendimento',
            name='categoria',
            field=models.CharField(choices=[('clinica', 'Clínica'), ('parque', 'Parque'), ('centro_apoio', 'Centro de Apoio')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='localatendimento',
            name='descricao',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='localatendimento',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='localatendimento',
            name='endereco',
            field=models.CharField(default=django.utils.timezone.now, max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='localatendimento',
            name='faixa_etaria_recomendada',
            field=models.CharField(choices=[('criancas', 'Crianças'), ('adolescentes', 'Adolescentes'), ('adultos', 'Adultos'), ('idosos', 'Idosos')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='localatendimento',
            name='servicos_oferecidos',
            field=models.CharField(choices=[('psicoterapia', 'Psicoterapia'), ('grupos_apoio', 'Grupos de Apoio'), ('atividades_fisicas', 'Atividades Físicas')], default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='localatendimento',
            name='site',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='localatendimento',
            name='validado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profissionalsaude',
            name='local_atendimento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppSaude.localatendimento'),
        ),
        migrations.AddField(
            model_name='profissionalsaude',
            name='registro_profissional',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='locais_cadastrados',
            field=models.ManyToManyField(blank=True, related_name='usuarios_cadastrados', to='AppSaude.localatendimento'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='locais_favoritos',
            field=models.ManyToManyField(blank=True, related_name='usuarios_favoritos', to='AppSaude.localatendimento'),
        ),
        migrations.AlterField(
            model_name='profissionalsaude',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profissional_saude', serialize=False, to='AppSaude.usuario'),
        ),
        migrations.AddField(
            model_name='localatendimento',
            name='imagens',
            field=models.ManyToManyField(related_name='locais', to='AppSaude.imagem'),
        ),
        migrations.CreateModel(
            name='ProblemaLocalAtendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('resolvido', models.BooleanField(default=False)),
                ('local_atendimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppSaude.localatendimento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppSaude.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ProblemaSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('resolvido', models.BooleanField(default=False)),
                ('print', models.ImageField(upload_to='prints/')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppSaude.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='localatendimento',
            name='telefones',
            field=models.ManyToManyField(blank=True, to='AppSaude.telefone'),
        ),
        migrations.CreateModel(
            name='HorarioFuncionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(choices=[('segunda', 'Segunda-feira'), ('terca', 'Terça-feira'), ('quarta', 'Quarta-feira'), ('quinta', 'Quinta-feira'), ('sexta', 'Sexta-feira'), ('sabado', 'Sábado'), ('domingo', 'Domingo')], max_length=10)),
                ('horario_abertura', models.TimeField()),
                ('horario_fechamento', models.TimeField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios_funcionamento', to='AppSaude.localatendimento')),
            ],
            options={
                'unique_together': {('local', 'dia_semana')},
            },
        ),
    ]
