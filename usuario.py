usuarios = {
    "ana": {
        "senha":"123",
        "permissao": "produtos",
    },
    "carlos":{
            "senha": "456",
            "permissao": "relatorios"
    }
}
def autenticar(login,senha):
    if login in usuarios:

        if usuarios[login]["senha"] == senha:
            return {
                "login": login,
                "permissao": usuarios[login]["permissao"]
                   
            }
    return None
