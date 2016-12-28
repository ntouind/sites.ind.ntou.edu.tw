/* pop3-user-authentication - 基於 POP3 協定的使用者身份驗證工具 */
/**
  @file pop3-user-authentication.c
  @brief 基於 POP3 協定的使用者身份驗證工具
  @author 饒仁達（推測之原始作者）
  @author 林博仁 <Buo.Ren.Lin@gmail.com>
  @copyright Refer project readme for the license
*/

/* for printf and etc. */
#include <stdio.h>

/* For
 * strncasecmp - compare two strings ignoring case
 * bcopy - copy byte sequence */
#include <string.h>

/* For close(2) - close a file descriptor */
#include <unistd.h>

/* For socket(7)
 * POSIX.1 does not require the inclusion of <sys/types.h>, and this header file is not required on Linux. However, some historical (BSD) implementations required this header file, and portable applications are probably wise to include it. */
#include <sys/socket.h>
#include <sys/types.h>

/* For inet_aton, inet_addr(3), inet_network, inet_ntoa, inet_makeaddr, inet_lnaof, inet_netof - Internet address manipulation routines */
#include <netinet/in.h>
#include <arpa/inet.h>

/* For gethostbyname(3), gethostbyaddr, sethostent, gethostent, endhostent, h_errno, herror, hstrerror, gethostbyaddr_r, gethostbyname2, gethostbyname2_r, gethostbyname_r, gethostent_r - get network host entry */
#include <netdb.h>
extern int h_errno;

#define TIMEOUT_SEC 20
#define PORT_POP3 110

/** @brief 將域名轉換成 IP 地址
    @arg host_name 域名
    @returns addr.s_addr(?)
    @retval 0 轉換失敗 */
unsigned long name_resolve(unsigned char * host_name)
{
	struct in_addr addr;
	struct hostent * host_ent;

	if((addr.s_addr = inet_addr(host_name)) == -1)
	{
		if(!(host_ent = gethostbyname(host_name))) {
			printf("錯誤：找不到郵件主機(%s)。", host_name);
			return (0);
		}

		bcopy(host_ent->h_addr, (char *)&addr.s_addr,
		      host_ent->h_length);
	}

	return (addr.s_addr);
}

/** @brief 跟伺服器交談的部份
    @arg host_name 域名
    @returns addr.s_addr(?)
    @retval 0 轉換失敗 */
int interactive(int s, char * cmd) {
	int bytes;
	char ret[1024] = "";

	if(cmd)
		if(send(s, cmd, strlen(cmd), 0) == -1) {
			printf("錯誤：POP3 命令送出失敗。\n");
			close(s);
			return(0);
		}

	bytes = recv(s, ret, 1024, 0);
	ret[bytes] = '\0';

	if(strncasecmp(ret, "+OK", 3) == 0) {
		ret[0] = '\0';
	} else {
		printf("錯誤：POP3 命令執行發生錯誤。\n");
		close(s);
		return(0);
	}

	return(1);
}

/** @brief main 函式 - C/C++ 程式的進入點(entry point)
    @arg argc 呼叫程式的命令列參數數量
    @arg argv 呼叫程式的命令列參數字串陣列
    @returns 此程式要傳回作業系統的結束狀態碼
    @retval 1 身份驗證成功
    @retval 0 身份驗證失敗 */
int main(int argc, char * argv[]) {
	char cmd[128];
	int s;
	struct sockaddr_in saddr;
	char * username;
	char * password;

	if(argc <= 3) {
		printf("錯誤：參數不正確(host, name, password)。\n");
		return -1;
	}

	username = argv[2];
	password = argv[3];
	s = socket(PF_INET, SOCK_STREAM, 0);
	memset(&saddr, 0, sizeof(saddr));
	saddr.sin_family = PF_INET;
	saddr.sin_port = htons(PORT_POP3);
	saddr.sin_addr.s_addr = name_resolve(argv[1]);

	if(connect(s, (struct sockaddr *)&saddr, sizeof(saddr)) == 0) {
		interactive(s, NULL);
		sprintf(cmd, "USER %s\r\n", username);

		if(interactive(s, cmd) == 0) {
			printf("錯誤: 使用者名稱不存在(%s)\n", username);
			close(s);
			return(0);
		}

		sprintf(cmd, "PASS %s\r\n", password);

		if(interactive(s, cmd) == 0) {
			printf("錯誤: 使用者名稱與密碼組合錯誤(%s)\n", password);
			close(s);
			return(0);
		}

		send(s, "QUIT\r\n", 6, 0);
		close(s);
	} else {
		printf("錯誤：無法連接伺服器\n");
		close(s);
		return(0);
	}

	printf("正確：認證通過\n");
	return(1);
}
