# Hahow 課程頁更新文字

課程：用 Python 理財：打造自己的 AI 股票理專

以下三段可以直接貼到 Hahow 後台。`<REPO>` 代表 `https://github.com/finlab-python/hahow-ai-stock-course`，上線前請確認 repo 已公開。

---

## (a) 「老師的話」公告全文

**標題：【重要】課程教材全面更新：打開瀏覽器就能上課，不用再裝 Docker**

各位同學好：

這門課在 2018 年錄製，這幾年證交所網站改版、Python 套件大幅更新，舊的安裝方式與爬蟲已經無法使用，很多同學卡在環境架設，甚至無法開始上課。對此我們深感抱歉。

我們把全部教材重新改寫、逐一執行驗證過，今天起請改用新版教材：

**新版教材的三個改變**

1. **免安裝**：用 Google Colab 上課，打開瀏覽器就能執行，不需要 Docker、conda，也不需要高規格電腦。Windows、Mac（含 M 系列晶片）、Chromebook 都可以。
2. **免爬蟲建資料庫**：資料改由 FinLab 官方資料 API 提供，一行程式就能取得上市櫃股價、財報、月營收。註冊 FinLab 免費會員就能跑完整門課。
3. **每個單元都有對應的 notebook**：開頭會寫「對應影片」與「和影片的差異」，看影片時遇到舊寫法，對照 notebook 的新寫法即可。

**怎麼開始（約 1 分鐘）**

1. 打開教材首頁：<REPO>
2. 在「單元對照表」點選正在上的單元，notebook 會在 Google Colab 開啟。
3. 執行第一格，點出現的網址登入 FinLab（沒有帳號可免費註冊）。
4. 上方選單「執行階段 → 全部執行」。

**舊的安裝方式已停用**

- Docker 映像檔 `finlabcompany/finlab_ml_course`、conda 安裝步驟、`crawler.py`、`u0_environment_setup.pdf` 都已停用，不再維護。
- 影片中安裝 Docker、conda、執行爬蟲更新資料庫的段落可以直接跳過。
- 想在自己電腦執行，也只要 `pip install -r requirements.txt`，教材首頁有 Windows、Mac 的完整步驟。

**關於資料期間**

免費會員可以用到 2023 年底以前的所有資料，所有單元都能完整執行；付費會員的資料會更新到最新交易日。

使用新版教材遇到任何問題，請在課程問答區留言，並附上 notebook 名稱與錯誤訊息的截圖，我們會協助處理。

祝學習順利！

---

## (b) 各單元附件更換

**先刪除舊附件**：第 1 章單元 1～3 的
`新的安裝法請參考「老師的話」（此檔無用）.txt`、`crawler.py`、`u0_environment_setup.pdf`，
以及其他單元若掛有舊版 `u01`～`u25` notebook、Docker／conda 相關檔案，全部刪除。

**再上傳新附件**：附件上傳對應的 `.ipynb`（從 repo 的 `notebooks/` 下載）；單元說明欄貼上 Colab 連結，讓同學一鍵開啟。
Colab 連結格式：`https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/<檔名>`

