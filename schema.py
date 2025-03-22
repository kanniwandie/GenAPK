from pydantic import BaseModel
from openai import OpenAI
class Country(BaseModel):
  name: str
  capital: str
  languages: list[str]



class File(BaseModel):
    relative_path: str
    content: str



class Project(BaseModel):
    name: str
    comments: str
    files: list[File]



# client = OpenAI(
#     api_key="AIzaSyB4SxHdIlJtX9arqwS2xMVFk2InXiGcIGY",
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )


# completion = client.beta.chat.completions.parse(
#     model="gemini-2.0-flash",
#     messages=[
#         {"role": "system", "content": "Get the details of the country"},
#         {"role": "user", "content": "Tell me more about Singapore."},
#     ],
#     response_format=Country,
# )

# country = completion.choices[0].message.parsed
# if country:
#     print(country.capital)
