package vu.algorithms;

/**
 * Created by vunguyen on 1/12/17.
 */
public class RatioJob extends Job implements Comparable<RatioJob> {
    private float score;

    public RatioJob() {

    }

    public RatioJob(int w, int l) {
        super(w, l);
        this.score = ((float) w) / l;
    }

    public float getScore() {
        return score;
    }

    @Override
    public int compareTo(RatioJob b) {
        if (this.getScore() > b.getScore()) {
            return -1;
        } else if (this.getScore() < b.getScore()) {
            return 1;
        }
        return 0;
    }
}