| 章 | 單元 | 單元名稱 | 新附件（上傳 `notebooks/` 內的檔案） |
| --- | --- | --- | --- |
| 1 | 1 | 打造專屬 Python 實驗室 I | `ch1_u01_u02_setup.ipynb` |
| 1 | 2 | 打造專屬 Python 實驗室 II | `ch1_u01_u02_setup.ipynb`（取代 `crawler.py`） |
| 1 | 3 | 大盤 1 分 K 爬蟲練習 | `ch1_u03_taiex_kbar_crawler.ipynb` |
| 1 | 4 | 獨家上市櫃資料存儲 API 操作 Part 1 | `ch1_u04_u05_finlab_data_api.ipynb` |
| 1 | 5 | 獨家上市櫃資料存儲 API 操作 Part 2 | `ch1_u04_u05_finlab_data_api.ipynb` |
| 2 | 1 | 大盤歷史圖表分析 | `ch2_u01_taiex_analysis.ipynb` |
| 2 | 2 | 大盤參考哪條均線最有用 Part 1 | `ch2_u02_u03_moving_average.ipynb` |
| 2 | 3 | 大盤參考哪條均線最有用 Part 2 | `ch2_u02_u03_moving_average.ipynb` |
| 2 | 4 | K 線型態哪種最有用 | `ch2_u04_candlestick_patterns.ipynb` |
| 2 | 5 | K 線型態任意買賣點全股票回測 | `ch2_u05_candlestick_backtest.ipynb` |
| 2 | 6 | Pyfolio 分析報酬率曲線 | `ch2_u06_pyfolio_report.ipynb` |
| 2 | 7 | 常用財報指標 | `ch2_u07_financial_indicators.ipynb` |
| 2 | 8 | 常用技術指標 | `ch2_u08_technical_indicators.ipynb` |
| 3 | 3 | 實做 SVM 選股 Part 1 | `ch3_u03_u04_svm_stock_selection.ipynb` |
| 3 | 4 | 實做 SVM 選股 Part 2 | `ch3_u03_u04_svm_stock_selection.ipynb` |
| 3 | 6 | 實做 RF 選股 Part 1 | `ch3_u06_u07_random_forest_stock_selection.ipynb` |
| 3 | 7 | 實做 RF 選股 Part 2 | `ch3_u06_u07_random_forest_stock_selection.ipynb` |
| 3 | 8 | 比 RF 更好用的 Decision tree 模型們 | `ch3_u08_gradient_boosting.ipynb` |
| 3 | 9 | 技術指標機器學習策略 Part 1 | `ch3_u09_u10_technical_ml_strategy.ipynb` |
| 3 | 10 | 技術指標機器學習策略 Part 2 | `ch3_u09_u10_technical_ml_strategy.ipynb` |
| 3 | 11 | 作業：哪些財報數據重要 | `ch3_u11_homework_feature_importance.ipynb` |
| 4 | 2 | 實做 NN 大盤策略 | `ch4_u02_nn_taiex_strategy.ipynb` |
| 4 | 3 | NN 優化 Part 1 | `ch4_u03_u04_nn_optimization.ipynb` |
| 4 | 4 | NN 優化 Part 2 | `ch4_u03_u04_nn_optimization.ipynb` |
| 4 | 6 | 實做 LSTM 大盤買賣 Part 1 | `ch4_u06_u07_lstm_taiex.ipynb` |
| 4 | 7 | 實做 LSTM 大盤買賣 Part 2 | `ch4_u06_u07_lstm_taiex.ipynb` |
| 4 | 9 | 實做 CNN 買賣大盤 | `ch4_u09_cnn_taiex.ipynb` |
| 4 | 10 | 作業：Attention 神經網路 | `ch4_u10_homework_attention.ipynb` |
| 5 | 1 | 穩定擊敗大盤的 ML 選股策略實做 | `ch5_u01_ml_stock_strategy.ipynb` |
| 5 | 2 | 用 Python API 自動下單 Part 1 | `ch5_u02_u03_auto_trading.ipynb` |
| 5 | 3 | 用 Python API 自動下單 Part 2 | `ch5_u02_u03_auto_trading.ipynb` |
| 5 | 4 | 作業：策略優化 | `ch5_u04_homework_strategy_optimization.ipynb` |

觀念講解單元（第 3 章單元 1、2、5，第 4 章單元 1、5、8）沒有程式實作，不需要附件。

單元編號依課程頁的單元順序；若後台編號不同，以單元名稱對應。

**第 1 章單元 1、2 的單元說明建議加一句**：
> 影片中的 conda／Docker 安裝方式已停用，請直接用 Google Colab 開啟本單元的 notebook，步驟見「老師的話」。

---

## (c) 課程介紹頁「上課前的準備」改寫

**原文要點（需更新）**：需要 2023 年後的電腦、i7 處理器、32 GB 記憶體、不支援 M1、需要會 conda。

**建議改為：**

> ### 上課前的準備
>
> **設備**
> - 一台能上網、能開 Chrome 瀏覽器的電腦即可：Windows、Mac（含 M1／M2／M3 等 Apple 晶片）、Chromebook 都可以。
> - 課程使用免費的 Google Colab 執行程式，不需要在電腦上安裝任何軟體，也不需要高規格硬體或顯示卡。
> - 想在自己電腦執行也可以：需要 Python 3.11 或 3.12，建議 8 GB 以上記憶體，用 `pip` 一行指令安裝，不需要 Docker 或 conda。
>
> **帳號**
> - Google 帳號（使用 Colab）
> - FinLab 免費會員帳號（取得台股資料，上課時註冊即可）
>
> **先備知識**
> - 會 Python 基礎語法：變數、if、for 迴圈、函式。
> - 用過 pandas 會更輕鬆，但不是必要，課程中會邊做邊教。
> - 不需要事先學過機器學習或統計。
