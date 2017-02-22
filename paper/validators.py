from django.forms import ValidationError

def validate_paper_file(paper_file):
    """
    This is a validator that validates if the extension is .pdf,
    Raises a validation error in the extension is not .pdf
    :param paper_file: The paper file field instance of the model
    :return: None
    """
    if not paper_file.name.endswith('.pdf'):
        raise ValidationError('The file is not a pdf')