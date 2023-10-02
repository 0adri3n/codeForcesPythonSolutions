import java.util.Scanner;

// WRITED IN JAVA CUZ OF TIME LIMIT EXCEDEED ON TEST 7

public class main{
	
	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String av = "";
		int grp = 0;
		for(int i=0;i<n+1;i++){
			
			String t = sc.nextLine();
			if(t.equals(av)){
				;
			}
			else{
				grp=grp+=1;
				av = t;
			}
		}
		System.out.println(grp);
	}
}