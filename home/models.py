from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed_to_updates = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/events/', blank=True, null=True)
    pushpay_link = models.URLField(max_length=500, blank=True, null=True)
    event_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    map_embed = models.TextField(null=True, blank=True)  # <-- NEW FIELD

    def __str__(self):
        return self.title  # (fixed minor typo: use self.title)



# ───────────────────────────────────────────────────────────────────────────────
# Add the AboutPage model directly below Event
# ───────────────────────────────────────────────────────────────────────────────

class AboutPage(models.Model):
    """
    A singleton model to hold all the editable text for the About Us page.
    We force pk=1 in save(), so there's only ever one AboutPage row.
    """

    # PAGE TITLES
    title_en    = models.CharField("Page Title (English)", max_length=100, default="About Us")

    # SUBTITLES / TAGLINES
    subtitle_en = models.TextField(
        "Subtitle (English)",
        default="We are One Family in Christ, Multicultural and Bilingual, Gospel-centered and outward-focused."
    )
    subtitle_es = models.TextField(
        "Subtítulo (Español)",
        default="Somos Una familia en Cristo, Multicultural y Bilingüe, centrada en el Evangelio y enfocada hacia el exterior."
    )

    # SERVICE TIMES (we store the entire HTML here, since it’s a short list)
    service_times_en = models.TextField(
        "Service Times (English)",
        blank=True,
        default=(
            "<h2>Sundays / Domingos:</h2>"
            "<ul>"
            "<li><strong>9:45am - 10:00am:</strong> Prayer time / Tiempo de Oración</li>"
            "<li><strong>10:00am - 10:30am:</strong> Coffee & Fellowship / Café y Compañerismo</li>"
            "<li><strong>10:30am:</strong> Bilingual Service</li>"
            "</ul>"
        )
    )

    # CONTACT CARD TEXT
    contact_name    = models.CharField("Contact Name", max_length=100, default="Redemption Mesa")
    contact_email   = models.CharField("Contact Email", max_length=100, default="mesa@redemptionaz.com")
    contact_address = models.CharField("Address", max_length=200, default="1818 E Southern Ave. Suite 5, Mesa, AZ 85204")

    # MISSION STATEMENTS
    mission_en = models.TextField(
        "Our Mission (English)",
        default=(
            "<p>We gather every week to focus — or refocus — on the truth of God’s word and the grace we have through Jesus.<br>"
            "We proclaim God’s truth, submitting ourselves to it, seeking to be transformed.<br>"
            "We collectively worship, not as disconnected individuals but as a community, through music, teaching, prayer, and sacraments.</p>"
            "<p>Because we are a Gospel Centered, Outward focused church, we value our bilingual service as a way to extend the good news of the gospel to all the people in our community.<br>"
            "You can join us in person at 1818 E Southern Ave (Bldg 2, Suite 5) or join us for the livestreamed service on YouTube.</p>"
        )
    )

    mission_es = models.TextField(
        "Nuestra Misión (Español)",
        default=(
            "<p>Nos reunimos cada semana para centrarnos -o reencontrarnos- en la verdad de la palabra de Dios y en la gracia que tenemos a través de Jesús.<br>"
            "Proclamamos la verdad de Dios, sometiéndonos a ella, buscando ser transformados.<br>"
            "Adoramos colectivamente, no como individuos desconectados sino como una comunidad, a través de la música, la enseñanza, la oración y los sacramentos.</p>"
            "<p>Porque somos una iglesia centrada en el Evangelio y enfocada hacia el exterior, valoramos nuestro servicio bilingüe como una forma de extender las buenas noticias del Evangelio a todas las personas de nuestra comunidad.<br>"
            "Usted puede unirse a nosotros en persona en 1818 E Southern Ave (Bldg 2, Suite 5) o unirse a nosotros para el servicio transmitido en vivo por YouTube.</p>"
        )
    )

    def save(self, *args, **kwargs):
        # Force pk=1 so there’s always exactly one AboutPage instance
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return "About Page Content"

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"
