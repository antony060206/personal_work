package ece325.labs.lab3;

/** 
 * Finish this class.
 */
public class AverageRating {
	private float avgRating;
	private int count;
	
	public AverageRating(float rating) {
		this.avgRating = rating;
		
	}
	
	/**
	 * Recomputes the average rating taking the new rating r into account.
	 * @param rating 
	 */
	public void addRating(float r) {
		count++;
		this.avgRating = (this.avgRating + r)/count;
	}
	
	public float getAvgRating() {
		return avgRating;
	}
	
	public String toString() {
		return "[AverageRating: " + avgRating + "]";
	}
}
