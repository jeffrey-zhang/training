import java.util.Scanner;

public class exam{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("请问需要打印多少个三角形：");
        //输入
        int answer = scanner.nextInt();
        if (answer > 0){
            for (int i = 1; i <= answer; i++) {
                method();
           }
        }else {
            System.out.println("错误输入");
        }
        
    }
    //打印三角形
    public static void method() {
     for (int i = 1; i <= 5; i++) {

            for (int j = 1; j <= 5 - i; j++) {
                System.out.print(" ");
            }

            for (int k = 1; k <= 2 * i - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
        
    }

}


