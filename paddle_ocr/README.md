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
| 语言 | 代码 | 语言 | 代码 |
|------|------|------|------|
| 罗马尼亚语 | ro | 俄语 | ru |
| 萨摩亚语 | sm | 苏格兰盖尔语 | gd |
| 塞尔维亚语 | sr | 塞索托语 | st |
| 修纳语 | sn | 信德语 | sd |
| 僧伽罗语 | si | 斯洛伐克语 | sk |
| 斯洛文尼亚语 | sl | 索马里语 | so |
| 西班牙语 | es | 巽他语 | su |
| 斯瓦希里语 | sw | 瑞典语 | sv |
| 塔加路语（菲律宾语） | tl | 塔吉克语 | tg |
| 泰米尔语 | ta | 鞑靼语 | tt |
| 泰卢固语 | te | 泰文 | th |
| 土耳其语 | tr | 土库曼语 | tk |
| 乌克兰语 | uk | 乌尔都语 | ur |
| 维吾尔语 | ug | 乌兹别克语 | uz |
| 越南语 | vi | 威尔士语 | cy |
| 班图语 | xh | 意第绪语 | yi |
| 约鲁巴语 | yo | 祖鲁语 | zu |

