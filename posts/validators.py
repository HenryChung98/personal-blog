from django.core.exceptions import ValidationError

def validateSymbols(value):
    if ('&' in value):
        raise ValidationError('"&" cannot be included')