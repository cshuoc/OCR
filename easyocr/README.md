# 文字識別系統

這個專案使用 EasyOCR 進行圖像中的文字識別，並支援使用 GPU 加速識別過程。它能夠讀取影像檔，識別圖像中的文字，並將識別結果保存到文字檔中。

## 環境要求

- Python 3.6+
- OpenCV
- EasyOCR
- NumPy

## 安裝

首先，確保您已經安裝了 Python 3.6 或更高版本。然後，您可以使用以下命令安裝所需的依賴：

```bash
pip install -r requirements.txt
```
## 執行
若要使用GPU來執行，請將 --use_gpu False 改為 True

```bash
python script_name.py --image_path "path/to/your/image.jpg" --recognized_text_path "path/to/save/text.txt" --pic_lang "['en', 'ch_tra']" --use_gpu False
```
