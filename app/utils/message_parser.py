from langchain.output_parsers import ResponseSchema, StructuredOutputParser

#Define schemas for format instructions and Output parser
task_schema = ResponseSchema(name="task",
                             description="The task you are asked to do it could be create, update or delete\
                                answser create, update or delete")
product_name_schema = ResponseSchema(name="product_name",
                                      description="the name of the product to create, update or delete")
price_schema = ResponseSchema(name="price",
                                    description="extract any value related to the product price only if the task is create or update")
description_schema = ResponseSchema(name="description",
                                    description="Extract any information related to the product description only if the task is create or update")
stock_schema = ResponseSchema(name="stock",
                              description="Extract any value related to the stock amount only if the task is create or update")

response_schemas = [
    task_schema,
    product_name_schema,
    price_schema,
    description_schema,
    stock_schema
]

#set output parser
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

def message_parser(message:str) -> dict:
    output = output_parser.parse(message)
    return output