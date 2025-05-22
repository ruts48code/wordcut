from pythainlp.tokenize import word_tokenize
from bottle import Bottle, request, run
from truckpad.bottle.cors import CorsPlugin, enable_cors

app = Bottle()

def tk(data):
  return  word_tokenize(data, engine="newmm")

def lenx(data):
  count = 0
  for i in data:
    match i:
      case '่'|'้'|'๊'|'๋'|'ิ'|'ี'|'ึ'|'ื'|'ั'|'ุ'|'ู'|'์'|'็':
        pass
      case _:
        count = count + 1
  return count

@enable_cors
@app.post("/wordcut")
def wordcut():
  output = {}
  data = request.json
  output["output"] = tk(data['data'])
  return output

@enable_cors
@app.post("/wordx")
def wordx():
  output = {}
  data = request.json
  wc = tk(data['data'])
  wb = []
  w1 = ""
  for i in wc:
    if lenx(w1)+lenx(i) > data['size']:
      wb.append(w1)
      w1 = i
      continue
    w1 = w1+i
  if w1!="":
    wb.append(w1)
  output['output'] = wb
  return output

if __name__=='__main__':
  app.install(CorsPlugin(origins=['*']))
  app.run(host='0.0.0.0', port=9887)
