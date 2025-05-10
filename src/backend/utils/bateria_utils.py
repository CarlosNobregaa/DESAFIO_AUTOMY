from datetime import datetime

def separar_baterias(dados):
    hoje = datetime.today().date()  # Considerando apenas a data, sem hora
    futuras, passadas = [], []

    for item in dados:
        data_str = item["data_agendamento"]
        data_obj = datetime.strptime(data_str, "%d/%m/%Y").date()  # Convertendo para apenas data

        bateria = {
            "data": item["data_agendamento"],
            "horario": item["horario_agendamento"],
            "nome": item["nome"],
            "qtde_pessoas": item["qtde_pessoas"]
        }

        if data_obj >= hoje:
            futuras.append(bateria)
        else:
            passadas.append(bateria)

    return futuras, passadas

def montar_mensagem(email, futuras, passadas):
    return {
        "mensagem": f"Olá! Encontramos {len(futuras)} próximas baterias agendadas para {email}.",
        "baterias_futuras": futuras,
        "baterias_passadas": passadas
    }
