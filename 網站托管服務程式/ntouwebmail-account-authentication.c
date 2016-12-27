#include <stdio.h>
#include <string.h>
#include <sys/time.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <arpa/inet.h>

#define TIMEOUT_SEC 20

int check_name(char *name) {
        int i, count=0;

        for(i = 0; i < strlen(name); i++) {
                if((name[i] >= '0' && name[i] <= '9')
                || (name[i] >= 'A' && name[i] <= 'Z')
                || (name[i] >= 'a' && name[i] <= 'z')
                || (name[i] == '-' || name[i] == '_'))
                        count++;
        }

        if(count == strlen(name))
                return(1);
        return(0);
}

int interactive(int s, char *cmd) {
        int bytes;
        char ret[1024]="";

        if(cmd)
        if(send(s, cmd, strlen(cmd), 0)==-1) {
                printf("連線中斷");
                close(s);
                return(0);
        }

                bytes = recv(s, ret, 1024, 0);
                ret[bytes] = '\0';
                if(strncasecmp(ret, "+OK", 3)==0) {
                        ret[0] = '\0';
                } else {
                        printf("失敗");
                        close(s);
                        return(0);
                }
        return(1);
}

unsigned long name_resolve(unsigned char *host_name)
{
        struct in_addr addr;
        struct hostent *host_ent;

        if ((addr.s_addr = inet_addr(host_name)) == -1)
        {
                if (!(host_ent = gethostbyname(host_name))){
                    printf("錯誤: 找不到郵件主機(%s).", host_name);
                    return (0);
                }
                bcopy(host_ent->h_addr, (char *)&addr.s_addr,
host_ent->h_length);
        }
        return (addr.s_addr);
}

int main(int argc,char *argv[]) {
        char cmd[128];

        int s;
        struct sockaddr_in saddr;
        char *username;
        char *password;
        if (argc <= 3) {
            printf("錯誤: 參數不正確(host, name, password)");
            return -1;
        }
        username=argv[2];
        password=argv[3];

        s = socket(PF_INET, SOCK_STREAM, 0);
        memset(&saddr, 0, sizeof(saddr));
        saddr.sin_family = PF_INET;
        saddr.sin_port = htons(110);
        saddr.sin_addr.s_addr = name_resolve(argv[1]);

        if(connect(s, (struct sockaddr*)&saddr, sizeof(saddr))== 0) {

                interactive(s,NULL);
                sprintf(cmd, "USER %s\r\n", username);
                if(interactive(s, cmd)==0){
                        printf("錯誤: 使用者不正確(%s)", username);
                        close(s);
                        return(0);
                }

                sprintf(cmd, "PASS %s\r\n", password);
                if(interactive(s, cmd)==0){
                        printf("錯誤: 密碼錯誤(%s)", password);
                        close(s);
                        return(0);
                }
                send(s, "QUIT\r\n", 6, 0);
                close(s);

        } else {
                printf("連線失敗");
                close(s);
                return(0);
        }
        printf("正確: 認證通過");
        return(1);
}
