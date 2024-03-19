import cv2
import easyocr
import numpy as np

def read_text_from_image(image_path, pic_lang : list):
    reader = easyocr.Reader(pic_lang)   # 初始化 easyocr 讀取器，假設文本包含英文和繁體中文
    image = cv2.imread(image_path)
    image = cv2.resize(image, None, fx=0.1, fy=0.1)
    results = reader.readtext(image, detail=1)  # detail=1 返回詳細資訊，包括邊界框
    return results

def draw_text_boxes(image_path, results):
    image = cv2.imread(image_path)
    image = cv2.resize(image, None, fx=0.1, fy=0.1)
    for (bbox, text, prob) in results:
        # 獲取邊界框的座標
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = (int(top_left[0]), int(top_left[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

        # 繪製邊界框和文本
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    return image

def save_recognized_text(results, save_path='/your/path/test.txt'):
    with open(save_path, 'w', encoding='utf-8') as file:
        for (_, text, _) in results:
            file.write(text + '\n')

# 執行
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='文字識別系統')
    parser.add_argument('--image_path', type=str, default="/your/path/pic", help='欲辨識圖像路徑')
    parser.add_argument('--recognized_text_path', type=str, default='/your/path/text.txt', help='辨識結果儲存路徑')
    parser.add_argument('--pic_lang', type=list, default=['en', 'ch_tra'], help='欲辨識圖像文字類型')
    
    args = parser.parse_args()
    
    recognized_text = read_text_from_image(args.image_path, args.pic_lang)
    image_with_boxes = draw_text_boxes(args.image_path, recognized_text)
    cv2.imshow("Image with Text Boxes", image_with_boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save_recognized_text(args.recognized_text_path)
    print("Text recognition complete. Results saved to 'your/path/text.txt.")
