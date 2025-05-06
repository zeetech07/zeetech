from django import template

register = template.Library()

@register.filter
def get(dictionary, key):
    """Yeh filter dictionary se key ki value return karega, warna empty list dega."""
    if dictionary is None:  # Agar dictionary None hai to empty dict set karo
        dictionary = {}
    return dictionary.get(key, [])  # Agar key nahi mili to empty list return karo

