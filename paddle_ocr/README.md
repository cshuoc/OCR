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
| 語言 | 代碼 | 語言 | 代碼 | 語言 | 代碼 |
|------|------|------|------|------|------|
| 羅馬尼亞語 | ro | 俄語 | ru | 塔加路語（菲律賓語） | tl | 塔吉克語 | tg |
| 薩摩亞語 | sm | 蘇格蘭蓋爾語 | gd | 泰米爾語 | ta | 韃靼語 | tt |
| 塞爾維亞語 | sr | 塞索托語 | st | 泰盧固語 | te | 泰文 | th |
| 修納語 | sn | 信德語 | sd | 土耳其語 | tr | 土庫曼語 | tk |
| 僧伽羅語 | si | 斯洛伐克語 | sk | 烏克蘭語 | uk | 烏爾都語 | ur |
| 斯洛維尼亞語 | sl | 索馬里語 | so | 維吾爾語 | ug | 烏茲別克語 | uz |
| 西班牙語 | es | 巽他語 | su | 越南語 | vi | 威爾士語 | cy |
| 斯瓦希裡語 | sw | 瑞典語 | sv | 班圖語 | xh | 意第緒語 | yi |
| 約魯巴語 | yo | 祖魯語 | zu



