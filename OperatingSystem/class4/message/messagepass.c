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
#define MSG_TYPE 1
#define MSG_SIZE 512
struct msg {
    long msg_types;
    char msg_buf[MSG_SIZE];
};
int qid, pid;
void create_queue(){
    if((qid = msgget(IPC_PRIVATE,IPC_CREAT|0666))< 0){
        perror("msgget");
        exit (1);
    }
}
void send(){
    struct msg pmsg;
    pmsg.msg_types = MSG_TYPE;
    sprintf(pmsg.msg_buf, "Hello! This is :%d\n", getpid());
    if((msgsnd(qid,&pmsg,MSG_SIZE,0))<0){
        perror("msgsnd");
        exit(1);
    }
    printf("Send a message to the queue successfully : %d\n", qid);
    printf("%s",pmsg.msg_buf);
}
void receive(){
    struct msg pmsg;
    if((msgrcv(qid,&pmsg,MSG_SIZE,MSG_TYPE,0))<0){
        perror("msgrcv");
        exit(1);
    }
    printf("Receive a message from the queue successfully : %d\n", qid);
    printf("%s", pmsg.msg_buf);
}
int main(){
    create_queue();
    pid_t pid = fork();
    if(!pid){
        send();
    }else{
        pid_t pid = fork();
        if(!pid){
            receive(); 
        }
    }   
    return 0;
}