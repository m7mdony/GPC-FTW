import java.util.HashMap;
import java.util.Scanner;
import java.io.*;

public class main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("chain.in"));
        FileWriter file = new FileWriter(new File("chain.answer"));
        String result = "";
        int nOfTestCases = scan.nextInt();

        while (nOfTestCases != 0) {
            String input = scan.next();
            int nOfMap = scan.nextInt();
            HashMap<String, Integer> map = new HashMap<String, Integer>();
            HashMap<String, Integer> memo = new HashMap<String, Integer>();
            for (int j = 0; j < nOfMap; j++) {
                String rd = scan.next();
                int rdnum = scan.nextInt();
                map.put(rd, rdnum);
            }
            System.out.println(map);

            result += calculate(input, map, 0, memo);
            result += "\n";
            // System.out.println(result);

            nOfTestCases = scan.nextInt();
        }

        file.write(result);
        file.close();
        scan.close();
    }

    public static int calculate(String input, HashMap<String, Integer> array, int score,
            HashMap<String, Integer> memo) {
        if (input.length() == 0) {
            return score;
        } else if (memo.containsKey(input)) {
            return memo.get(input);
        } else {
            int maxValue = Integer.MIN_VALUE;

            for (String value : array.keySet()) {
                int num = 0;

                if (input.contains(value)) {
                    num = calculate(input.replaceFirst(value, ""), array, score + array.get(value), memo);
                } else if (input.contains(flipString(value))) {
                    num = calculate(input.replaceFirst(flipString(value), ""), array, score + array.get(value), memo);
                }

                maxValue = Math.max(maxValue, num);
            }

            if (!memo.containsKey(input)) {
                memo.put(input, score);
            }

            return maxValue;
        }
    }

    public static String flipString(String input) {
        String result = "";

        for (int i = input.length() - 1; i >= 0; i--) {
            result += input.charAt(i);
        }

        return result;
    }
}
