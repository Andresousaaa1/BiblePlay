from meu_app.models.usuario import Usuario


def Listar_Usuarios():
    return Usuario.objects.all()