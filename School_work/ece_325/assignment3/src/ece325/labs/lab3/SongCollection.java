package ece325.labs.lab3;

import java.util.ArrayList;

/** 
 * Finish this class.
 */
public class SongCollection {
	private ArrayList<Song> songs;

	public SongCollection() {
		this.songs = new ArrayList<>();

	}

	/**
	 * Add the song if it is not in the list yet, otherwise update the average
	 * rating of the song.
	 * 
	 * @param s
	 */
	public void add(Song s) {
		if (s == null) return;
		if(contains(s) == false){
			songs.add(s);
		}
		
	}

	public void remove(Song s) {
		if(contains(s) == true){
			songs.remove(s);
		}

		
	}

	public boolean contains(Song s) {

		//use a for loop to check if songs exist in the collection
		for (int i = 0; i < songs.size(); i++){
			if(s.equals(songs.get(i)) == true){
				(songs.get(i)).addRating(s.getRating().getAvgRating());
				return true;
			}
		}
		return false;
	}

	public Song getSong(int index) {
		return songs.get(index);
	}

	public int getNumberOfSongs() {
		return songs.size();
		
	}

	public ArrayList<Song> getSongs() {
		return songs;
		
	}

	public String toString() {
		String toRet = "[SongCollection: ";
		for (Song s : songs)
			toRet += "\n\t" + s + "; ";
		return toRet + "\n]";
	}
}
