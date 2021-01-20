import datetime
import logging
import os, uuid
from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)

import os, uuid
import azure.functions as func
import base64


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    conn_str = "DefaultEndpointsProtocol=https;AccountName=yyyy;AccountKey=hhhh==;EndpointSuffix=core.windows.net"
    
    queue_name="outqueue1"    
    
    message = "EDNUpdateProcessRunning"

    queue_client = QueueClient.from_connection_string(conn_str, queue_name)

    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    
    queue_client.send_message(base64_message)

    if mytimer.past_due:
        logging.info('The timer is past due!')
    
           
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
