import os 
import cv2 
import argparse
from PIL import Image 
from googletrans import Translator
from matplotlib import pyplot as plt
from paddleocr import PaddleOCR,draw_ocr

def pic_to_txt(img_path : str,  result_save_path : str, pic_lang : str, target_lang : str, gpu:bool):
    ppocr = PaddleOCR(lang= pic_lang ,use_gpu=gpu, use_angle_cls = True)
    image = cv2.imread(img_path)
    image = cv2.resize(image, (image.shape[0]*2, image.shape[1]*2), interpolation=cv2.INTER_AREA)
    result = ppocr.ocr(image)
    print(result)
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='C:/Users/user/Desktop/shuo/id_card/TaipeiSansTCBeta-Regular.ttf')
    im_show = Image.fromarray(im_show)
    plt.imshow(im_show)                   
    plt.show()
    print(result)
    for res in result:
        # print(res[1][0])
        merge_result.append(res[1][0])
    # 將列表中的所有字符串合併成一個字串
    merge_result = ' '.join(merge_result)
    print(merge_result)
    #翻譯
    translator = Translator()
    result = translator.translate(merge_result, dest=target_lang, src = pic_lang)
    print(result.text)
    save_recognized_text(result, save_path)
def save_recognized_text(results, save_path='/your/path/test.txt'):
    with open(save_path, 'w', encoding='utf-8') as file:
        for (_, text, _) in results:
            file.write(text + '\n')
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='文字識別及翻譯')
    parser.add_argument('--image_path', type=str, default="/your/path/pic", help='欲辨識圖像路徑')
    parser.add_argument('--result_text_path', type=str, default='/your/path/text.txt', help='辨識結果儲存路徑')
    parser.add_argument('--pic_lang', type=str, default='en', help='欲辨識圖像文字類型')
    parser.add_argument('--target_lang', type=str, default='chinese_cht', help='欲辨識圖像文字類型')
    parser.add_argument('--gpu', type=bool, default=False, help='是否使用gpu')
    
    args = parser.parse_args()    
    
    pic_to_txt(args.img_path, args.result_text_path, args.pic_lang, args.target_lang, args.gpu)
