from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from gpt.settings import CHATGPT_APIKEY

import openai
openai.api_key = CHATGPT_APIKEY

class Chatgpt(generics.GenericAPIView):
    
    def post(self, request, *args,**kwargs):

        text = request.data.get('text')
        print(text)

        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user", 
                    "content": f"{text}",
                }
            ]
        )

        response = res.choices[0].message["content"]
        print(res.choices)


        return Response({"success":"True" , "response": response} , status=status.HTTP_200_OK)