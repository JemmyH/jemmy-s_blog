from .forms import Login_form


def login_modal_form(request):
    return {'login_modal_form': Login_form()}
