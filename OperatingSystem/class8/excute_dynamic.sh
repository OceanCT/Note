# 编译生成目标文件，并把目标文件打包成动态库
# /* 生成目标文件 */
gcc -c -fPIC bill.c fred.c  
# /* 生成动态库 */
gcc -shared -o libfoo.so bill.o fred.o
# /* 编译时链接 libfoo.so 动态库 */
gcc main.c -o dlmain -L ./ -l foo
./dlmain
# % 如果运行可执行文件会出现一下错误提示
# errorwhile loading shared libraries: libfoo.so:cannot open shared object file: No suchfile or directory
# 就把生成的 libfoo.so 文件复制到 /usr/lib 目录下，重新运行。同时确认生成的可执行文件的文件大小，与静态库连接生成的可执行文件进行比较。
# sudo cplibfoo.so /usr/lib
# ./dlmain
