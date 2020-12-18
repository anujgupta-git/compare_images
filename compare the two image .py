#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image,ImageChops
img1=Image.open('desktop/anujp1.png')
img2=Image.open('desktop/anujphoto.jpg')
diff=ImageChops.difference(img1,img2)
if diff.getbbox():
    diff.show()

