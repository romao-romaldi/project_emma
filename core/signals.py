from asgiref.sync import async_to_sync
from django.shortcuts import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contenu

@receiver(post_save,sender=Contenu)
def desactivate_contenu(sender, created, instance,*args, **kwargs):
    if created and instance.is_principal:
        (Contenu.objects.filter(entreprise=instance.entreprise, is_principal=True).exclude(id=instance.id)
         .update(is_principal=False))

# @receiver(post_save,sender=Notifications)
# def new_notification(sender, created, instance,*args, **kwargs):
#
#     if created:
#         channel_layer = get_channel_layer()
#         user =instance.user
#         group_name = f"notif-{user.pid}"
#
#         if instance.
#
#         event = {
#             "type": "user_joined",
#             "text": {
#                 "count_notification": Notifications.objects.filter(user=user, lu=False).count()
#                 "titre": instance.titre,
#                 "url":
#             }
#         }
#         async_to_sync(channel_layer.group_send)(group_name, event)