import java.util.Scanner;
import java.util.ArrayList; 
import java.util.Scanner; 
import java.util.stream.Collectors; 
import java.util.stream.Stream; 

public class main{
	
	public static void main(String[] args){

		Scanner sc = new Scanner(System.in);
		int l = sc.nextInt();
    
        for(int j=0; j<l;j++){
            Scanner scanner = new Scanner(System.in);
            scanner.useDelimiter(" ");
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            int n = scanner.nextInt();

            int i=n;
            boolean f = false;
            while(f == false){
                if(i%x==y){
                    f = true;
                }
                else{
                    i-=1;
                }
            }
            
            System.out.println(i);
            jcdInput.close(); 

        }


    }

}