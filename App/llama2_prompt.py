from openai import OpenAI

def call_llama(event, gender):
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
    
    completion = client.chat.completions.create(
      model="local-model", # this field is currently unused
      messages=[
        {"role": "system", "content": "Below is an instruction that describes a task. Write a response that appropriately completes the request."},
        {"role": "user", "content": f'Suggest some attires for {event} for {gender}. For each apparel in the outfit give its color. Each outfit on a new line. Suggest less than 5 outfits. Do not use special characters like "-" and "#" in the response generated by you. Response:less Ten words reply for each outfit:' }
      ],
      temperature=0.5
    )

    return list(completion.choices[0].message)[0][1]


def clean_tokens(response):
    
    response = response.split('.')
    response = [item.split(" - ") for item in response]
    response = [item for sublist in response for item in sublist]
    
    response = [txt for txt in response if len(txt) > 28]

    for indx, apparel in enumerate(response):
        apparel = apparel.replace("with",",").replace("and",",").replace(" ' ","")
        apparel = apparel.split(',')
        apparel = [txt.strip() for txt in apparel]
    
        response[indx] = apparel

    return response