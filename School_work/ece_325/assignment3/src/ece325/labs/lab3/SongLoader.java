package ece325.labs.lab3;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/** 
 * Finish this class.
 */
public class SongLoader {
	/**
	 * Load a SongCollection from a file. Uses one or more Scanners to read the
	 * file, create Song objects and insert them into a SongCollection.
	 * 
	 * 
	 * The input is of the format: Songtitle; Instruments; Rating 
	 * Contribution;Guitar,Guitar,Drums;4.5
	 * 
	 * (see songratings.txt for the full input)
	 * 
	 * @param file
	 * @return the loaded SongCollection
	 */
	public static SongCollection loadSongs(String file) throws IOException{
		SongCollection song_collection = new SongCollection();
		BufferedReader in = null;

		in = new BufferedReader(new FileReader(file));

			String line; 
			while((line = in.readLine()) != null){
				try {
					song_collection.add(parseSong(line));
				} catch (InvalidSongFormatException e) {
					e.printStackTrace();
				}
			}
		
			in.close();


		return song_collection; 
		
		
	}

	/**
	 * Parse a Song object from the String and return it. If the String cannot be
	 * parsed into a Song, throw an InvalidSongFormatException.
	 * 
	 * @param songString
	 * @return
	 * @throws InvalidSongFormatException
	 */
	public static Song parseSong(String songString) throws InvalidSongFormatException {
		Scanner s = null;

    try {
		if (songString == null) throw new InvalidSongFormatException("Null input");
        s = new Scanner(songString);
        s.useDelimiter(";"); // divides each line into song, instruments, and rating

        // Expecting 3 parts

        if (!s.hasNext()) throw new InvalidSongFormatException("Missing song name field.");
        String songName = s.next().trim();

        if (!s.hasNext()) throw new InvalidSongFormatException("Missing instruments field.");
        ArrayList<String> instruments = parseInstrumentsList(s.next().trim());

		if (!s.hasNext()) throw new InvalidSongFormatException("Missing rating field.");
        float ratingValue = Float.parseFloat(s.next().trim());
        AverageRating new_rating = new AverageRating(ratingValue);

		
        return new Song(songName, instruments, new_rating);
    } 
    catch (NumberFormatException e) {
		
        throw new InvalidSongFormatException("Invalid rating format: " + e.getMessage());
    } 
    catch (Exception e) {
        throw new InvalidSongFormatException("Failed to parse song: " + e.getMessage());
    } 
    finally {
        if (s != null) {
            s.close();
        }
    }

	}

	/**
	 * Uses a scanner to parse the instruments string into an ArrayList of String
	 * objects. You can assume that the string comes in CSV (comma-separated-value)
	 * format, and that it is valid CSV (so no need to do error checking or account
	 * for issues with the data).
	 * 
	 * @param instruments
	 * @return an ArrayList with one String per parsed instrument
	 */
	public static ArrayList<String> parseInstrumentsList(String instruments) {
		ArrayList<String> instrumentsArrayList = new ArrayList<String>();
		String[] myArray = instruments.split(",");
		for (String s : myArray) {
  			instrumentsArrayList.add(s);
		}
		return instrumentsArrayList;
		
	}

	public static void main(String[] args) throws IOException {
		String file = "songratings.txt";
		System.out.println(SongLoader.loadSongs(file));
	}
}
