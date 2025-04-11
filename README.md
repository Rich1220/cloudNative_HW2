# CloudShop CLI Marketplace 

## Overview

cloudShop 是一個命令列應用程式，使用Ｐython撰寫與執行，用來模擬線上市集。使用者可以註冊帳號、發布商品、查詢商品與熱門分類等操作。



## 🐍 Python Environment

本專案開發時使用 **Python 3.9.6**，所有功能均使用 Python 標準函式庫。  
助教可直接使用 `python3` 或 `python` 執行主程式，不需虛擬環境。

> ⚠ 若系統預設 Python 版本過舊（低於 3.8），建議使用 Python 虛擬環境（venv）或安裝新版 Python（建議 3.9+）以執行本專案。



## 🧱 Project Structure

```plaintext
cloudShop/
├── cli.py            # 主程式入口，處理指令輸入與輸出
├── marketplace.py    # 處理商場邏輯，如註冊、listing 操作等
├── database.py       # 管理資料儲存與資料結構
├── build.sh          # 確認python
├── run.sh            # 啟動 CLI 應用程式

Ｎote:
🧩 Presentation Layer（呈現層／CLI） ➜ cli.py
🧠 Business Logic Layer（商業邏輯層） ➜ marketplace.py
🗃️ Persistence Layer（資料層） ➜ database.py
```



## 🚀 How to Build and Run

## ▶️ macOS / Linux 使用者：

```bash
# 進入到 cloudShop 目錄
chmod +x build.sh run.sh         # 第一次執行需賦予執行權限
./build.sh                       # 建置環境
./run.sh                         # 執行 CLI 主程式
```

### ▶️ Windows 使用者：

請使用 Git Bash / WSL 或者執行：

```bash
# 進入到 cloudshop 目錄
bash build.sh
bash run.sh
```

或直接使用 Python：

```bash
python cli.py
```





## 📦 Data Structure Overview

```plaintext
Data
├── Users (dict)
│   └── username_lowercase : User object
│
├── Listings (dict)
│   └── listing_id : Listing object
│
└── Categories (dict)
    └── category_name : List of Listing objects
```



## 🔧 System Overview（三層系統）

```plaintext
 [使用者 CLI 輸入]
        ↓
     cli.py
    （指令解析）
        ↓
  marketplace.py
 （邏輯判斷與錯誤處理）
        ↓
    database.py
  （儲存資料與查詢）
```



## 💡 Features Implemented and Command Details

## 1. 🧩 呈現層 - `cli.py`

- 讀取使用者輸入（例如：`REGISTER user1`）
- 使用 `shlex.split()` 解析輸入字串
- 根據指令呼叫 `Marketplace` 對應方法
- 顯示結果

### 支援指令（命令格式）：

- `REGISTER <username>`
- `CREATE_LISTING <username> <title> <description> <price> <category>`
- `DELETE_LISTING <username> <listing_id>`
- `GET_LISTING <username> <listing_id>`
- `GET_CATEGORY <username> <category>`
- `GET_TOP_CATEGORY <username>`
- `EXIT`



## 2. 🧠 商業邏輯層 - `marketplace.py`

- 接收 CLI 呼叫的指令與參數
- 驗證使用者、商品、分類等是否有效
- 決定是否回傳錯誤，或呼叫資料層
- 負責主要邏輯流程控制

### 支援功能（方法）：

- `register_user(username)`：使用者註冊
- `create_listing(username, title, description, price, category)` ：創建商品
- `delete_listing(username, listing_id)` ：刪除商品(需本人)
- `get_listing(username, listing_id)`：使用ID查詢商品
- `get_category(username, category)`：使用類別查詢商品
- `get_top_category(username)`：找最熱門商品



## 3. 🗃️ 資料層 - `database.py`

- 實際儲存所有使用者、商品、分類資料
- 使用 set / dict 作為資料結構（記憶體內模擬 DB）
- 負責新增 / 查詢 / 刪除資料

### 支援功能（方法）：

- `add_user(username)`：新增使用者
- `user_exists(username)`：檢查使用者是否存在
- `add_listing(username, title, description, price, category)`：新增 listing
- `listing_exists(listing_id)`：檢查 listing 是否存在
- `is_listing_owerner(listing_id, username)`：檢查 listing 擁有者是否為 username
- `get_listing(listing_id)`：取得單一 listing 資訊
- `delete_listing(listing_id)`：刪除 listing 並更新分類
- `category_exist(category)`：檢查分類是否存在
- `get_category(category)`：取得分類下所有 listings（依時間排序）
- `get_top_category()`：取得目前 listings 最多的分類名稱





## 🧩 Design Techniques

- 採用分層模組：CLI 處理互動，Marketplace 處理邏輯，Database 管理資料，分離邏輯與資料儲存，便於測試及維護
- 強調模組化與可擴充性，每個功能單一，方便未來擴充，如 BUY, SEARCH 等...
- 確保商業邏輯層讓維護者不需要了解使用的資料庫結構





## 📬 作者資訊

名子：*陳宗佑* 😸

學號：r13922194

Email：r13922194@ntu.edu.tw



