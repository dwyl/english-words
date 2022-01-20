import java.util.*;
public class prt {
    prtnode root;
    public prtnode[] search(int k, String query){
        // Code to be implemented
        prq quePrq = new prq(k);
        quePrq.add(findnode(query));
        while(quePrq.que.size() > 0){
            prtnode pz = quePrq.first();
            quePrq.remove(pz);
            for (prtnode prtn : pz.arr) {
                if(prtn != null)
                quePrq.add(prtn);
            }
            if(pz.rank > 0)
            quePrq.add2(pz);
        }
        int j = 1;
        prtnode results[] = new prtnode[quePrq.que2.size()];
        for (prtnode px : quePrq.que2) {
            results[quePrq.que2.size()-j] = px;
            j++;
        }
        return results;
    }
    public prtnode[] search(String query){
        return search(Integer.MAX_VALUE, query);
    }
    public void insert(int rank, String keyword){
        key keyx = new key(keyword);
        ArrayList<prtnode> a = find(keyx);
        Collections.reverse(a);
        prtnode cur = a.get(0);
        if(cur.val.equals(keyx)){
            cur.val.end = true;
        } else {
            prtnode p = new prtnode(keyword, rank);
            int x = keyx.c[cur.val.len]-'a';
            prtnode pn = cur.arr[x];
            if(pn == null){
                cur.arr[x] = p;
            } else {
                int z = keyx.compare(pn.val);
                if(z == -1){
                    p.set(pn);
                    cur.arr[x] = p;
                } else {
                    key zl = new key(keyx, z);
                    prtnode q = new prtnode(zl);
                    q.set(pn);
                    cur.arr[x] = q;
                    q.set(p);
                }
            }
        }
        for (prtnode node : a) {
            node.update(rank);
        }
    }
    public ArrayList<prtnode> find(key query){
        ArrayList<prtnode> answer = new ArrayList<prtnode>();
        return root.find(query, answer);
    }
    public ArrayList<prtnode> find(String query){
        return find(new key(query));

    }
    public prtnode findnode(String q){
        ArrayList<prtnode> as = find(q);
        return as.get(as.size()-1);
    }
    
    public prt(){
        root = new prtnode();
    }
    public prt(String[] dictionary){
        root = new prtnode();
        for (int i = 0; i < dictionary.length; i++) {
            try {
                insert(dictionary.length-i, dictionary[i]);
                
            } catch (Exception e) {
                System.out.println("error");
                System.out.println(i);
                System.out.println(dictionary[i]);
                e.printStackTrace();
                key keyz = new key(dictionary[i]);
                int j = 0;
                for (prtnode prtnode : find(keyz)) {
                    System.out.println(j++);
                    System.out.println(prtnode.val.str);   
                }
                System.out.println("printed j");
                root.print();
            }
        }
    }  
    public void query(String q){
        for (prtnode p : find(q)){
            p.printself();
        }
    }
}

class prtnode {
    key val;
    prtnode arr[] = new prtnode[26];
    int rank;
    int maxrank;
    public ArrayList<prtnode> find(key query, ArrayList<prtnode> answer){
        answer.add(this);
        if(val.equals(query)){
            return answer;
        } else {
            prtnode p =  arr[query.c[val.len]-'a'];
            if(p == null){
                return answer;
            } else {
                if(p.val.lequals(query)){
                    return p.find(query, answer);
                } else {
                    return answer;
                }
            }
        }
    }
    public void update(int v){
        if (v > maxrank){
            maxrank = v;
        }
    }
    public void set(prtnode px){
        arr[px.val.c[val.len]-'a'] = px;
        update(px.maxrank);
    }
    public prtnode(String s, int r){
        rank = r;
        val = new key(s);
        maxrank = r;
    }
    public prtnode(key k){
        val = k;
        rank = 0;
        maxrank = 0;
    }
    public prtnode(){
        rank = 0;
        maxrank = 0;
        val = new key();
    }
    public void printself(){
        System.out.println(val.len);
        System.out.println(val.str);
        System.out.println(rank);
        System.out.println(maxrank);
        for (int i = 0; i < arr.length; i++) {
            System.out.print((char)(i+97));
            if(arr[i] != null) System.out.print("*");
            System.out.print(" ");
        }
        System.out.println();
        System.out.println(" - ");
    }
    public void print(){
        System.out.println("+-");
        if(this == null){
            System.out.println("null");

        } else {
            printself();
            int j = 0;
            for (prtnode prtnode : arr) {
                if(prtnode != null){
                    System.out.print("j is ");
                    System.out.print(j);
                    System.out.print(" ");
                    prtnode.print();
                }
                j++;
            }
        }
        System.out.print("--");
    }
}


class prtnodeComparator implements Comparator<prtnode>{
    public int compare(prtnode s1, prtnode s2) {
        if (s1.maxrank > s2.maxrank)
            return 1;
        else if (s1.maxrank < s2.maxrank)
            return -1;
        return 0;
        }
}
class prtnodeComparator2 implements Comparator<prtnode>{
    public int compare(prtnode s1, prtnode s2) {
        if (s1.rank > s2.rank)
            return 1;
        else if (s1.rank < s2.rank)
            return -1;
        return 0;
        }
}
class prq {
    SortedSet<prtnode> que = new TreeSet<prtnode>(new prtnodeComparator());
    SortedSet<prtnode> que2 = new TreeSet<prtnode>(new prtnodeComparator2());
    int max;
    public prq(int k){
        max = k;
    }
    public prq(){
        max = 10;
    }
    public void remove(){
        while(que.size() > max){
            prtnode p = que.first();
            que.remove(p);
        }
    }
    public void remove2(){
        while(que2.size() > max){
            prtnode p = que2.first();
            que2.remove(p);
        }
    }
    public void remove(prtnode p){
        que.remove(p);
    }
    public boolean add(prtnode p){
        if(que.size() == 0){
            que.add(p);
            return true;
        }
        que.add(p);
        if(que.size() > max){
            remove();
        }
        return true;
    }
    public boolean add2(prtnode p){
        if(que2.size() == 0){
            que2.add(p);
            // size2++;
            return true;
        }
        // if (que2.first().rank > p.rank){
        //     return false;
        // } else {
            que2.add(p);
            // size2++;
            if(que2.size() > max){
                remove2();
            }
            return true;
        // }
    }
    public prtnode first(){
        return que.last();
    }
}