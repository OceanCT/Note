# 动态加载
# 利用 libtest.c 源码,生成动态库，文件命名为 libtest.so, 并动态加载方式运行 dloading.c.
# 利用所提供的工具ranlib, 观察对动态加载 libtest 库之前、之后, 以及释放动态库之后的内存使用情况
# 对 slmain, dlmain, dloading 文件大小进行比较
gcc libtest.c -shared -fPIC -o libtest.so
gcc dloading.c -o dloading -ldl
./dloading