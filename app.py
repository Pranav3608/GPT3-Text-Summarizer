def lambda_handler(event=None, context=None):
  

  import os
  import openai
  import json

  OPENAI_API_KEY =''
  with open('OpenAI.json', 'r') as file_to_read:
    json_data = json.load(file_to_read)
    OPENAI_API_KEY = json_data["OPENAI_API_KEY"]
  
  openai.api_key = OPENAI_API_KEY

  
  import PyPDF2
  from PyPDF2 import PdfReader
  EOF_MARKER = b'%%EOF'
  doc = "apple_short.pdf"

  with open(doc, 'rb') as f:
    contents = f.read()
  

  if EOF_MARKER in contents:
    contents = contents.replace(EOF_MARKER, b'')
    contents = contents + EOF_MARKER
  else:
    print(contents[-8:])
    contents = contents[:-6] + EOF_MARKER

  with open(doc.replace('apple_short.pdf', '') + 'apple_short_fixed.pdf', 'rb') as f:
    f.write(contents)


  doc = PdfReader("apple_short.pdf")
  number_of_pages = len(doc.pages)
  page = doc.pages[0]
  text = page.extract_text()

  summary_list=[]
  prompt = text + "\n Tl;dr:"
  response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = prompt,
    temperature = 0.9,
    max_tokens = 256,
    top_p = 1,
    frequency_penalty = 0.0,
    presence_penalty = 1
  )
  summary_list.append(response["choices"][0]["text"])

  summary_text = ' '.join(summary_list)
  print(summary_text)