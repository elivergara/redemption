# Generated by Django 5.1.5 on 2025-05-31 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_event_event_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(default='About Us', max_length=100, verbose_name='Page Title (English)')),
                ('subtitle_en', models.TextField(default='We are One Family in Christ, Multicultural and Bilingual, Gospel-centered and outward-focused.', verbose_name='Subtitle (English)')),
                ('subtitle_es', models.TextField(default='Somos Una familia en Cristo, Multicultural y Bilingüe, centrada en el Evangelio y enfocada hacia el exterior.', verbose_name='Subtítulo (Español)')),
                ('service_times_en', models.TextField(blank=True, default='<h2>Sundays / Domingos:</h2><ul><li><strong>9:45am - 10:00am:</strong> Prayer time / Tiempo de Oración</li><li><strong>10:00am - 10:30am:</strong> Coffee & Fellowship / Café y Compañerismo</li><li><strong>10:30am:</strong> Bilingual Service</li></ul>', verbose_name='Service Times (English)')),
                ('contact_name', models.CharField(default='Redemption Mesa', max_length=100, verbose_name='Contact Name')),
                ('contact_email', models.CharField(default='mesa@redemptionaz.com', max_length=100, verbose_name='Contact Email')),
                ('contact_address', models.CharField(default='1818 E Southern Ave. Suite 5, Mesa, AZ 85204', max_length=200, verbose_name='Address')),
                ('mission_en', models.TextField(default='<p>We gather every week to focus — or refocus — on the truth of God’s word and the grace we have through Jesus.<br>We proclaim God’s truth, submitting ourselves to it, seeking to be transformed.<br>We collectively worship, not as disconnected individuals but as a community, through music, teaching, prayer, and sacraments.</p><p>Because we are a Gospel Centered, Outward focused church, we value our bilingual service as a way to extend the good news of the gospel to all the people in our community.<br>You can join us in person at 1818 E Southern Ave (Bldg 2, Suite 5) or join us for the livestreamed service on YouTube.</p>', verbose_name='Our Mission (English)')),
                ('mission_es', models.TextField(default='<p>Nos reunimos cada semana para centrarnos -o reencontrarnos- en la verdad de la palabra de Dios y en la gracia que tenemos a través de Jesús.<br>Proclamamos la verdad de Dios, sometiéndonos a ella, buscando ser transformados.<br>Adoramos colectivamente, no como individuos desconectados sino como una comunidad, a través de la música, la enseñanza, la oración y los sacramentos.</p><p>Porque somos una iglesia centrada en el Evangelio y enfocada hacia el exterior, valoramos nuestro servicio bilingüe como una forma de extender las buenas noticias del Evangelio a todas las personas de nuestra comunidad.<br>Usted puede unirse a nosotros en persona en 1818 E Southern Ave (Bldg 2, Suite 5) o unirse a nosotros para el servicio transmitido en vivo por YouTube.</p>', verbose_name='Nuestra Misión (Español)')),
            ],
            options={
                'verbose_name': 'About Page',
                'verbose_name_plural': 'About Page',
            },
        ),
    ]
