package edu.hitwh.test;

import edu.hitwh.dao.UserDao;
import edu.hitwh.domain.User;
import org.junit.Test;

public class UsersDaoTest {

    @Test
   public void testLogin(){
        User loginUser = new User();
        loginUser.setUsername("zhangsan");
        loginUser.setPassword("1234");
        UserDao dao = new UserDao();
        User user = dao.login(loginUser);
        System.out.println(user);
    }


}