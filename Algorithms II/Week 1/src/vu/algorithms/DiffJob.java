package vu.algorithms;

/**
 * Created by vunguyen on 1/12/17.
 */
public class DiffJob extends Job implements Comparable<DiffJob> {
    private float score;

    public DiffJob() {

    }

    public DiffJob(int w, int l) {
        super(w, l);
        this.score = w - l;
    }

    public float getScore() {
        return score;
    }

    @Override
    public int compareTo(DiffJob b) {
        if (this.getScore() == b.getScore()) {
            return -(this.getWeight() - b.getWeight());
        } else {
            return (int) -(this.getScore() - b.getScore());
        }
    }
}
