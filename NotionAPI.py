import os #installs all the libraries we need as pre-settings
os.system('pip install --upgrade pip')
os.system('pip3 install requests')
os.system('pip3 install lzstring')

import requests
import lzstring
import json

def create_txt(A):
  result = ''.join(A)

  
  x = lzstring.LZString()
  compressed = x.compressToBase64(json.dumps({
  "files": {
    "main.py": {
      "content": result,
      "isBinary": False
    },
    "package.json": {
      "content": {
        "dependencies": {}
      }
    }
  }
}))
  print("\t", compressed)
  r = requests.get(f'https://codesandbox.io/api/v1/sandboxes/define?parameters={compressed}')

  return r.text

#print(create_txt(["georgi", "steven", "viktor",'vicki']).text)


#print(create_txt(['### test task 4\nif a != 0:\n\tprint("a is not zero")\nelse:\n\treturn("a is zero")', "### test task 8\n\ndef function(a,b,c):\n\tif a is not int:\n\t\tprint('error')\n\telse b > 5:\n\t\tprint('b is greater than 5')\n\telse c = 10:\n\t\tprint('c is equal to 10')\n\nfunction(10,5,3)"]))
print(create_txt(['georgi', 'viktor']))
