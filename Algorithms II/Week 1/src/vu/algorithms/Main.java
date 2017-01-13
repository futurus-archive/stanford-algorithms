package vu.algorithms;

import java.util.ArrayList;
import java.util.Collections;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static ArrayList<RatioJob> getJobs(String filename) throws IOException {
        File file = new File(filename); //for ex foo.txt
        Scanner sc = null;
        ArrayList<RatioJob> jobs = null;
        try {
            jobs = new ArrayList<RatioJob>();
            sc = new Scanner(file);
            int lines = sc.nextInt();

            for (int i = 0; i < lines; i++) {
                int w = sc.nextInt();
                int l = sc.nextInt();
                jobs.add(new RatioJob(w, l));
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (sc != null) {
                sc.close();
            }
            return jobs;
        }
    }

    public static void main(String[] args) {
        try {
            ArrayList<RatioJob> jobs = getJobs("data/jobs.txt");

            System.out.println("Before: ");
            for (int i = 0; i < 20; i++) {
                jobs.get(i).output();
            }

            Collections.sort(jobs);

            System.out.println("After: ");
            for (int i = 0; i < 200; i++) {
                jobs.get(i).output();
            }

            int length = 0;
            long sum = 0;
            for (int i = 0; i < 10000; i++) {
                RatioJob j = jobs.get(i);
                length += j.getLength();
                sum += j.getWeight() * length;
            }
            System.out.println(sum);
        } catch (IOException e) {}
        // D: 69119377652
        // R: 67311454237
    }
}
