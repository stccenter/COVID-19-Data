from PIL import ImageFont, ImageDraw, Image
import os
import time
import cv2
import numpy as np

def addtext(analyze_date, image_path):
    print('------Add legend to image------')    
    path_list = os.listdir(image_path)
    path_list.sort()
    
    for img_name in path_list:
        if img_name[:10] not in analyze_date:
            continue
        bk_img = cv2.imread(image_path + img_name)
        
        img_pil = Image.fromarray(bk_img)
        draw = ImageDraw.Draw(img_pil)        
        
        font = ImageFont.truetype('arial.ttf', 18)
        # add legend text
        note_text = ['<=20', '100', '1,000', '10,000','50,000']
        draw.text((1100, 590), text=note_text[0], font=font, fill=(0, 0, 0))
        draw.text((1100, 567), text=note_text[1], font=font, fill=(0, 0, 0))
        draw.text((1100, 540), text=note_text[2], font=font, fill=(0, 0, 0))
        draw.text((1100, 500), text=note_text[3], font=font, fill=(0, 0, 0))
        draw.text((1100, 420), text=note_text[4], font=font, fill=(0, 0, 0))
        
        # add legend line
        draw.line(((1037, 598), (1095, 598)), fill='lightgray', width=1)#
        draw.line(((1037, 576), (1095, 576)), fill='lightgray', width=1)
        draw.line(((1037, 550), (1095, 550)), fill='lightgray', width=1)
        draw.line(((1052, 510), (1095, 510)), fill='lightgray', width=1)
        draw.line(((1080, 430), (1095, 430)), fill='lightgray', width=1)
        bk_img = np.array(img_pil)
        
        cv2.waitKey()
        cv2.imwrite(image_path + img_name, bk_img)

def png2gif(image_path, selected_date, gifname, duration):
    print('------Convert png to gif------')
    file_list = os.listdir(image_path)
    file_list.sort()
    frames = [] # buffer zone
    
    # PIL method
    imN = 1
    for filename in file_list:
        if imN == 1:  
            im = Image.open(image_path + filename)
            imN = 2
        if filename[:10] in selected_date:
            frames.append(Image.open(image_path + filename))
    im.save(gifname, save_all=True, append_images=frames, loop=1, duration=duration)
    