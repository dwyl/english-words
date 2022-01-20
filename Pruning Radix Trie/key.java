public class key {
    String str;
    int len = 0;
    char c[];
    public key(String s){
        str = s;
        c = new char[s.length()];
        len = s.length();
        for (int i = 0; i < len; i++) {
            c[i] = s.charAt(i);
        }
        end = true;
    }
    public key(){
        str = "";
        len = 0;
        end = true;
    }
    public key(key k, int l){
        len = l;
        c = new char[len];
        for (int i = 0; i < len; i++) {
            c[i] = k.c[i];
        }
        str = new String(c);
        end = false;
    }
    boolean end;
    public int compare(key k){
        if(k == null || this == null || len == 0 || k.len == 0){
            return -1;
        }
        int i = 0;
        while(c[i] == k.c[i]){
            i++;
            if(i == len || i == k.len){
                i = -1;
                break;
            }
        }
        return i;
    }
    public boolean equals(key k){
        return (compare(k) == -1)&(len == k.len);
    }
    public boolean lequals(key k){
        return (compare(k) == -1)&(len <=k.len);
    }
}

