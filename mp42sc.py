import cv2
import os
import json
import re
from PIL import Image
import jt
inputfile = input("Имя файла: ")
vidcap = cv2.VideoCapture(inputfile)
success,image = vidcap.read()
fps = int(vidcap.get(cv2.CAP_PROP_FPS))
print(f"FPS: {fps}")
count = 0
if os.path.isdir("frames\\"):
  if os.listdir("frames\\") == []:
    pass
  else:
    for f in os.listdir("frames\\"):
      os.remove(os.path.join("frames\\", f))
else:
  os.mkdir("frames\\")
while success:
  cv2.imwrite("frames\\%d.png" % count, image)
  success,image = vidcap.read()
  #print('Save a new frame: frame%d' % count, success)
  count += 1
print("All frames were successfully saved to 'frames' folder!")
lst = []
for f in os.listdir("frames\\"):
  lst.append("frames\\"+ f)
def num_sort(test_string):
  return list(map(int, re.findall(r'\d+', test_string)))[0]
lst.sort(key=num_sort)
print(lst)
images = [Image.open(x) for x in lst]
widths, heights = zip(*(i.size for i in images))
total_width = sum(widths)
max_height = max(heights)
new_img = Image.new('RGB', (total_width, max_height))
x_offset = 0
for im in images:
  new_img.paste(im, (x_offset,0))
  x_offset += im.size[0]
new_img.save('test.png', optimize=True,quality=90)
files_number = len(os.listdir("frames\\"))
print(files_number)
def write_json(new_data,arrayf,filename='111.json'):
  with open(filename,'r+') as file:
    file_data = json.load(file)
    file_data[arrayf].append(new_data)
    file.seek(0)
    json.dump(file_data,file,indent=4)
def write_json0(new_data,arrayf,arrayg,arrayb,filename='111.json'):
  with open(filename,'r+') as file:
    file_data = json.load(file)
    file_data[arrayf][arrayg][arrayb].append(new_data)
    file.seek(0)
    json.dump(file_data,file,indent=4)
def write_json3(arrayf,filename='111.json'):
  with open(filename,'r+') as file:
    file_data = json.load(file)
    if arrayf == "width":
      file_data["textures"][0][arrayf] = total_width
    else:
      file_data["textures"][0][arrayf] = max_height
    file.seek(0)
    json.dump(file_data,file,indent=4)
def write_json1(new_data,arrayf,arrayg,arrayb,arrayc,filename='111.json'):
  with open(filename,'r+') as file:
    file_data = json.load(file)
    file_data[arrayf][arrayg][arrayb][arrayc].append(new_data)
    file.seek(0)
    json.dump(file_data,file,indent=4)
