import java.util.Scanner;


public class main{
	
	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		long s = 0;
		if (n%2 == 0) s = n/2;
		else s = (-1)*(n/2 + 1);
		System.out.println(s);
		
	}
}