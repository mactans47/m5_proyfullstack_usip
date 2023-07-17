from django.core.exceptions import ValidationError

def validation_isbn(value):
    if len(value) !=13:
        raise ValidationError(
            "Valor de ISBN no válido"
        )