jt.movieClip["frameRate"] = fps
write_json(jt.movieClip, "movieClips")
write_json(jt.blahblah, "movieClips")
write_json(jt.blahblah1, "movieClips")
write_json3("width")
write_json3("height")
for i in range(0, files_number + 1):
  jt.bitmapsJson['id'] = i
  jt.transformsJson["transforms"][0]["bindIndex"] = i
  jt.bind['bindId'] = i
  jt.movieClip["binds"] = jt.bind
  write_json0(jt.movieClip["binds"],"movieClips",0,"binds")
  write_json1(jt.transformsJson,"movieClips",0,"data","frames")
  print(i)
  jt.bitmapsJson["bitmaps"][0]["points"][0]["twip"][0] = 0
  jt.bitmapsJson["bitmaps"][0]["points"][0]["twip"][1] = int(-(widths[0] + heights[0] * 1.5))
  jt.bitmapsJson["bitmaps"][0]["points"][1]["twip"][0] = int(widths[0] + heights[0] * 1.5)
  jt.bitmapsJson["bitmaps"][0]["points"][1]["twip"][1] = int(-(widths[0] + heights[0] * 1.5))
  jt.bitmapsJson["bitmaps"][0]["points"][2]["twip"][0] = int(widths[0] + heights[0] * 1.5)
  jt.bitmapsJson["bitmaps"][0]["points"][2]["twip"][1] = 1
  jt.bitmapsJson["bitmaps"][0]["points"][3]["twip"][0] = 0
  jt.bitmapsJson["bitmaps"][0]["points"][3]["twip"][1] = 1
  if jt.bitmapsJson["id"] == 0:
    jt.bitmapsJson["bitmaps"][i - 1]["points"][0]["uv"][0] = 0
    jt.bitmapsJson["bitmaps"][i - 1]["points"][0]["uv"][1] = 0
    jt.bitmapsJson["bitmaps"][i - 1]["points"][1]["uv"][0] = widths[0]
    jt.bitmapsJson["bitmaps"][i - 1]["points"][1]["uv"][1] = 0
    jt.bitmapsJson["bitmaps"][i - 1]["points"][2]["uv"][0] = widths[0]
    jt.bitmapsJson["bitmaps"][i - 1]["points"][2]["uv"][1] = heights[0]
    jt.bitmapsJson["bitmaps"][i - 1]["points"][3]["uv"][0] = 0
    jt.bitmapsJson["bitmaps"][i - 1]["points"][3]["uv"][1] = heights[0]
  elif jt.bitmapsJson["id"] == 1:
    jt.bitmapsJson["bitmaps"][0]["points"][0]["uv"][0] = widths[0] * (i)
    jt.bitmapsJson["bitmaps"][0]["points"][0]["uv"][1] = 0
    jt.bitmapsJson["bitmaps"][0]["points"][1]["uv"][0] = widths[0] * (i + 1)
    jt.bitmapsJson["bitmaps"][0]["points"][1]["uv"][1] = 0
    jt.bitmapsJson["bitmaps"][0]["points"][2]["uv"][0] = widths[0] * (i + 1)
    jt.bitmapsJson["bitmaps"][0]["points"][2]["uv"][1] = heights[0]
    jt.bitmapsJson["bitmaps"][0]["points"][3]["uv"][0] = widths[0] * (i)
    jt.bitmapsJson["bitmaps"][0]["points"][3]["uv"][1] = heights[0]
  else:
    jt.bitmapsJson["bitmaps"][0]["points"][0]["uv"][0] = widths[0] * (i - 2)
    jt.bitmapsJson["bitmaps"][0]["points"][0]["uv"][1] = heights[0] * (i - 2)
    jt.bitmapsJson["bitmaps"][0]["points"][1]["uv"][0] = heights[0] * (i - 2)
    jt.bitmapsJson["bitmaps"][0]["points"][1]["uv"][1] = widths[0] * (i - 1)
    jt.bitmapsJson["bitmaps"][0]["points"][2]["uv"][0] = widths[0] * (i - 1)
    jt.bitmapsJson["bitmaps"][0]["points"][2]["uv"][1] = heights[0] * (i - 1)
    jt.bitmapsJson["bitmaps"][0]["points"][3]["uv"][0] = heights[0] * (i - 1)
    jt.bitmapsJson["bitmaps"][0]["points"][3]["uv"][1] = widths[0] * (i - 2)
    jt.bitmapsJson["bitmaps"][0]["points"][0]["uv"][0] = widths[0] * (i)
    jt.bitmapsJson["bitmaps"][0]["points"][0]["uv"][1] = 0
    jt.bitmapsJson["bitmaps"][0]["points"][1]["uv"][0] = widths[0] * (i + 1)
    jt.bitmapsJson["bitmaps"][0]["points"][1]["uv"][1] = 0
    jt.bitmapsJson["bitmaps"][0]["points"][2]["uv"][0] = widths[0] * (i + 1)
    jt.bitmapsJson["bitmaps"][0]["points"][2]["uv"][1] = heights[0]
    jt.bitmapsJson["bitmaps"][0]["points"][3]["uv"][0] = widths[0] * (i)
    jt.bitmapsJson["bitmaps"][0]["points"][3]["uv"][1] = heights[0]
  write_json(jt.bitmapsJson,"shapes")