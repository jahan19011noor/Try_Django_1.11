from django.core.exceptions import ValidationError

CATEGORIES =['Sylheti', 'Dhakai', 'Bangladeshi', 'Thai']

def validate_email(value):
    if ".edu" in value:
        raise ValidationError(
            'we do not except emails like %(value)',
            params={'value': value},
        )

def validate_caterogy(value):
    cat = value.capitalize()
    if value not in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(
            '{0} is not a valid category'.format(value)
        )