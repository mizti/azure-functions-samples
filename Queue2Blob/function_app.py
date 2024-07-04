import azure.functions as func
import datetime
import json
import logging
from datetime import datetime

now = datetime.now()
formatted_time = now.strftime('%Y%m%d%H%M%S')
filename = "mycontainer/test" + formatted_time + ".txt"

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="ksqueue0701", connection="AzureWebJobsStorage")
@app.blob_output(arg_name="$return",
                path=filename,
                connection="AzureWebJobsStorage")
def MyQueueTrigger(azqueue: func.QueueMessage) -> str:
    inputblob = azqueue.get_body().decode('utf-8')
    logging.info('Python Queue trigger processed a message: %s',inputblob)
    return inputblob