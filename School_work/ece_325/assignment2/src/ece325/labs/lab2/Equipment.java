package ece325.labs.lab2;

/** 
 * Finish this class.
 */
public abstract class Equipment {
	public abstract String getType();

    @Override
    public String toString() {
        return getType();
    }
}
