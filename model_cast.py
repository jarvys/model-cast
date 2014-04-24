import sys

def cast(inst):
	from django.contrib.contenttypes.models import ContentType

	realType = ContentType.objects.get_for_model(type(inst))
	return realType.get_object_for_this_type(pk=inst.pk)


sys.modules[__name__] = cast

