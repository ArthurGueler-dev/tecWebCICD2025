import json

def lambda_handler(event, context):
    """
    Função Lambda padrão em Python.
    
    :param event: Dados de entrada (payload do evento que acionou a Lambda).
    :param context: Informações de execução (tempo restante, ARN, etc).
    :return: Resposta em formato JSON.
    """
    
    # Exemplo: logar o evento recebido
    print("Evento recebido:", json.dumps(event))
    
    # Exemplo: acessar uma informação do contexto
    print(f"Função ARN: {context.invoked_function_arn}")
    print(f"Tempo restante (ms): {context.get_remaining_time_in_millis()}")

    # Retorno
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Lambda executada com sucesso!",
            "input": event
        })
    }
    
    return response
