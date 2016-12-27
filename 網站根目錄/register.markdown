# 註冊帳號<br />Register Account

[[回首頁](/)]

請先閱畢我們的[服務條款](/terms.markdown)再嘗試註冊帳號。

<form id="registration-form" method="post" action="/cgi-bin/register-user.cgi">
	<table>
		<thead>
			<tr>
				<th>填寫項目</th><th>回答</th><th>說明</th>
			</tr>
		</thead>
		<tfoot>
			<tr>
				<td colspan="3">
					<input id="submit" type="submit" value="送出" />
					<input id="reset" type="reset" value="清空表單" />
				</td>
			</tr>
		</tfoot>
		<tbody>
			<tr>
				<td>海大信箱使用者名稱</td><td><input name="ntouwebmail_id" type="text" size="10" maxlength="30" /></td><td>教職員為您所申請的電子郵件信箱使用者名稱，學生則為您的學號，請參閱<a href="http://infosec.ntou.edu.tw/?p=174" target="_blank">預設帳號密碼為何 ? &#x007c; 海大資訊站</a></td>
			</tr>
			<tr>
				<td>海大信箱密碼</td><td><input name="ntouwebmail_password" type="text" size="10" maxlength="30" /></td><td>職員為您所申請的電子郵件信箱使用者密碼，學生則為您所設定的密碼或預設密碼，請參閱<a href="http://infosec.ntou.edu.tw/?p=174" target="_blank">預設帳號密碼為何 ? &#x007c; 海大資訊站</a><br />注意：不是<a href="http://ais.ntou.edu.tw" target="_blank">海大教學務系統</a>的密碼</td>
			</tr>
			<tr>
				<td>暱稱</td><td><input name="nickname" type="text" size="10" maxlength="20" /></td><td>希望我們稱呼您的名稱</td> 
			</tr>
			<tr>
				<td>使用者名稱</td><td><input name="username" type="text" size="10" maxlength="20"  /></td><td>服務中實際使用的名稱<br />
	限制：<br />
	<ul>
		<li>只能使用小寫英文字母、數字、連字號(-)、底線(_)</li>
		<li>只能以英文字母作為開頭字元</li>
	</ul>
				</td>
			</tr>
			<tr>
				<td rowspan="2">密碼</td><td><input name="password" type="password" size="10" maxlength="100" /></td><td>服務中使用的密碼，請勿使用弱密碼</td>
			</tr>
			<tr>
				<!-- <td>密碼</td> --><td><input name="password-again" type="password" size="10" maxlength="100" /></td><td>為避免輸入錯誤，請再次輸入一次密碼</td>
			</tr>
			<tr>
				<td>慣用電子郵件地址</td><td><input name="perferred-email-address" type="text" size="10" maxlength="254" /><!-- [standards - What is the longest possible email address? - Stack Overflow](http://stackoverflow.com/questions/7717573/what-is-the-longest-possible-email-address#7717596) --></td><td>您的慣用電子郵件地址，我們將會用此電子郵件地址跟學校信箱來發送服務通知<br />此信箱可用於重設服務密碼，請勿使用拋棄式電子信箱</td>
			</tr>
		</tbody>
	</table>
</form>
