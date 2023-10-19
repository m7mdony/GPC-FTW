import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.io.*;

public class main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("dance.in"));
        FileWriter file = new FileWriter(new File("dance.answer"));
        String result = "";
        int nOfCases = scan.nextInt();

        for (int i = 0; i < nOfCases; i++) {
            int numberOfDancers = scan.nextInt();
            int numberOfSensors = scan.nextInt();
            int K = scan.nextInt();
            ArrayList<Double[]> dancers = new ArrayList<Double[]>();
            ArrayList<Double[]> sensors = new ArrayList<Double[]>();

            for (double j = 0; j < numberOfDancers; j++) {
                double x = scan.nextDouble();
                double y = scan.nextDouble();
                double constantFactor = scan.nextDouble();

                dancers.add(new Double[] { x, y, constantFactor });
            }

            for (int j = 0; j < numberOfSensors; j++) {
                double x = scan.nextDouble();
                double y = scan.nextDouble();
                double rangeOfTheSensor = scan.nextDouble();

                sensors.add(new Double[] { x, y, rangeOfTheSensor });
            }

            long totalEnergy = 0;

            for(Double[] dancer: dancers) {
                int nOfSensors = 0;
                for(Double[] sensor: sensors) {
                    if(isIntersect(dancer, sensor)) {
                        //System.out.println(Arrays.toString(dancer) + " Intersects with " + Arrays.toString(sensor));
                        nOfSensors++;
                    }
                }
                
                totalEnergy += calculateEnergy(K, dancer[2], nOfSensors) * nOfSensors;
            }

            result+= (i + 1) + ". " + totalEnergy +".00" + "\n";
        }

        file.write(result);
        scan.close();
        file.close();
    }

    public static double calculateEnergy(double Kconstant, double energyExpected, double numberOfSensors) {
        if(numberOfSensors == 0) return 0;
        return (double) (Kconstant * energyExpected) / numberOfSensors;
    }

    public static boolean isIntersect(Double[] dancer, Double[] sensor) {
        if(calcDistance(dancer[0], dancer[1], sensor[0], sensor[1]) <= sensor[2]) {
            return true;
        } else {
            return false;
        }
    }

    public static double calcDistance(double x1, double y1, double x2, double y2) {
        return Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));
    }

    public static void printArrayList(ArrayList<int[]> array) {
        for (int i = 0; i < array.size(); i++) {
            int[] arr = array.get(i);
            System.out.println(Arrays.toString(arr));
        }
    }
}
