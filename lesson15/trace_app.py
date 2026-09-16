from openai import OpenAI

from openinference.instrumentation.openai import OpenAIInstrumentor

from phoenix.otel import register

tracer_provider = register(endpoint="http://localhost:6006/v1/traces")

OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)

client = OpenAI(

    base_url="http://localhost:11434/v1",

    api_key="ollama" 

)

 

response = client.chat.completions.create(

    model="phi3",

    messages=[{"role": "user", "content": "How much does a junior qa automation engineer make a month?"}],

    temperature = 0

)

print(response.choices[0].message.content)