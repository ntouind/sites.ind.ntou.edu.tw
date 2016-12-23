# 使用教學

[[回首頁](https://sites.ind.ntou.edu.tw)]

## 取得一個 SFTP 客戶端軟體
您可以使用慣用的 SFTP 客戶端軟體來上傳網站內容，在這個教學中我們以自由與開放來源碼又跨平台的 [Filezilla FTP/FTPS/SFTP 客戶端軟體](https://filezilla-project.org/)為例

注意：FileZilla 另有提供 FTP 伺服器(server)產品，請下載其客戶端(client)產品

## 建立站台設定檔（僅適用 FileZilla 客戶端軟體）
為了日後存取方便您可以啟動 FileZilla 後請至 `檔案(F)/站台管理員(S)` 新增一個新站台細節如下：

* 「主機」欄位填入「sites.ind.ntou.edu.tw」
* 「連接埠」欄位毋須填寫（將使用預設值）
* 「協定」下拉式選單選擇「SFTP - SSH File Transfer Protocol」
* 「登入型式」選擇「一般」
* 「使用者」欄位填入您於註冊頁面填寫的使用者名稱（獨立域名使用者則是您所申請的**完整域名**，如 「xxx.ntou.edu.tw」）
* 「密碼」欄位則輸入您的密碼

![FileZilla 站台管理員一般使用者設定方式示意圖](assets/pictures/tutorial-filezilla-site-manager-regular-user-example.png)  
![FileZilla 站台管理員獨立域名使用者設定方式示意圖](assets/pictures/tutorial-filezilla-site-manager-individual-domain-user-example.png)

然後點擊「確定(O)」即可保存站台設定，日後如需連線即可直接到站台管理員中選取您要連線的站台後點擊「連線&#x0028;C&#x0029;」即可連線

## 連線伺服器
如使用其他 SFTP 客戶端軟體本服務的 SFTP 檔案傳輸介面的連線細節如下：

<table>
	<thead>
		<tr><th>主機名稱</th><th>連接埠(Port)</th><th>使用者名稱</th><th>密碼</th></tr>
	</thead>
	<tbody>
		<tr><td>sites.ind.ntou.edu.tw</td><td>22（預設埠）</td><td>您於註冊時所設定的使用者名稱<br />（如為獨立域名使用者則為您的<strong>完整域名</strong>）</td><td>您於註冊時所設定的密碼<br />（如為獨立域名使用者則為我們發給您的密碼）</td></tr>
	</tbody>
</table>

請參考該軟體的使用手冊設定連線。

如果您的客戶端軟體要求使用 URL（網址）來連線伺服器，請使用：

    sftp://〈使用者名稱〉@sites.ind.ntou.edu.tw

來進行連線

## 檔案管理
連線完成後*中間靠右側*的遠端站台面板即會列出伺服器端的檔案列表

![FileZilla 檔案管理介面遠端站台面板示意圖](assets/pictures/tutorial-filezilla-file-manager-remote-panel-rootdir.png)

「網站根目錄/」為您的網站的最上層目錄，對應一般使用者的 `http(s)://sites.ind.ntou.edu.tw/~〈使用者名稱〉` 與獨立域名使用者的 `http(s)://〈您所申請的域名〉/`，將左側本地站台面板中要上傳的檔案選取後在其內容導向選單(contextual menu)中選取「上傳(U)」即可將選取的檔案上傳到遠端伺服器

提示：如果出現「上傳失敗」錯誤訊息請檢查您是否在遠端站台面板中尚未切換到「網站根目錄」目錄，這是您唯一可以上傳檔案的地方

![FileZilla 檔案管理介面本地站台面板上傳檔案示意圖](assets/pictures/tutorial-filezilla-file-manager-local-panel-file-upload.png)

上傳完成之後您應可於對應的網址察看到您上傳的網站內容：

![上傳結果示意圖](assets/pictures/tutorial-individual-domain-upload-result.png)

## 檢視服務運行紀錄
查閱運行紀錄是找出網站問題的最佳手段，您可於遠端站台中的「服務運行紀錄」目錄中找到您網站的相關運行紀錄，目前包含：

| 檔案名稱 | 用途 | 
| :--------: | :-------: |
| access.log | Web 伺服器存取紀錄 |
| error.log | Web 伺服器錯誤紀錄 | 

如果您的磁碟配額用盡您可以刪除運行紀錄檔以清出一些空間（注意：由於運行紀錄檔不會立刻重建這樣做可能會讓您遺失部份運行紀錄與短時間內無法查閱運行紀錄）

## 常見問答集<br />Frequently Asked Questions
### 我的〈填入動態網頁語言〉網頁無法正常顯示
目前本站不支持任何動態語言，如有需求請來信洽詢

### 我的網站的部份資源 Web 瀏覽器拒絕載入
為維護資訊安全，本站全域強制使用 HTTPS 安全連線協議，若網頁中的外連資源不支援 HTTPS 則會被部份 Web 瀏覽器拒絕載入，改用 HTTPS 版本的外連資源連結或是將資源上傳到本服務中即可解決此問題。

獨立域名使用者可以選擇將此政策停用，如有此需求請跟我們連繫。

如有任何問題，請不吝來信網路發展協會 &lt;<ntouind@gmail.com>&gt; 詢問