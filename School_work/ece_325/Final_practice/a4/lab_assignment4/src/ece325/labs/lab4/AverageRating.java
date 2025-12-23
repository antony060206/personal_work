package ece325.labs.lab4;

/** 
 * Finish this class.
 */
public class AverageRating {
	// not allowed to change anything after this (until the next marker which says you can add code again)
	private float avgRating;
	private int votes;
	
	public AverageRating(float rating, int votes) {
		this.avgRating = rating;
		this.votes = votes;
	}
		
	public float getAvgRating() {
		return avgRating;
	}
	
	public int getVotes() {
		return votes;
	}
	
	public String toString() {
		return "[AverageRating: " + avgRating + ", votes: " + votes + "]";
	}

	// You are allowed to make changes or add code after this line
}
