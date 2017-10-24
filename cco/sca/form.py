from app.models import Sexo

class Setor(forms.Form):

    SETOR = (
        (1, "DIM"),
        (2, "DGC"),
    )
    setor = forms.ChoicerField(choices=SETOR, max_length=1)
