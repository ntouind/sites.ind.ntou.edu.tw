#!/usr/bin/env perl

use String::ShellQuote;

print "Content-Type: text/plain\n\n";
require "readform.pl";

&ReadForm(*admit);

#$pop3="./pop3";

$nickname="$admit{'nickname'}"; # 暱稱
$ntouwebmail_id="$admit{'ntouwebmail_id'}"; # 海大信箱使用者名稱
$ntouwebmail_password="$admit{'ntouwebmail_password'}"; # 海大信箱密碼
$username="$admit{'username'}"; # 使用者名稱
$password="$admit{'password'}"; # 密碼
$password_again="$admit{'password-again'}"; # 密碼再次確認

# 確認非空值
&errmsg("錯誤：有欄位沒填寫") unless($ntouwebmail_id && $ntouwebmail_password && $username && $password && $password_again && $nickname);

# 把空白去掉
$ntouwebmail_id=~s/[^\d\w]//gi;
$username=~s/[^\d\w]//gi;

# 去除怪符號
$nickname=~s/[\s\$\@\<>]//gi;

# 確認帳號格式
&errmsg("錯誤：「使用者名稱」欄位格式錯誤") if ($username&&!($username =~ /^[a-z][a-z0-9-]{2,30}$/));
&errmsg("錯誤：「使用者名稱」欄位為禁止註冊的名稱") if ($username =~ /root|adm|sysop|administrator/);

# 兩次密碼輸入要一樣,格式要符合
&errmsg("錯誤：「密碼」與「再次輸入密碼」欄位不吻合，請再試一次") if($password ne $password_again || !($password =~/^[\w\d\,\.\/]{5,12}$/));

&errmsg("錯誤：「暱稱」長度太長") unless($nickname =~ /^.{0,20}$/);

#sleep 3; # Why sleep?

$now = `date`;
open(FC,">>register-user-attempt.log");
print FC "$ntouwebmail_id 使用者於 $now 嘗試申請帳號。";
close FC;

# 海大身份驗證
# $pass = 0;

# 避免傳入參數可以控制系統，使用 shell_quote Perl Module 處理參數
# $ntouwebmail_id = shell_quote($ntouwebmail_id);
# $ntouwebmail_password = shell_quote($ntouwebmail_password);

#$auth = `$pop3 mail.ntou.edu.tw $stu_id $stu_pw`;
#$pass=1 if ($auth =~ /認證通過/);
#&errmsg("海洋大學 WebMail 帳號或密碼錯誤") unless($pass);
#print "海大身份已成功驗證<br>";

# 檢查帳號是否已存在
# $admit{'number'}=lc($admit{'number'}); #轉換成小寫
# open FP,"</etc/passwd" or die $!;
# while(<FP>)
# {
#     next unless($_);
#     next if($_=~/^#/);
#     &errmsg($stu_id."已申請過了") if($_=~ /$stu_id/i) ;
#     $id=(split(/:/))[0];	#第一行 也就是帳號
#     &errmsg($ind_id."帳號已存在") if($ind_id eq $id) ;
# }
# close FP;

# 一般使用者沒有 shell 存取權
$user_shell = "/usr/sbin/nologin";

$user_group = "web-hosting-users";
$user_homedir = "/home/"."$username";
$user_site_rootdir = $user_homedir."/網站根目錄";
# $user_log_dir = $user_homedir."/服務運行紀錄"

# 嘗試新增群組，即便已經存在
system("sudo", "addgroup", "sftponly");
system("sudo", "addgroup", "$user_group");

# 新增使用者
system("sudo", "adduser", "--no-create-home", "--home", "$user_homedir", "--ingroup", "$user_group", "--shell", "$user_shell", "$username");

# 將使用者加入只能使用 SFTP 不能用 SSH 的使用者群組
system("sudo", "adduser", $username, "sftponly");

# 建立並設定家目錄存取權限
system("sudo", "mkdir", "$user_homedir");
system("sudo", "chown", "--recursive", "root:other-sites-readable", "$user_homedir");

# 建立並設定網站根目錄存取權限
system("sudo", "mkdir", "$user_site_rootdir");
system("sudo", "chown", "--recursive", "$username:other-sites-readable", "$user_site_rootdir");
system("sudo", "chmod", "2750", "$user_site_rootdir");

# 設定使用者磁碟空間限額
system("sudo", "edquota", "--prototype", "template-user" , "$username");

# 設定使用者密碼
# $chpasswd_password_file="chpasswd.passwd";
# open(FDP,">$chpasswd_password_file");
# print FDP "$username:$password\n";
# $chpw="/usr/sbin/pw usermod -n $username -h fd";
# `$chpw < $tmp`;
# close(FDP);
#
# $cmd="/bin/rm -f $tmp";
# `$cmd`;
system("sudo", "chpasswd", "$username:$password");

open(FC,">>register-user-success.log");
print FC "$nickname ($ntouwebmail_id) 於 $now 申請 $username 帳號成功。";
close FC;

print <<EOT;
您的帳號已經成功建立。
使用教學：https://sites.ind.ntou.edu.tw/tutorial.markdown
有任何問題請來信 ntouind\@gmail.com 說明您遇到的詳細狀況。
EOT
exit(0);

sub errmsg
{
        print shift;
        exit(1);
}
