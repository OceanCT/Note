# 编译生成目标文件，并把目标文件打包成静态库，命令如下
gcc -c fred.c bill.c
ls *.o
ar crv libfoo.a bill.o fred.o
ranlib libfoo.a
# 通过链接静态库生成可执行文件-静态链接
gcc -c main.c
gcc -o slmain main.o libfoo.a
./slmain
# 利用目标文件生成可执行文件
gcc -c main.c
gcc -o main main.o bill.o
./main
# 比较可执行文件 slmain 文件和 main 文件的大小
ls *main -lh >> out
