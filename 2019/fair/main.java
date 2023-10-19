import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("fair.in"));
        FileWriter file = new FileWriter("fair.answer");
        String result = "";
        int line = scan.nextInt();

        while (line != 0) {
            int n = scan.nextInt();
            String value = "";

            for (int i = 0; i < line; i++) {
                value += scan.next();
            }

            ArrayList<String> combinations = generateAllCombinations(value, n);
            System.out.println(combinations);

            int minValue = Integer.MAX_VALUE;
            for (int i = 0; i < combinations.size(); i++) {
                for (int j = 0; j < combinations.size(); j++) {
                    if (checkIfRelated(combinations.get(i), combinations.get(j))) {
                        System.out.println(combinations.get(i) + " " + combinations.get(j));
                        minValue = Math.min(
                                Math.abs(Integer.parseInt(combinations.get(i)) - Integer.parseInt(combinations.get(j))),
                                minValue);
                        if (minValue == 1) {
                            break;
                        }
                    }

                }
                if (minValue == 1) {
                    break;
                }
            }

            result += minValue;
            result += "\n";
            System.out.println(result);

            line = scan.nextInt();
        }

        file.write(result);
        file.close();
        scan.close();
    }

    public static boolean checkIfRelated(String s1, String s2) {
        for (int i = 0; i < s1.length(); i++) {
            if (s2.contains(s1.charAt(i) + "")) {
                return false;
            }
        }

        return true;
    }

    public static ArrayList<String> generateAllCombinations(String characters, int n) {
        ArrayList<String> combinations = new ArrayList<>();
        generateCombinationsRecursive(n, characters, "", 0, combinations);
        return combinations;
    }

    public static void generateCombinationsRecursive(int k, String characters, String currentCombination,
            int startIndex, ArrayList<String> combinations) {
        if (k == 0) {
            combinations.add(currentCombination);
            return;
        }

        for (int i = startIndex; i < characters.length(); i++) {
            char character = characters.charAt(i);

            // Remove character from available options
            String remainingCharacters = characters.substring(0, i) + characters.substring(i + 1);

            generateCombinationsRecursive(k - 1, remainingCharacters, currentCombination + character, i, combinations);
        }
    }

}  

// 1234
// 1
