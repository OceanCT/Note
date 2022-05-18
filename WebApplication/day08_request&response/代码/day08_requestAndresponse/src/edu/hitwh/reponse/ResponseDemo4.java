package edu.hitwh.reponse;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/responseDemo4")
public class ResponseDemo4 extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        //获取流对象之前，流的默认编码：ISO-8859-1 设置为：utf-8
         response.setCharacterEncoding("utf-8");

        //告诉浏览器，服务器发送的消息体数据的编码。建议浏览器使用该编码解码
        //response.setHeader("content-type","text/html;charset=utf-8");

        //简单的形式，设置编码
        //response.setContentType("text/html;charset=utf-8");

        //1.获取字符输出流
        PrintWriter pw = response.getWriter();
        //2.输出数据
        //pw.write("<h1>hello response</h1>");
        pw.write("<h1>中国</h1>");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
