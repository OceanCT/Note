thread_scope.c解析
```cpp
// 导入头文件
#include <pthread.h>
#include <stdio.h>
// 声明线程数
#define NUM_THREADS 5
// 声明线程所需运行的函数
void * runner(void * param);
int main (int argc, char * argv[]){
        int i, scope;
        // 声明线程变量
        pthread_t tid[NUM_THREADS];
        // 声明线程参数
        pthread_attr_t attr;
        // 初始化线程参数
        pthread_attr_init(&attr);
        // 打印线程参数
        if (pthread_attr_getscope(&attr, &scope) != 0)
                 fprintf(stderr, "unable to ge scheduling scope\n");
        else {
                 if (scope == PTHREAD_SCOPE_PROCESS)
                         printf("PTHREAD_SCOPE_PROCESS\n");
                 else if (scope == PTHREAD_SCOPE_SYSTEM)
                         printf("PTHREAD_SCOPE_SYSTEM\n");
                 else
                         fprintf(stderr, "Illegal scope value.\n");
        }
        // 调节线程参数
        pthread_attr_setscope(&attr, PTHREAD_SCOPE_PROCESS);
        // 打印线程参数
        if (pthread_attr_getscope(&attr, &scope) != 0)
                 fprintf(stderr, "unable to ge scheduling scope\n");
        else {
                 if (scope == PTHREAD_SCOPE_PROCESS)
                         printf("PTHREAD_SCOPE_PROCESS\n");
                 else if (scope == PTHREAD_SCOPE_SYSTEM)
                         printf("PTHREAD_SCOPE_SYSTEM\n");
                 else
                         fprintf(stderr, "Illegal scope value.\n");
        }
        // 创建线程
        for (i = 0; i < NUM_THREADS; i++ )
                 pthread_create(&tid[i], &attr, runner, NULL);
        // 等待线程结束
        for (i = 0; i < NUM_THREADS; i++ )
                 pthread_join(tid[i], NULL);
}
// 线程函数
void * runner(void * param)
{
        pthread_exit(0);
}
```