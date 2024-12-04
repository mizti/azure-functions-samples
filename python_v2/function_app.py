import azure.functions as func
import logging

app = func.FunctionApp()

@app.function_name(name="myFunction1")
@app.route(route="myFunction1", auth_level=func.AuthLevel.ANONYMOUS)
def myFunction1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get('name')
        except ValueError:
            pass

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body.",
            status_code=400
        )

