from PIL import Image
import ffmpeg

import os
from django.contrib.auth.models import User
from django.db import models
import mimetypes

# Create your models here.


class Entreprise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entreprises')

    def __str__(self):
        return self.name

class AddressEntreprise(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_address_entreprises')
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='adresses')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contacts(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return f"{self.name} - {self.entreprise.name}"

class Contenu(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='contenus')
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_principal = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    file = models.FileField(upload_to='contenu_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    width = models.IntegerField(null=True, blank=True, editable=False)
    height = models.IntegerField(null=True, blank=True, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contenus')

    def save(self, *args, **kwargs):
        # 1. Sauvegarde d'abord le fichier temporairement pour y avoir accès sur le disque
        super().save(*args, **kwargs)

        # 2. Si les dimensions ne sont pas encore définies
        if not self.width or not self.height:
            path = self.file.path

            try:
                # --- CAS 1 : IMAGE (via Pillow) ---
                if self.file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    with Image.open(path) as img:
                        self.width, self.height = img.size

                # --- CAS 2 : VIDÉO (via FFmpeg) ---
                elif self.file.name.lower().endswith(('.mp4', '.mov', '.avi')):
                    probe = ffmpeg.probe(path)
                    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
                    if video_stream:
                        self.width = int(video_stream['width'])
                        self.height = int(video_stream['height'])
            except Exception as e:
                print(f"Erreur lors de l'extraction des dimensions: {e}")

            super().save(update_fields=['width', 'height'])


    def ratio_string(self):
        if self.width and self.height:
            if self.width > self.height:
                return '16/9'

            elif self.height > self.width:
                return '9/16'

            else:
                return '1/1'

        return "16/9"  # Valeur par défaut

    def get_media_type(self):
        """Retourne 'image', 'video' ou 'unknown'"""
        if not self.file:
            return 'unknown'

        # Devine le type MIME basé sur le nom du fichier
        type_mime, _ = mimetypes.guess_type(self.file.name)

        if type_mime:
            if type_mime.startswith('image'):
                return 'image'
            elif type_mime.startswith('video'):
                return 'video'
        return 'unknown'

    def __str__(self):
        return f"{self.title} - {self.entreprise.name}"



class Projet(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='projets')
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    file = models.FileField(upload_to='projet_files/', null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projets')

    def __str__(self):
        return f"{self.name} - {self.entreprise.name}"


class Realisation(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='realisations')
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='realisation_files/', null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='realisations')

    def __str__(self):
        return f"{self.title} - {self.projet.name}"


class SectionDescription(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='section_descriptions')
    title = models.CharField(max_length=255)
    content = models.TextField()
    file = models.FileField(upload_to='section_description_files/', null=True, blank=True)
    banner = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='section_descriptions')

    def __str__(self):
        return f"{self.title} - {self.entreprise.name}"




