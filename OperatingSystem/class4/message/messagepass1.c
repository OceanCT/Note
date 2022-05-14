#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <time.h>
#include <strings.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stddef.h>

struct msg {
    long msg_types;
    char msg_buf[511];
};

int main(){
    int qid, pid, len;
    struct msg pmsg;
    sprintf(pmsg.msg_buf, "Hello! This is :%d\n", getpid());
    len = strlen(pmsg.msg_buf);

    if((qid = msgget(IPC_PRIVATE,IPC_CREAT|0666))< 0){
        perror("msgget");
        exit (1);
    }

    if((msgsnd(qid,&pmsg,len,0))<0){
        perror("msgsnd");
        exit(1);
    }
    printf("Send a message to the queue successfully : %d\n", qid);
    exit(1);
}