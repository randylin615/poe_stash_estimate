# poe_stash_estimat   一個用來估計PoE倉庫/公倉價值的小小應用
### FastAPI + Vue CDN + PostgreSQL(SQLAlchemy)
</br> 

## 注意事項
### 目前僅針對單頁倉庫，並以ninja網賣方價格計算價值。
### 計價之物品初版僅有通貨及符文。
</br>

## 安裝/啟動方法
請先自行完成postgreSQL安裝，[此處](https://github.com/randylin615/poe_stash_estimate/blob/main/sundries/Items.csv)有提供可直接導入的table。
1. 開啟 power shell 後 git clone  
`$git clone https://github.com/randylin615/poe_stash_estimate.git`

2. 修改 `/backend/database.py` 中postgreSQL的URL，此處須根據postgreSQL安裝時的設定  
>`URL_DATABASE='postgresql://<username>:<password>@localhost:5432/<databasename>'`  
ex:
`URL_DATABASE='postgresql://postgresql:postgresql@localhost:5432/postgresql'` 
3. 修改 `/frontend/poe_stash_est.html` 中FastAPI的URL，此處須和後續uvicorn host的ip相同   
>`const apiUrl = "";`  
ex:
`const apiUrl = "http://127.0.0.1:8000/"`

4. 進入虛擬環境  
`$.\poe_stash_estimate\.venv\Scripts\activate`

5. uvicorn 啟動伺服器，此處須和上述html中apiUrl的ip相同  
`$uvicorn main:app --host 127.0.0.1 --port 8000 --reload`

6. 使用瀏覽器開啟 `/frontend/poe_stash_est.html` 即可




</br>

## 使用方法

<div style="display: flex; justify-content: center; gap: 10%; flex-wrap: wrap;">
    <div style="text-align: center; max-width: 40%;">
        <img src="https://github.com/randylin615/poe_stash_estimate/blob/main/sundries/eg_pic1.png?raw=true" alt="eg_pic1" style="width: 100%; height: 70%; object-fit: contain;">
        <p style="text-align: justify;">1. 開啟PoE官網、F12切換至網路活動，並擷取Fetch/XHR<br>
           2. 點擊頭像選擇腳色，至欲估計的倉庫頁取得GGG的API request
        </p>
    </div>
    <div style="text-align: center; max-width: 40%;">
        <img src="https://github.com/randylin615/poe_stash_estimate/blob/main/sundries/eg_pic2.png?raw=true" alt="eg_pic2" style="width: 100%; height: 70%; object-fit: contain;">
        <p style="text-align: justify;">3. 雙擊get(-guild)-stash開啟本圖頁面<br>
           4. 點擊美化排版 (只是看起來比較舒服，不影響運行)，並Ctrl+A全選後複製到下方輸入欄
        </p>
    </div>
    <div style="text-align: center; max-width: 40%;">
        <img src="https://github.com/randylin615/poe_stash_estimate/blob/main/sundries/eg_pic3.png?raw=true" alt="eg_pic3" style="width: 100%; height: 100%; object-fit: contain;">
        <p style="text-align: justify;">5. 上傳後即可點選通貨進行計價
        </p>
    </div>
</div>

## 後續更新方向
- [ ] BUG_一般裝備被讀取時error
- [ ] 加入物品(ex:催化劑、油瓶等)
- [ ] 部署至GCP Cloud Run
- [ ] 帳號歷史紀錄
- [ ] API整理(CRUD分離)
</br>  

## 特別感謝 
[poe.ninja/economy](https://poe.ninja/economy/settlers/currency) 網站統整的各物品交易價格及API

[FastAPI + SQLAlchemy+PostgreSQL — FastAPI的ORM](https://medium.com/@King610160/fastapi-sqlalchemy-postgresql-fastapi的orm-00818bc63106) Tako大的筆記

救了我很多前端問題的ChatGPT


