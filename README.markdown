# 海洋大學網路發展協會網站托管服務<br />NTOU IND Site Hosting Service
這裡是[海洋大學網路發展協會網站托管服務](https://sites.ind.ntou.edu.tw)與它的開發與維護專案  
到 <http://github.com/ntouind/sites.ind.ntou.edu.tw> 參與本專案的開發！

[註冊帳號] [忘記密碼] [管理帳號] [[使用教學](tutorial.markdown)] [[回報問題／建議（議題追蹤系統）](https://github.com/ntouind/sites.ind.ntou.edu.tw/issues)] [[服務條款](terms.markdown)] [[隱私政策](privacy-policy.markdown)] [[資訊安全政策](security-policy.markdown)]

## 特色<br />Features
* **（尚未實作完成）**支援 sites.ind.ntou.edu.tw 域名下使用者自己托管網站
	* 靜態網頁
	* **（尚未支援）**PHP
	* **（尚未支援）**MySQL/MariaDB 資料庫
	* （不支援）CGI 程式
* 支援其他域名的站台托管（請來信 <ntouind@gmail.com> 洽詢，我們保留是否通過申請的決定權）
* 支援以 [Let's Encrypt - Free SSL/TLS Certificates](https://letsencrypt.org/) 為基礎的 HTTPS 加密通訊協議，保護傳輸的資料
* **（限主網站）**俱備可自訂的 [Apache Web 伺服器錯誤頁面](https://sites.ind.ntou.edu.tw/http-404-not-found)
* **（限主網站）**使用 [Git](https://git-scm.com/)、[Git Large File Storage](https://git-lfs.github.com/) 管理網站內容，並支持 [GitHub Web 掛勾程式](https://developer.github.com/webhooks/)在提交新版本至 GitHub 時自動更新網站版本
* 預設啟用每天自動安裝系統更新並重新啟動系統讓伺服器維持最佳運作狀態與安全性
* 俱備良好的[維護文件](http://github.com/ntouind/sites.ind.ntou.edu.tw/wiki)

## 開發目標<br />Development Goals
* 一個易於架設維護、安全的 L.A.M.P.(Linux+Apache+MySQL/MariaDB+PHP) 伺服器與網站托管服務
* 作為讓社員學習 Apache 多虛擬主機(Virtual Host)、PHP 動態網頁設計、CGI 程式設計、多重使用者管理、磁碟配額控制的平台
* 一樣，能公開的資源都會公開在 GitHub 上

## 作者<br />Authors
* 本作品由國立台灣海洋大學網路發展協會之社員所作，惟至近期並沒有紀錄誰改了什麼
* 目前有紀錄的作者請參考 [Contributors to ntouind/sites.ind.ntou.edu.tw](https://github.com/ntouind/sites.ind.ntou.edu.tw/graphs/contributors)

## 目前維護者<br />Current Maintainer
林博仁 &lt;<Buo.Ren.Lin@gmail.com>&gt;

## 智慧財產授權條款<br />I.P. License
除特別註明授權條款的內容，本智慧財產採用 [Creative Commons 《姓名標示 - 相同方式分享》授權條款第 4.0 版](https://creativecommons.org/licenses/by-sa/4.0/)或其任意更近期之版本釋出供所有人在授權範圍內自由使用

在授權範圍外之使用請來信國立台灣海洋大學網路發展協會 &lt;<ntouind@gmail.com>&gt; 洽詢

## 相關連結<br />Related links
* [ntouind/sites.ind.ntou.edu.tw Wiki](https://github.com/ntouind/sites.ind.ntou.edu.tw/wiki)
* [舊站逆向工程 · ntouind/sites.ind.ntou.edu.tw Wiki](https://github.com/ntouind/sites.ind.ntou.edu.tw/wiki/%E8%88%8A%E7%AB%99%E9%80%86%E5%90%91%E5%B7%A5%E7%A8%8B)
* [架站指引 · ntouind/sites.ind.ntou.edu.tw Wiki](https://github.com/ntouind/sites.ind.ntou.edu.tw/wiki/%E6%9E%B6%E7%AB%99%E6%8C%87%E5%BC%95)
* [ntouind/sites.ind.ntou.edu.tw-etckeeper: 海洋大學網路發展協會網站托管服務的 etckeeper](https://github.com/ntouind/sites.ind.ntou.edu.tw-etckeeper) 
