package vu.algorithms;

/**
 * Created by vunguyen on 1/12/17.
 */
public abstract class Job {
    private int weight;
    private int length;

    public Job() {
    }

    public Job(int w, int l) {
        weight = w;
        length = l;
    }

    public int getWeight() {
        return weight;
    }

    public int getLength() {
        return length;
    }

    public void setWeight(int w) {
        weight = w;
    }

    public void setLength(int l) {
        length = l;
    }

    public void output() {
        System.out.println("w: " + weight + ", l: " + length);
    }
    public abstract float getScore();
}
