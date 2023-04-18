package alphabet;

import java.util.*;

public class Alphabet {


    public static void main(String[] args) {



        Scanner scan = new Scanner(System.in);

        char[] input = scan.nextLine().toCharArray();
        scan.close();
        
        int[] arr = new int[input.length];
        for (int i : arr) {
            i = 1;
        }

        for (int i = input.length-1; i >= 0; i--) {

            char a = input[i];

            for (int j = i; j < input.length; j++) {
                char b = input[j];

                if(a<b && arr[j]+1>arr[i]) {
                    arr[i] = arr[j]+1;
                }
            }
        }

        int max = 0;
        for (int i : arr) {
            if(i > max) {
                max = i;
            }
        }

        System.out.println(26-max);

    }


}