from django.core.exceptions import PermissionDenied
from account.models import Employee, Employer

def user_is_employer(function):

    def wrap(request, *args, **kwargs):   

        if request.user.employer:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap



def user_is_employee(function):

    def wrap(request, *args, **kwargs):    

        if request.user.employee:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap