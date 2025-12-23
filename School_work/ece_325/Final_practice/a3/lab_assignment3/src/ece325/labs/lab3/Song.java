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
	
	public Song(String title, ArrayList<String> instruments, AverageRating rating) {
		//adds the titles and paremeters of the songs 
		if (title == null) title = "";
        this.title = title;
        this.instruments = new ArrayList<>();
        if (instruments != null) {
            for (String s : instruments) {
                if (s != null) this.instruments.add(s.trim());
            }
        }

		//sort the instruments based on 
		Collections.sort(this.instruments, String.CASE_INSENSITIVE_ORDER);
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
		if(o == null) return false;
		if(!(o instanceof Song )) return false;

		//check for same title
		Song other_song = (Song) o;
		if(!this.title.equals(other_song.title)) return false;

		//check for same instruments , where order doesnt matter
		return this.instruments.equals(other_song.instruments);
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
		averageRating.addRating(rating);
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
