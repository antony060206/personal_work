package ece325.labs.lab4;

import java.util.Comparator;

// finish this

public class SongComparator implements Comparator<Song> {
    @Override
    public int compare (Song s1, Song s2){
        if(s1.getAverageRating().getAvgRating() == s2.getAverageRating().getAvgRating()){//get votes if ratings are equal
            if(s1.getAverageRating().getVotes() > s2.getAverageRating().getVotes()){
                return -1;
            }
            else if(s1.getAverageRating().getVotes() < s2.getAverageRating().getVotes()){
                return 1;
            }
            else{
                return 0;
            }
        }
        else{
            if(s1.getAverageRating().getAvgRating() > s2.getAverageRating().getAvgRating()){
                return -1;
            }
            else if(s1.getAverageRating().getAvgRating() < s2.getAverageRating().getAvgRating()){
                return 1;
            }
            else{
                return 0;
            }
        }

    }
}