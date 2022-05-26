#include <unistd.h>
#include <pthread.h>
#include <sched.h>
#include <stdio.h>
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
static void set_thread_policy(pthread_attr_t attr, int policy)
{
        pthread_attr_setschedpolicy(&attr, policy);
        get_thread_policy(attr);
}
static void show_thread_priority(pthread_attr_t attr, int policy)
{
        int priority = sched_get_priority_max(policy);
        printf(" max priority = %d, ", priority);
        priority = sched_get_priority_min(policy);
        printf(" min priority = %d\n", priority);
}
static int get_thread_priority(pthread_attr_t attr)
{
        struct sched_param param;
        pthread_attr_getschedparam(&attr, &param);
        printf(" priority = %d\n", param.sched_priority);
        return param.sched_priority;
}
int main (void)
{
        pthread_attr_t attr;
        struct sched_param sched;
        pthread_attr_init(&attr);
        printf("- Show Current Policy:");
        int policy = get_thread_policy(attr);
        printf("- Show current configuration of priority:");
        show_thread_priority(attr, policy);
        printf("- Show SCHED_FIFO of priority:");
        show_thread_priority(attr, SCHED_FIFO);
        printf("- Show SCHED_RR of priority:");
        show_thread_priority(attr, SCHED_RR);
        printf("- Show priority of current thread:");
        int priority = get_thread_priority(attr);
        printf("\n -SET THREAD POLICY\n");
        printf("- SET SCHED_FIFO policy:");       
        set_thread_policy(attr, SCHED_FIFO);
        printf("- SET SCHED_RR policy:");  
        set_thread_policy(attr, SCHED_RR);
        printf("- Restore current policy:");
        set_thread_policy(attr, policy);
        pthread_attr_destroy(&attr);
        return 0;
}