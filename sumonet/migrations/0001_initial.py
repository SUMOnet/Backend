# Generated by Django 5.0.1 on 2024-02-05 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SUMO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein_id', models.CharField(max_length=100)),
                ('peptide_sequence', models.CharField(max_length=100)),
                ('lysine_position', models.IntegerField()),
                ('nonsumoylation_class_probs', models.DecimalField(decimal_places=9, max_digits=10)),
                ('sumoylation_class_probs', models.DecimalField(decimal_places=9, max_digits=10)),
                ('predicted_labels', models.IntegerField()),
            ],
        ),
    ]
