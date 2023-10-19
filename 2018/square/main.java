// 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
// 8 1 2 3 4 5 6 7 9 10 11 12 13 14 15
// 8 1 15 3 4 5 6 7 9 10 11 12 13 14 2
// 8 1 15 10 4 5 6 7 9 3 11 12 13 14 2

import java.io.FileWriter;
import java.util.Arrays;
import java.util.Scanner;
import java.io.*;

public class main2 {
    public static void main(String[] args) throws IOException{
        Scanner scan = new Scanner(new File("square.in"));
        FileWriter file = new FileWriter(new File("square.answer"));
        String result = "";
        int line = scan.nextInt();

        while (line != 0) {
            int[] tempArr = new int[line];
            for (int i = 0; i < tempArr.length; i++) {
                tempArr[i] = scan.nextInt();
            }
            int[] resultArr = sort(tempArr);

            if (resultArr.length == 0) {
                result += "No solution";
            } else {
                result += Arrays.toString(resultArr);
            }

            result += "\n";

            line = scan.nextInt();
        }

        file.write(result);
        file.close();
        scan.close();
    }

    public static int[] sort(int[] array) {
        boolean hasSorted = false;

        for (int i = 0; i < array.length; i++) {
            boolean isPerfectSquare = false;
            for (int j = i + 1; j < array.length; j++) {
                if (checkIfPerfectSquare(array[i], array[j]) && i != j) {
                    swapValues(array, i + 1, j);
                    isPerfectSquare = true;
                    hasSorted = true;
                }
            }

            if (!isPerfectSquare) {
                break;
            }
        }

        int[] newArray;

        if (hasSorted) {
            newArray = new int[array.length];
            newArray[0] = array[array.length - 1];
            for (int i = 1; i < newArray.length; i++) {
                newArray[i] = array[i - 1];
            }
        } else {
            newArray = new int[0];
        }

        return newArray;
    }

    public static boolean checkIfPerfectSquare(int num1, int num2) {
        double calculatedNumber = Math.sqrt(num1 + num2);
        if (calculatedNumber == (int) calculatedNumber) {
            return true;
        } else {
            return false;
        }
    }

    public static void swapValues(int[] arr, int index1, int index2) {
        int tempvalue = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = tempvalue;
    }
}
