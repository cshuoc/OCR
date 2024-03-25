# 手寫識別

使用PaddleOCR和EasyOCR兩種高效光學字元辨識，來實現手寫辨識，也加入翻譯套件，來完整手寫翻譯功能。

## 項目列表

### EasyOCR

1. 優點：
 - 易於使用： EasyOCR設計用於快速且簡單的部署，即使對於沒有深度學習背景的用戶也很容易上手。
 - 多語言支持： 支持超過80種語言，涵蓋了大多數主要的世界語言。
 - 快速部署： EasyOCR提供了預訓練的模型，使得部署變得更加迅速和方便。
 - 輕量級： 相對於其他OCR工具，EasyOCR具有較小的模型大小和較低的運行成本。
2. 缺點：
 - 準確度： EasyOCR的準確度在某些場景下可能會較低，尤其是對於複雜字體或低質量圖像的處理能力較弱。
 - 功能限制： EasyOCR的功能相對較為基本，對於一些高級需求可能無法滿足。

### PaddleOCR

1. 優點：
 - 高性能： PaddleOCR基於PaddlePaddle深度學習框架，擁有強大的計算性能和良好的擴展性，能夠處理大規模圖像數據。
 - 準確度： PaddleOCR使用了先進的深度學習模型，因此在準確度上通常表現較好，尤其是對於複雜圖像的處理能力較強。
 - 多功能： PaddleOCR不僅支持文本檢測和識別，還提供了其他高級功能，如文本方向檢測、多語言支持等。
2. 缺點：
 - 複雜性： 對於初學者來說，PaddleOCR的使用可能相對複雜，需要一定程度的深度學習和計算機視覺知識。
 - 部署複雜： 相對於EasyOCR，PaddleOCR的部署和配置可能較為繁瑣，需要考慮到更多的技術細節和環境要求。
## 參考資料

本項目參考以下資料：

- [PyTorch 官方文檔](https://pytorch.org/docs/stable/index.html)：提供 PyTorch 的安裝步驟、API 文檔和教學。
- [OpenCV 官方文檔](https://docs.opencv.org/master/)：提供 OpenCV 的安裝指南、API 文檔和教學。
- [facenet-pytorch GitHub 倉庫](https://github.com/timesler/facenet-pytorch)：提供使用 PyTorch 實現 FaceNet 模型，用於人臉識別和驗證。
- [Googletrans：Google 翻譯 API](https://py-googletrans.readthedocs.io/en/latest/)：提供調用 Google 翻譯服務。
- [Anaconda 官方文檔](https://docs.anaconda.com/)：提供了 Anaconda 和 Miniconda 的安裝和管理教學。

## 致謝

感謝所有開源項目貢獻者的辛勤工作。
