gcc thread_scope.c -o thread_scope -pthread
gcc thread_sched.c -o thread_sched -pthread
./thread_scope
./thread_sched