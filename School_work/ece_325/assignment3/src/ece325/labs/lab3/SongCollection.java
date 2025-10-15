package ece325.labs.lab3;

import java.util.ArrayList;

/** 
 * Finish this class.
 */
public class SongCollection {
	private ArrayList<Song> songs;

	public SongCollection() {
		
	}

	/**
	 * Add the song if it is not in the list yet, otherwise update the average
	 * rating of the song.
	 * 
	 * @param s
	 */
	public void add(Song s) {
		
	}

	public void remove(Song s) {
		
	}

	public boolean contains(Song s) {
		
	}

	public Song getSong(int index) {
		
	}

	public int getNumberOfSongs() {
		
	}

	public ArrayList<Song> getSongs() {
		
	}

	public String toString() {
		String toRet = "[SongCollection: ";
		for (Song s : songs)
			toRet += "\n\t" + s + "; ";
		return toRet + "\n]";
	}
}
