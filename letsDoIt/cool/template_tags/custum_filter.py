from django import template

user_id = template.Library()

@user_id.filter
def reverse_age(value):
       return value[::-1]
                    
                    
@user_id.filter
def nameStarted(value, startswith):
    return [value.startswith]
