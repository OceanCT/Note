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

thread_sched.c解析
```cpp
#include <unistd.h>
#include <pthread.h>
#include <sched.h>
#include <stdio.h>
// 获取当前线程的调度属性
static int get_thread_policy(pthread_attr_t attr)
{
        int policy;
        pthread_attr_getschedpolicy(&attr, &policy);
        switch(policy)
        {
                 case SCHED_FIFO:
                         printf(" policy = SCHED_FIFO\n");
                         break;
                 case SCHED_RR:
                         printf(" policy = SCHED_RR\n");
                         break;
                 case SCHED_OTHER:
                         printf(" policy = SCHED_OTHER\n");
                         break;
                 default:
                         printf(" policy = UNKOWN\n");
                         break;
        }
        return policy;
}
// 设置线程的调度属性
static void set_thread_policy(pthread_attr_t *attr, int policy)
{
        pthread_attr_setschedpolicy(attr, policy);
        get_thread_policy(*attr);
}
// 展示并打印线程的调度属性下的最高和最低优先级
static void show_thread_priority(pthread_attr_t attr, int policy)
{
        int priority = sched_get_priority_max(policy);
        printf(" max priority = %d, ", priority);
        priority = sched_get_priority_min(policy);
        printf(" min priority = %d\n", priority);
}
// 展示并打印当前线程属性的优先级
static int get_thread_priority(pthread_attr_t attr)
{
        struct sched_param param;
        pthread_attr_getschedparam(&attr, &param);
        printf(" priority = %d\n", param.sched_priority);
        return param.sched_priority;
}
int main (void)
{
        // 创建线程属性
        pthread_attr_t attr;
        struct sched_param sched;
        // 初始化线程属性
        pthread_attr_init(&attr);
        // 查看默认线程调度属性及其优先级相关信息
        printf("- Show Current Policy:");
        int policy = get_thread_policy(attr);
        printf("- Show current configuration of priority:");
        show_thread_priority(attr, policy);
        // 设置线程的调度属性为FIFO, 并获取其优先级相关信息
        printf("- Show SCHED_FIFO of priority:");
        show_thread_priority(attr, SCHED_FIFO);
        // 设置线程的调度属性为RR, 并获取其优先级相关信息
        printf("- Show SCHED_RR of priority:");
        show_thread_priority(attr, SCHED_RR);
        // 查看默认线程优先级
        printf("- Show priority of current thread:");
        get_thread_priority(attr);
        // 改变线程的调度属性
        printf("\n- SET THREAD POLICY\n");
        // 设置线程的调度属性为FIFO
        printf("- SET SCHED_FIFO policy:");       
        set_thread_policy(&attr, SCHED_FIFO);
        // 设置线程的调度属性为RR
        printf("- SET SCHED_RR policy:");  
        set_thread_policy(&attr, SCHED_RR);
        // 回复为默认调度属性
        printf("- Restore current policy:");
        set_thread_policy(&attr, policy);
        // 销毁线程属性
        pthread_attr_destroy(&attr);
        return 0;
}
```