import java.io.FileInputStream;
import java.io.IOException;


//extend the words each day

public class Dictionary {
		public static String[] correct(string input){


//algorithm to make the best match for the words with probability ans suggest different things



}
		public static void main(String[] args) throws IOException{
			FileInputStream in = new FileInputStream("WORDS.txt");
			Node dic = new Node();
			Node traverser = dic;
			int c;
			while(true){
				c = in.read();
				if (c == -1) {
					break;
				}
				if (c == '\n') {
					traverser.isWord = true;
					traverser = dic;
					continue;
				}
				else{
					switch (c) {
					case 'a':
						traverser.a = new Node();
						traverser = traverser.a;
						break;

					case 'b':
						traverser.b = new Node();
						traverser = traverser.b;
						break;

					case 'c':
						traverser.c = new Node();
						traverser = traverser.c;
						break;
						
					case 'd':
						traverser.d = new Node();
						traverser = traverser.d;
						break;
						
					case 'e':
						traverser.e = new Node();
						traverser = traverser.e;
						break;
						
					case 'f':
						traverser.f = new Node();
						traverser = traverser.f;
						break;
						
					case 'g':
						traverser.g = new Node();
						traverser = traverser.g;
						break;
						
					case 'h':
						traverser.h = new Node();
						traverser = traverser.h;
						break;

					case 'i':
						traverser.i = new Node();
						traverser = traverser.i;
						break;

					case 'j':
						traverser.j = new Node();
						traverser = traverser.j;
						break;
						
					case 'k':
						traverser.k = new Node();
						traverser = traverser.k;
						break;
						
					case 'l':
						traverser.l = new Node();
						traverser = traverser.l;
						break;
						
					case 'm':
						traverser.m = new Node();
						traverser = traverser.m;
						break;
						
					case 'n':
						traverser.n = new Node();
						traverser = traverser.n;
						break;
						
					case 'o':
						traverser.o = new Node();
						traverser = traverser.o;
						break;

					case 'p':
						traverser.p = new Node();
						traverser = traverser.p;
						break;

					case 'q':
						traverser.q = new Node();
						traverser = traverser.q;
						break;
						
					case 'r':
						traverser.r = new Node();
						traverser = traverser.r;
						break;
						
					case 's':
						traverser.s = new Node();
						traverser = traverser.s;
						break;
						
					case 't':
						traverser.t = new Node();
						traverser = traverser.t;
						break;
						
					case 'u':
						traverser.u = new Node();
						traverser = traverser.u;
						break;
						
					case 'v':
						traverser.v = new Node();
						traverser = traverser.v;
						break;
						
					case 'w':
						traverser.w = new Node();
						traverser = traverser.w;
						break;
						
					case 'x':
						traverser.x = new Node();
						traverser = traverser.x;
						break;
						
					case 'y':
						traverser.y = new Node();
						traverser = traverser.y;
						break;
						
					case 'z':
						traverser.z = new Node();
						traverser = traverser.z;
						break;

					case '-':
						traverser.dash = new Node();
						traverser = traverser.dash;
						break;

					case '_':
						traverser.underline = new Node();
						traverser = traverser.underline;
						break;

					case '1':
						traverser.one = new Node();
						traverser = traverser.one;
						break;

					case '2':
						traverser.two = new Node();
						traverser = traverser.two;
						break;

					case '3':
						traverser.three = new Node();
						traverser = traverser.three;
						break;

					case '4':
						traverser.four = new Node();
						traverser = traverser.four;
						break;

					case '5':
						traverser.five = new Node();
						traverser = traverser.five;
						break;

					case '6':
						traverser.six = new Node();
						traverser = traverser.six;
						break;

					case '7':
						traverser.seven = new Node();
						traverser = traverser.seven;
						break;

					case '8':
						traverser.eight = new Node();
						traverser = traverser.eight;
						break;

					case '9':
						traverser.nine = new Node();
						traverser = traverser.nine;
						break;

					case '0':
						traverser.zero = new Node();
						traverser = traverser.zero;
						break;

					case '/':
						traverser.slash = new Node();
						traverser = traverser.slash;
						break;

					case '\'':
						traverser.prime = new Node();
						traverser = traverser.prime;
						break;

					case '.':
						traverser.dot = new Node();
						traverser = traverser.dot;
						break;

					case 'A':
						traverser.A = new Node();
						traverser = traverser.A;
						break;

					case 'B':
						traverser.B = new Node();
						traverser = traverser.B;
						break;

					case 'C':
						traverser.C = new Node();
						traverser = traverser.C;
						break;

					case 'D':
						traverser.D = new Node();
						traverser = traverser.D;
						break;

					case 'E':
						traverser.E = new Node();
						traverser = traverser.E;
						break;

					case 'F':
						traverser.F = new Node();
						traverser = traverser.F;
						break;

					case 'G':
						traverser.G = new Node();
						traverser = traverser.G;
						break;

					case 'H':
						traverser.H = new Node();
						traverser = traverser.H;
						break;

					case 'I':
						traverser.I = new Node();
						traverser = traverser.I;
						break;

					case 'J':
						traverser.J = new Node();
						traverser = traverser.J;
						break;

					case 'K':
						traverser.K = new Node();
						traverser = traverser.K;
						break;

					case 'L':
						traverser.L = new Node();
						traverser = traverser.L;
						break;

					case 'M':
						traverser.M = new Node();
						traverser = traverser.M;
						break;

					case 'N':
						traverser.N = new Node();
						traverser = traverser.N;
						break;

					case 'O':
						traverser.O = new Node();
						traverser = traverser.O;
						break;

					case 'P':
						traverser.P = new Node();
						traverser = traverser.P;
						break;

					case 'Q':
						traverser.Q = new Node();
						traverser = traverser.Q;
						break;

					case 'R':
						traverser.R = new Node();
						traverser = traverser.R;
						break;

					case 'S':
						traverser.S = new Node();
						traverser = traverser.S;
						break;

					case 'T':
						traverser.T = new Node();
						traverser = traverser.T;
						break;

					case 'U':
						traverser.U = new Node();
						traverser = traverser.U;
						break;

					case 'V':
						traverser.V = new Node();
						traverser = traverser.V;
						break;

					case 'W':
						traverser.W = new Node();
						traverser = traverser.W;
						break;

					case 'X':
						traverser.X = new Node();
						traverser = traverser.X;
						break;

					case 'Y':
						traverser.Z = new Node();
						traverser = traverser.Z;
						break;

					case 'Z':
						traverser.Z = new Node();
						traverser = traverser.Z;
						break;

					case ' ':
						traverser.space = new Node();
						traverser = traverser.space;
						break;

					default:
						break;
					}
				}
			}
		in.close();
		String input;

		//TODO: GET STRING INPUT; . PUT IT IN A STRING ARRAY, PROCCESS THEM AND FIND THE BEST MATCH.


		String[] output = correct(input);
		//System.out.println(dic.s.e.x.isWord);
		//System.out.println(dic.a.b.a.y.isWord);
		}
}
class Node{
	public Node a;
	public Node b;
	public Node c;
	public Node d;
	public Node e;
	public Node f;
	public Node g;
	public Node h;
	public Node i;
	public Node j;
	public Node k;
	public Node l;
	public Node m;
	public Node n;
	public Node o;
	public Node p;
	public Node q;
	public Node r;
	public Node s;
	public Node t;
	public Node u;
	public Node v;
	public Node w;
	public Node x;
	public Node y;
	public Node z;
	public Node A;
	public Node B;
	public Node C;
	public Node D;
	public Node E;
	public Node F;
	public Node G;
	public Node H;
	public Node I;
	public Node J;
	public Node K;
	public Node L;
	public Node M;
	public Node N;
	public Node O;
	public Node P;
	public Node Q;
	public Node R;
	public Node S;
	public Node T;
	public Node U;
	public Node V;
	public Node W;
	public Node X;
	public Node Y;
	public Node Z;
	public Node one;
	public Node two;
	public Node three;
	public Node four;
	public Node five;
	public Node six;
	public Node seven;
	public Node eight;
	public Node nine;
	public Node ten;
	public Node zero;
	public Node underline;
	public Node dash;
	public Node slash;
	public Node prime;
	public Node dot;
	public Node space;
	boolean isWord;
}
