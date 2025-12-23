package ece325.labs.lab2;

/** 
 * Finish this class.
 */
public abstract class Equipment {
    
    public abstract String currentclass();

    @Override 
    public String toString(){
        return currentclass();

    }
}
