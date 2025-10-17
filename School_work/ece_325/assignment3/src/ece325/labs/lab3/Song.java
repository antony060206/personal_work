package ece325.labs.lab3;

import java.util.ArrayList;
import java.util.Collections;

/** 
 * Finish this class.
 */
public class Song {
	private String title;
	private ArrayList<String> instruments;
	private AverageRating averageRating;
	

	public Song(){}

	public Song(String title, ArrayList<String> instruments, AverageRating rating) {
		//adds the titles of the songs 
		this.title = title;
		this.instruments = instruments;
		this.averageRating = rating;
		
	}
	
	/**
	 * Returns true if the title of and instruments used in the Songs are the same.
	 * Note that you don't have to include the AverageRating in this comparison (as it is not really related to the equality of the Song). 
	 */
	@Override
	public boolean equals(Object o) {
		
		//if already the same object /or not
		if(this == o) return true;
		if (o == null) return false;

		//check for same title
		Song other_song = (Song) o;
		if(this.title != other_song.title);

		//check for same instruments , where order doesnt matter
		ArrayList<String> a = new ArrayList<>(this.instruments);
    	ArrayList<String> b = new ArrayList<>(other_song.instruments);
    	Collections.sort(a);
    	Collections.sort(b);

    	return a.equals(b);
	}

	
	/**
	 * Returns true if the title of and instruments used in the Songs are the same.
	 * Note that you don't have to include the AverageRating in this comparison (as it is not really related to the equality of the Song). 
	 */
	public boolean equals(Song s) {
		return this.equals((Object) s);
	}
	
	public ArrayList<String> getInstruments(){
		return this.instruments;
		
	}
	
	public void addRating(float rating) {
		addRating(rating);
	}
	
	public AverageRating getRating() {
		return this.averageRating;
		
	}
	
	public String getTitle() {
		return this.title;
		
	}
	
	public String toString() {
		return "[Song: " + title + ", instruments: " + instruments + ", avg. rating: " + averageRating + "]"; 
	}
}
