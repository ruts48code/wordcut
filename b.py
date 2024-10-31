from pythainlp.tokenize import word_tokenize
import asyncio
import json
import tornado

def tk(data):
  return  word_tokenize(data, engine="newmm")

def lenx(data):
  count = 0
  for i in data:
    match i:
      case '่'|'้'|'๊'|'๋'|'ิ'|'ี'|'ึ'|'ื'|'ั'|'ุ'|'ู':
        pass
      case _:
        count = count + 1
  return count

class Cors(tornado.web.RequestHandler):
  def set_default_headers(self):
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Headers", "Content-Type")
    self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
  def options(self):
    self.set_status(204)
    self.finish()

class WordCut(Cors):
  def post(self):
    self.set_header("Content-Type", "application/json")
    output = {}
    data = json.loads(self.request.body.decode('utf-8'))
    output["output"] = tk(data['data'])
    self.write(json.dumps(output))
  
class Wordx(Cors):
  def post(self):
    self.set_header("Content-Type", "application/json")
    output = {}
    data = json.loads(self.request.body.decode('utf-8'))
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
    self.write(json.dumps(output))

async def main():
  app = tornado.web.Application([
    (r"/wordcut", WordCut),
    (r"/wordx", Wordx),
  ])
  app.listen(9887)
  await asyncio.Event().wait()

if __name__=="__main__":
  asyncio.run(main())

