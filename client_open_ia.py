from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:8090/v1", api_key="ECNxrtp6fs2w627031990_2026")
r = client.chat.completions.create(
    model="qwent2.5-3b",
    messages=[{"role":"user","content":"Hola, ¿Quien eres?"}] )
print(r.choices[0].message.content)
