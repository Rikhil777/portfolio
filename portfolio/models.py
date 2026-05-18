from django.db import models
import os

class Project(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    github_url  = models.URLField(blank=True)
    image       = models.ImageField(upload_to='projects/', blank=True)
    tech_stack  = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class Skill(models.Model):
    name  = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    job_title   = models.CharField(max_length=200)
    company     = models.CharField(max_length=200)
    location    = models.CharField(max_length=200, blank=True)
    start_date  = models.CharField(max_length=50)
    end_date    = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    order       = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.job_title} at {self.company}'


class Education(models.Model):
    degree      = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location    = models.CharField(max_length=200, blank=True)
    start_year  = models.CharField(max_length=20)
    end_year    = models.CharField(max_length=20, blank=True)
    grade       = models.CharField(max_length=50, blank=True)
    order       = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.degree} — {self.institution}'


class Profile(models.Model):
    name        = models.CharField(max_length=100)
    tagline     = models.CharField(max_length=200)   # "Django backend developer building..."
    bio         = models.TextField(blank=True)        # longer about me text
    photo       = models.ImageField(upload_to='profile/')
    github_url  = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    email       = models.EmailField(blank=True)
    available_for_work = models.BooleanField(default=True)  # controls the green badge

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Profile'  # fixes spelling in admin sidebar


class Certification(models.Model):
    title            = models.CharField(max_length=200)
    issuer           = models.CharField(max_length=200)
    issued_date      = models.CharField(max_length=50)
    certificate_file = models.FileField(upload_to='certificates/', blank=True)
    preview_image    = models.ImageField(upload_to='certificates/previews/', blank=True)
    order            = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.title} — {self.issuer}'

    def is_pdf(self):
        if self.certificate_file:
            return self.certificate_file.name.lower().endswith('.pdf')
        return False

    def is_image(self):
        if self.certificate_file:
            name = self.certificate_file.name.lower()
            return name.endswith(('.jpg', '.jpeg', '.png', '.webp'))
        return False

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Auto-generate preview if it's a PDF and no preview exists yet
        if self.is_pdf() and not self.preview_image and self.certificate_file:
            self._generate_pdf_preview()

    def _generate_pdf_preview(self):
        try:
            from pdf2image import convert_from_path
            from django.core.files.base import ContentFile
            from io import BytesIO

            POPPLER_PATH = r'C:\poppler-26.02.0\Library\bin'  # ← change this to YOUR poppler bin path

            pages = convert_from_path(
                self.certificate_file.path,
                dpi=150,
                first_page=1,
                last_page=1,
                poppler_path=POPPLER_PATH
            )

            if pages:
                img_buffer = BytesIO()
                pages[0].save(img_buffer, format='JPEG', quality=85)
                img_buffer.seek(0)

                filename = os.path.splitext(
                    os.path.basename(self.certificate_file.name)
                )[0] + '_preview.jpg'

                self.preview_image.save(
                    filename,
                    ContentFile(img_buffer.read()),
                    save=True
                )
        except Exception as e:
            print(f'PDF preview generation failed: {e}')