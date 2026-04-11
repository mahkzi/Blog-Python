from django import forms

class FormularioCreacionProducto(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        label="Nombre del producto"
        )
    precio = forms.DecimalField(
        label= "Precio",
        max_digits=10, 
        decimal_places=2,
    )
    descripcion = forms.CharField(
        label="Descripcion producto",
        widget=forms.Textarea
    )
class FormDeBusqueda(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        required=False,
    )