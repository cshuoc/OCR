# 文字識別及翻譯工具

這個專案使用 PaddleOCR 進行圖像中的文字識別，並使用 Google Translate 進行翻譯。它能夠讀取影像檔，識別圖像中的文字，並將識別出的文字翻譯成指定的語言。

## 環境要求

- Python 3.6+
- PaddleOCR
- OpenCV
- PIL
- Matplotlib
- Googletrans

## 安裝

首先，確保您已經安裝了 Python 3.6 或更高版本。然後，您可以使用以下命令安裝所需的依賴：

```bash
pip install -r requirements.txt
```

## 執行

```bash
python ppocr.py --image_path "path/to/your/image.jpg" --result_text_path "path/to/save/text.txt" --pic_lang "en" --target_lang "zh-cn"
```

### Google Translate 語言種類代號
可以參考 [官網](<[http://example.com/Hello World.html](https://support.google.com/googleplay/android-developer/table/4419860?hl=zh-Hant)> "Title") 知道更多語言代碼。
| 語言 | 代碼 | 語言 | 代碼 | 語言 | 代碼 |
|------|------|------|------|------|------|
| 南非荷蘭語 | af | 阿爾巴尼亞語 | sq | 阿姆哈拉語 | am |
| 阿拉伯語 | ar | 亞美尼亞語 | hy | 亞塞拜然語 | az |
| 巴斯克語 | eu | 白俄羅斯語 | be | 孟加拉語 | bn |
| 波士尼亞語 | bs | 保加利亞語 | bg | 加泰羅尼亞語 | ca |
| 宿務語 | ceb(ISO-639-2) | 中文（簡體） | zh-CN或zh(BCP-47) | 中文（繁體） | zh-TW(BCP-47) |
| 科西嘉語 | co | 克羅埃西亞語 | hr | 捷克語 | cs |
| 丹麥語 | da | 荷蘭語 | nl | 英語 | en |
| 世界語 | eo | 愛沙尼亞語 | et | 芬蘭語 | fi |
| 法語 | fr | 弗裡斯蘭語 | fy | 加利西亞語 | gl |
| 格魯吉亞語 | ka | 德語 | de | 希臘語 | el |




