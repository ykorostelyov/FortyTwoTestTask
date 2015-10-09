from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import get_model
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User


ADDITION = 1
CHANGE = 2
DELETION = 3


@receiver(post_save)
def model_create_or_update(sender, created,  **kwargs):
    try:
        class_name = sender.__name__
        if str(class_name) not in("Mycard", "RequestInfo"):
            return
        action = ADDITION if created else CHANGE

        curr_model = get_model("hello",
                               class_name,
                               seed_cache=False,
                               only_installed=False)

        change_message = 'created object' if created else 'changed some ' \
                                                          'field'
        curr_user = User.objects.filter(username='anonymous').first().id

        LogEntry.objects.create(
            user_id=curr_user,
            content_type_id=ContentType.objects.get_for_model(
                curr_model).pk,
            object_id=1,
            object_repr=force_unicode(class_name) + ' object',
            action_flag=action,
            change_message=change_message)
    except:
        print "err change signal: " + str(sender)


@receiver(post_delete)
def model_delete(sender, **kwargs):
    try:
        class_name = sender.__name__
        if str(class_name) not in("Mycard", "RequestInfo"):
            return
        action = DELETION
        curr_model = get_model("hello",
                               class_name,
                               seed_cache=False,
                               only_installed=False)

        curr_user = User.objects.filter(username='anonymous').first().id
        LogEntry.objects.create(
            user_id=curr_user,
            content_type_id=ContentType.objects.get_for_model(
                curr_model).pk,
            object_id=1,
            object_repr=force_unicode(class_name) + ' object',
            action_flag=action,
            change_message='deleting object')
    except:
        print "err del signal: " + str(sender)
