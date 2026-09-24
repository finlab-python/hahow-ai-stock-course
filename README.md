# 用 Python 理財：打造自己的 AI 股票理專｜課程教材（新版）

Hahow 課程「用 Python 理財：打造自己的 AI 股票理專」的配套 notebook。

新版教材**不需要安裝 Docker、conda，也不需要高規格電腦**：用瀏覽器打開 Google Colab 就能執行。
資料改由 FinLab 官方資料 API 提供，不必自己爬蟲建資料庫。

## 一分鐘開始

1. 在下方「單元對照表」點選要上的單元，會在 Google Colab 開啟 notebook（需要 Google 帳號）。
2. 執行第一格（點左邊的 ▶ 或按 `Shift + Enter`）。第一格會安裝套件並印出 FinLab 登入網址。
3. 點登入網址，用 FinLab 帳號登入（沒有帳號可以免費註冊），回到 Colab 看到「已登入」。
4. 上方選單「執行階段 → 全部執行」，跑完整本。

每本 notebook 開頭都有兩段說明：**對應影片**（這本對應哪個單元）與**和影片的差異**（影片裡的舊寫法換成了什麼）。邊看影片邊對照即可。

## 單元對照表

Colab 連結格式：`https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/<檔名>`

| 章 | 單元 | 單元名稱 | Notebook |
| --- | --- | --- | --- |
| 1 | 1、2 | 打造專屬 Python 實驗室 I、II | [ch1_u01_u02_setup.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch1_u01_u02_setup.ipynb) |
| 1 | 3 | 大盤 1 分 K 爬蟲練習 | [ch1_u03_taiex_kbar_crawler.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch1_u03_taiex_kbar_crawler.ipynb) |
| 1 | 4、5 | 獨家上市櫃資料存儲 API 操作 Part 1、2 | [ch1_u04_u05_finlab_data_api.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch1_u04_u05_finlab_data_api.ipynb) |
| 2 | 1 | 大盤歷史圖表分析 | [ch2_u01_taiex_analysis.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch2_u01_taiex_analysis.ipynb) |
| 2 | 2、3 | 大盤參考哪條均線最有用 Part 1、2 | [ch2_u02_u03_moving_average.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch2_u02_u03_moving_average.ipynb) |
| 2 | 4 | K 線型態哪種最有用 | [ch2_u04_candlestick_patterns.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch2_u04_candlestick_patterns.ipynb) |
| 2 | 5 | K 線型態任意買賣點全股票回測 | [ch2_u05_candlestick_backtest.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch2_u05_candlestick_backtest.ipynb) |
| 2 | 6 | Pyfolio 分析報酬率曲線 | [ch2_u06_pyfolio_report.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch2_u06_pyfolio_report.ipynb) |
| 2 | 7 | 常用財報指標 | [ch2_u07_financial_indicators.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch2_u07_financial_indicators.ipynb) |
| 2 | 8 | 常用技術指標 | [ch2_u08_technical_indicators.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch2_u08_technical_indicators.ipynb) |
| 3 | 1 | 什麼是 ML | 觀念影片，無 notebook |
| 3 | 2 | SVM | 觀念影片，實作在單元 3、4 |
| 3 | 3、4 | 實做 SVM 選股 Part 1、2 | [ch3_u03_u04_svm_stock_selection.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch3_u03_u04_svm_stock_selection.ipynb) |
| 3 | 5 | RF | 觀念影片，實作在單元 6、7 |
| 3 | 6、7 | 實做 RF 選股 Part 1、2 | [ch3_u06_u07_random_forest_stock_selection.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch3_u06_u07_random_forest_stock_selection.ipynb) |
| 3 | 8 | 比 RF 更好用的 Decision tree 模型們 | [ch3_u08_gradient_boosting.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch3_u08_gradient_boosting.ipynb) |
| 3 | 9、10 | 技術指標機器學習策略 Part 1、2 | [ch3_u09_u10_technical_ml_strategy.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch3_u09_u10_technical_ml_strategy.ipynb) |
| 3 | 11 | 作業：哪些財報數據重要 | [ch3_u11_homework_feature_importance.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch3_u11_homework_feature_importance.ipynb)（起始 notebook） |
| 4 | 1 | NN | 觀念影片，實作在單元 2 |
| 4 | 2 | 實做 NN 大盤策略 | [ch4_u02_nn_taiex_strategy.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch4_u02_nn_taiex_strategy.ipynb) |
| 4 | 3、4 | NN 優化 Part 1、2 | [ch4_u03_u04_nn_optimization.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch4_u03_u04_nn_optimization.ipynb) |
| 4 | 5 | RNN / LSTM | 觀念影片，實作在單元 6、7 |
| 4 | 6、7 | 實做 LSTM 大盤買賣 Part 1、2 | [ch4_u06_u07_lstm_taiex.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch4_u06_u07_lstm_taiex.ipynb) |
| 4 | 8 | CNN | 觀念影片，實作在單元 9 |
| 4 | 9 | 實做 CNN 買賣大盤 | [ch4_u09_cnn_taiex.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch4_u09_cnn_taiex.ipynb) |
| 4 | 10 | 作業：Attention 神經網路 | [ch4_u10_homework_attention.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch4_u10_homework_attention.ipynb)（起始 notebook） |
| 5 | 1 | 穩定擊敗大盤的 ML 選股策略實做 | [ch5_u01_ml_stock_strategy.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch5_u01_ml_stock_strategy.ipynb) |
| 5 | 2、3 | 用 Python API 自動下單 Part 1、2 | [ch5_u02_u03_auto_trading.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch5_u02_u03_auto_trading.ipynb) |
| 5 | 4 | 作業：策略優化 | [ch5_u04_homework_strategy_optimization.ipynb](https://colab.research.google.com/github/finlab-python/hahow-ai-stock-course/blob/main/notebooks/ch5_u04_homework_strategy_optimization.ipynb)（起始 notebook） |

「起始 notebook」從頭執行就能跑出基本結果，作業題目寫在 notebook 最後。

## 和影片不一樣的地方（總覽）

影片在 2018 年錄製，這幾年套件與資料來源都變了。新版教材的觀念、步驟與影片相同，寫法換成現在能用的版本：

| 影片 | 新版教材 |
| --- | --- |
| 用 conda / Docker 架環境 | Google Colab，或本機 `pip install -r requirements.txt` |
| `crawler.py` 爬蟲自建 pickle 資料庫、`from finlab.data import Data` | 官方 `finlab` 套件：`from finlab import data`、`data.get('price:收盤價')` |
| 大盤 1 分 K、15 分 K | 加權指數日 K（`taiex_total_index`）；1 分 K 保留在爬蟲練習單元 |
| 自己寫迴圈算報酬、手續費 | `finlab.backtest.sim()` 回測，自動計入手續費與交易稅 |
| `finlab.ml` 自製模組 | 官方 `finlab.ml.feature`、`finlab.ml.label` |
| 舊版 Keras、原版 pyfolio | Keras 3（Colab 內建）、`pyfolio-reloaded` |
| 直接呼叫券商 API 下單 | `finlab.online`（`Position`、`OrderExecutor`），教材只用模擬帳戶，不送真實委託 |

## 資料與會員方案

- **免費會員就能跑完整門課。** 免費會員的資料期間到 2018 年底（2018-12-28），剛好涵蓋影片錄製時的資料；付費會員的資料更新到最新交易日。
- notebook 裡保存的輸出（表格、圖表）是用**免費會員資料**執行的結果。付費會員執行時資料期間較長，數字會不同。
- 回測的「測試期間」都從 2016 年開始，所以兩種會員都能跑，只是測試期間的長度不同。
- 免費會員每天可下載 500 MB（付費會員 5000 MB），每天台北時間 08:00 重置。以免費會員資料估算，每本 notebook 約下載 150 MB 以內。

## 在自己的電腦執行

需要 Python 3.11 或 3.12（到 [python.org](https://www.python.org/downloads/) 下載）。

```bash
# 1. 下載教材（或在 GitHub 頁面按 Code → Download ZIP）
git clone https://github.com/finlab-python/hahow-ai-stock-course.git
cd hahow-ai-stock-course

# 2. 建立虛擬環境並安裝套件
python -m venv .venv
source .venv/bin/activate          # Windows 請改用：.venv\Scripts\activate
pip install -r requirements.txt

# 3. 開啟 Jupyter
jupyter lab
```

在 Jupyter 中打開 `notebooks/` 裡的檔案，一樣從第一格開始執行。第一次登入後，登入資訊與下載的資料會保存在電腦裡（資料在家目錄的 `finlab_db` 資料夾）。

## 常見問題

**Q：第一格的登入網址點了沒反應／一直等不到「已登入」？**
確認已經在打開的網頁上登入 FinLab。網址有效時間約 5 分鐘，逾時請重新執行第一格。
FinLab 帳號同時登入的裝置有上限，Colab 也算一台（重新連線會沿用同一個名額）。出現「已達裝置數量上限」時，到不用的那台電腦執行 `python -m finlab logout` 登出；超過 7 天沒用的裝置也會自動讓出名額。

**Q：出現「今日用量已達 80%」或額度用完？**
免費會員每天 500 MB，台北時間 08:00 重置；以免費會員資料估算，每本 notebook 約下載 150 MB 以內，一天可以跑兩三本。額度用完請隔天再跑，或升級付費會員（5000 MB／天）。

**Q：Colab 跑到一半斷線，變數都不見了？**
Colab 閒置一段時間會中斷連線。重新連線後，從第一格開始「執行階段 → 全部執行」即可。深度學習的單元（第 4 章）如果想跑快一點，可以把 `QUICK_RUN` 改成 `True`，只訓練幾個 epoch 確認程式能跑。

**Q：Colab 每次都要重新登入？**
是的。Colab 每次連線都是一台新的機器，登入資訊不會保留。在自己電腦執行只需登入一次。

**Q：Windows 可以在本機跑嗎？**
可以，**不需要 Docker**。照「在自己的電腦執行」操作即可：
- 安裝 Python 時勾選「Add python.exe to PATH」。
- 啟用虛擬環境的指令是 `.venv\Scripts\activate`（PowerShell 若出現權限錯誤，先執行 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`）。
- TA-Lib 0.6 版之後有 Windows 的安裝檔，`pip install` 會直接裝好，不需要另外下載 C 函式庫。
- TensorFlow 在 Windows 上使用 CPU 執行，本課程的模型都很小，CPU 就夠用。

**Q：舊版的 Docker 映像檔、conda 安裝方式、`crawler.py` 還能用嗎？**
已經停用，也不再維護。證交所網站改版後，舊爬蟲抓不到資料；Docker 映像檔裡的資料庫停在當年，而且需要大量記憶體。
請改用本教材：Colab 免安裝，資料由 FinLab 提供並持續更新。影片中安裝 Docker、conda、執行 `crawler.py` 的步驟都可以跳過。

**Q：圖表的標題為什麼是英文？**
Colab 預設沒有中文字型，matplotlib 的中文會變成方框。為了讓每個人打開都能正常顯示，圖表標題與座標軸一律用英文；表格裡的中文不受影響。

## 驗證方式（給維護者）

```bash
pip install -r requirements-dev.txt
python tests/check_notebooks.py --executed   # 格式、敏感資訊、輸出完整性
python tests/run_notebooks.py --quick        # 從頭執行全部 notebook（QUICK_RUN）
python tests/run_notebooks.py --inplace      # 完整執行並把輸出寫回 notebooks/
```

`.github/workflows/notebooks.yml` 每週一自動以 `QUICK_RUN` 執行全部 notebook，任何一本失敗就會標示失敗。
需要在 GitHub repo 設定 `FINLAB_REFRESH_TOKEN`、`FINLAB_SESSION_ID`、`FINLAB_API_KEY` 三個 secret（在自己電腦登入後執行 `python -m finlab token --env` 取得）。

## 免責聲明

本教材僅供教學使用，回測結果不代表未來績效，不構成任何投資建議。自動下單涉及真實資金，請自行評估風險。
