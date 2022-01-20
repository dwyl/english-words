import java.util.*;
public class tester {
    public static void main(String[] args) {
        dictionary dict = new dictionary(1000);
        String[] diction = dict.getarray(1000);
        String cons = "aqwertyuiopasdfghjklzxcvbnm";
        prt prtrie = new prt(diction);
        prtnode[] pq = prtrie.search("abs");
        System.out.println("Number of Results:");
        System.out.println(pq.length);
        for (int i = 0; i < pq.length; i++) {
            prtnode str = pq[i];
            if(str != null)
            System.out.println(str.val.str);
        }
    }
    
}
