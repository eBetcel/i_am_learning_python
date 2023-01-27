#arquivo main.py
import base64

def backup_diario(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    if pubsub_message == 'START':
        print('Backup Iniciado')
        #
        # código para realizar backups
        #
    else:
        print('O backup não foi iniciado')