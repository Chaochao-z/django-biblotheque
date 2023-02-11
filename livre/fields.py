from django.forms import ModelChoiceField


class LivreModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()
