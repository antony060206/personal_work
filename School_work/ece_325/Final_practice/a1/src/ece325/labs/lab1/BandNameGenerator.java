package ece325.labs.lab1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Random;

public class BandNameGenerator {
	String[] adjectives;
	String[] nouns;
	
	boolean adjectivesLoaded = false;
	boolean nounsLoaded = false;
	
	String adjectivesFile;
	String nounsFile;
	
	public BandNameGenerator(String adjectivesFile, String nounsFile) {
		this.adjectivesFile = adjectivesFile;
		this.nounsFile = nounsFile;		
	}
	
	
	/**
	 * Load the adjectives file and initialize that part of the generator.
	 */
	public void loadAdjectives() {
		adjectives = loadTxt(adjectivesFile);

	}
	
	/**
	 * Load the nouns file and initialize that part of the generator.
	 */
	public void loadNouns() {
		nouns = loadTxt(nounsFile);

	}
			
	/**
	 * Return a string that capitalizes the first letter of s and lowercases the rest. So for example,
	 * 'cat' becomes 'Cat', and 'CHUBBY CAt' becomes 'Chubby cat'. Read the assignment carefully and think about how 
	 * to implement this part of the code.
	 * 
	 * @param s
	 * @return
	 */
	public String capitalizeFirst(String s) {
		return s.substring(0, 1).toUpperCase() + s.substring(1).toLowerCase();
		
	}
	
	
	/** 
	 * Generate a name for your band consisting of two adjectives and one noun.
	 * Make sure to return "UNINITIALIZED" if the band name generator is not initialized correctly yet.
	 * @return the generated name or "UNINITIALIZED"
	 */
	public String generateName() {
		
		Random r = new Random();
		int r1 = 0;
		int r2 = 0;
		int r3 = 0;
		
		
		r1 = r.nextInt(adjectives.length);
		r2 = r.nextInt(adjectives.length);
		r3 = r.nextInt(nouns.length);
		
		


		String first_adj = adjectives[r1];
		String second_adj = adjectives[r2];;
		String third_noun = nouns[r3];;

		

		return capitalizeFirst(first_adj + " " + second_adj + " " + third_noun);
			
	}

	
	/**
	 * This method loads a text file into a String array. It assumes the number of 
	 * lines in the file is on the first line of the file itself.
	 * 
	 * Note: you are not allowed to make changes to this method. You can use this method for 
	 * loading text files in the other lab and course assignments as well.
	 * 
	 * @param file
	 * @return
	 */
	private String[] loadTxt(String file) {
		String[] data = new String[0];
		BufferedReader in = null;
		
		try { 
			in = new BufferedReader(new FileReader(file));
			String line;
			int i = 0;
			int totalLines = Integer.parseInt(in.readLine());
			data = new String[totalLines];
			while((line = in.readLine()) != null)
			{
				data[i] = line;
				i++;
				
			}
		} catch (Exception e) {
			System.err.println("Problem while reading file: " + file);
			e.printStackTrace();			
		}
		finally {
			if(in != null) { 
				try {
					in.close();
				} catch (IOException e) {
					System.err.println("Problem closing file: " + file);
					e.printStackTrace();
				} 
			}
		}
		return data;
	}
	
	/**
	 * Returns the list of adjectives.
	 * @return
	 */
	public String[] getAdjectives() {
		return adjectives;
	}
	
	/**
	 * Returns the list of nouns.
	 * @return
	 */
	public String[] getNouns() {
		return nouns;
	}
	
	public static void main(String[] args) {
		// create a BandNameGenerator and initialize it
		BandNameGenerator generator = new BandNameGenerator("adjectives.txt", "nouns.txt");

		generator.loadAdjectives();
		generator.loadNouns();
		// generate and print 20 names for your band
		for (int i = 0; i < 20; i++){
			System.out.println(generator.generateName());
		}
		
		
		
	}

}
