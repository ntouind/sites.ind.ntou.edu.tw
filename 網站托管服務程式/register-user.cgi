#!/usr/bin/env perl

use String::ShellQuote;

print "Content-Type: text/plain\n\n";
require "readform.pl";

&ReadForm(*admit);

$pop3="./pop3";

# -#$admit{'name'};	描述姓名
# -#$admit{'number'}	使用者學號
# -#$admit{'s_pw'}		使用者校務行政密碼
# -#$admit{'ind_ac'}	帳號
# -#$admit{'ind_pw1'}	密碼
# -#$admit{'ind_pw2'}	密碼再次確認
# -$stu_name=$admit{'name'};
# -$stu_kind=$admit{'RadioGroup'};
# -$stu_id=$admit{'number'};
# -$stu_pw=$admit{'s_pw'};
# -$ind_id=$admit{'ind_ac'};
# -$ind_pw=$admit{'ind_pw1'};
# -$ind_pw2=$admit{'ind_pw2'};
$nickname=$admit{'nickname'}; # 暱稱
$ntouwebmail_id=$admit{'ntouwebmail_id'}; # 海大信箱使用者名稱
$ntouwebmail_password=$admit{'ntouwebmail_password'}; # 海大信箱密碼
$username=$admit{'username'}; # 使用者名稱
$password=$admit{'password'}; # 密碼
$password_again=$admit{'password-again'}; # 密碼再次確認

# 確認非空值
&errmsg("有欄位沒填寫") unless($ntouwebmail_id && $ntouwebmail_password && $username && $password && $password_again && $nickname);

# 把空白去掉
$ntouwebmail_id=~s/[^\d\w]//gi;
$username=~s/[^\d\w]//gi;

# 去除怪符號
$nickname=~s/[\s\$\@\<>]//gi;

# 確認帳號格式
&errmsg("「使用者名稱」欄位格式錯誤") if ($username&&!($username =~ /^[a-z][a-z0-9-]{2,30}$/));
&errmsg("「使用者名稱」欄位為禁止註冊的名稱") if ($username =~ /fuck|adm|sysop|administrator/);

# 兩次密碼輸入要一樣,格式要符合
&errmsg("「密碼」與「再次輸入密碼」欄位不吻合，請再試一次") if($password ne $password || !($password =~/^[\w\d\,\.\/]{5,12}$/));

&errmsg("「暱稱」長度太長") unless($nickname =~ /^.{0,20}$/);

#sleep 3; # Why sleep?

# check 身份
# $stu_id=lc($stu_id); #轉換成小寫
# $ind_id=lc($ind_id); #轉換成小寫
#
# &errmsg("身份不符合，不符合大學部學號") if($stu_kind==1 && !($stu_id=~/^b(\d{8}|\d{3}\w\d{4})$/));
# &errmsg("身份不符合，不符合研究生學號") if($stu_kind==2 && !($stu_id=~/^[dm][\d]{8}$/));
# &errmsg("身份不符合，不符合夜校生學號") if($stu_kind==3 && !($stu_id=~/^n[\d]{8}$/));
# &errmsg("身份不符合，不符合進修部學號") if($stu_kind==4 && !($stu_id=~/^e[\d\w]{8}$/));
# &errmsg("身份不符合，不符合教職員學號") if($stu_kind==5 && ($stu_id=~/^((e[\d\w]{8})|(n[\d]{8})|([dm][\d]{8})|(b(\d{8}|\d{3}\w\d{4})))$/));

$now = `date`;
open(FC,">>register-user-attempt.log");
print FC "$ntouwebmail_id 使用者於 $now 嘗試申請帳號。";
close FC;

# 校務行政密碼認證
$pass = 0;

# 避免傳入參數可以控制系統，使用 shell_quote Perl Module 處理參數
$ntouwebmail_id = shell_quote($ntouwebmail_id);
$ntouwebmail_password = shell_quote($ntouwebmail_password);

$auth = `$pop3 mail.ntou.edu.tw $stu_id $stu_pw`;
$pass=1 if ($auth =~ /認證通過/);
&errmsg("海洋大學 WebMail 帳號或密碼錯誤") unless($pass);
print "海大身份已成功驗證<br>";



# 檢查帳號是否已存在
$admit{'number'}=lc($admit{'number'}); #轉換成小寫
open FP,"</etc/passwd" or die $!;
while(<FP>)
{
    next unless($_);
    next if($_=~/^#/);
    &errmsg($stu_id."已申請過了") if($_=~ /$stu_id/i) ;
    $id=(split(/:/))[0];	#第一行 也就是帳號
    &errmsg($ind_id."帳號已存在") if($ind_id eq $id) ;
}
close FP;

# $dir="/home/notexist";
#
# if($stu_kind<=4){
# 		$sdir="/home/class".substr($stu_id,1,2);
# 		$dir=$sdir."/$stu_id";
# 		$group="student";
# 		mkdir $sdir unless(-e $sdir);
# }
# elsif($stu_kind==5){$dir="/home/faculty/$stu_id";$group ="faculty";}

# 一般使用者沒有 shell 存取權
$shell = "/usr/sbin/nologin";
$group = "student";
$homedir = "/home/"."$username";
$user_site_rootdir = $homedir."/網站根目錄"
# $user_log_dir = $homedir."/服務運行紀錄"

# 嘗試新增群組，即便已經存在
system("addgroup", "sftponly");
system("addgroup", "student");

# 新增使用者
system("adduser", "--no-create-home", "--home", $homedir, "--ingroup", "sftponly", "--shell", $shell, $username);

system("adduser", $username, "student");

# 建立並設定家目錄存取權限
system("mkdir", "$homedir");
system("chown", "--recursive", "root:other-sites-readable", $homedir);

# 建立並設定網站根目錄存取權限
system("mkdir", $user_site_rootdir);
system("chown", "--recursive", "$username:other-sites-readable", $user_site_rootdir);
system("chmod", "2750", $user_site_rootdir);

# 設定使用者磁碟空間限額
system("edquota", "--prototype", "template-user" , $username);

# 設定使用者密碼
# $tmp="/root/tmp";
# open(FDP,">$tmp");
# print FDP "$ind_pw\n";
#
# $chpw="/usr/sbin/pw usermod -n $ind_id -h fd";
# `$chpw < $tmp`;
# close(FDP);
#
# $cmd="/bin/rm -f $tmp";
# `$cmd`;

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
        exit(0);
}
