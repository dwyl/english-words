import java.util.*;
public class tester {
    public static void main(String[] args) {
        String[] diction = new String[1000];
        dictionary dict = new dictionary(1000);
        String cons = "aqwertyuiopasdfghjklzxcvbnm";
        // for (int i = 0; i < dictionary.length; i++) {
        //     char c1 = (char)((i%26)+97);
        //     char c2 = (char)(((i*23718)%26)+97);
        //     dictionary[i] = cons.replace(c1,c2);
        // }
        for (int i = 0; i < diction.length; i++) {
            diction[i] = dict.get(i);
        }    
        prt prtrie = new prt(diction);
        prtnode[] pq = prtrie.search(10, "a");
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
            prtnode str = pq[i];
            if(str != null)
            str.printself();
        }
        // prtrie.findnode("abdest").printself();
    }
    
}
