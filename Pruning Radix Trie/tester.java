import java.util.*;
import java.io.*;
public class tester {
    public static void main(String[] args) {
        dictionary dict = new dictionary(1000);
        String[] diction = dict.getarray(1000);
        // String[] dict2 = dict.dictfromfile("alpha.txt");
        Vector<String> vs = new Vector<String>();
        try {
            FileInputStream fstream = new FileInputStream("/Users/dhruvtyagi/Documents/GitHub/english-words/Pruning Radix Trie/alpha.txt");
            Scanner s = new Scanner(fstream);
            while (s.hasNextLine()) vs.add(s.nextLine());
        } catch (FileNotFoundException e){
            System.out.println("File not found");
        }
        String[] answer = new String[vs.size()];
        int h = 0;
        for (String string : vs) {
            answer[h++] = string;
        }
        String cons = "aqwertyuiopasdfghjklzxcvbnm";
        prt prtrie = new prt(answer);
        String queryy = "carbon";
        int k = 10;
        for (int i = 0; i < queryy.length(); i++) {
            long starttime = System.currentTimeMillis();
            String query = queryy.substring(0, i+1);
            prtnode[] pq = prtrie.search(query);
            long stoptime1 = System.currentTimeMillis();
            prtnode[] pq1 = prtrie.search(k,query);
            long stoptime2 = System.currentTimeMillis();
            System.out.print("Query ");
            System.out.println(query);
            System.out.println("Total number of results");
            System.out.println(pq.length);
            System.out.println("Relevant Results:");
            System.out.println(pq1.length);
            for (int j = 0; j < pq1.length; j++) {
                prtnode str = pq[j];
                if(str != null)
                System.out.println(str.val.str);
            }
            System.out.println("end of results\nTime taken:-");
            
            // System.out.println(pq1.length);
            System.out.print(stoptime1-starttime);
            System.out.print(" ");
            System.out.println(stoptime2-stoptime1);
            System.out.println("_____________________________");
            
        }
        

       
    }
    
}
