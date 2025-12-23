package ece325.labs.lab2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

/** 
 * Finish this class.
 */
public class EquipmentInventory {

	/** The list of all your equipment objects */
	ArrayList<Equipment> inventory;
	/** The number of objects per type of equipment, grouped by the String description of a type */
	HashMap<String, Integer> inventoryCount;

	/** 
	 * Create an EquipmentInventory object by initializing the inventory and inventoryCount objects.
	 */
	public EquipmentInventory() {
		inventory = new ArrayList<Equipment>();
		inventoryCount = new HashMap<String, Integer>();
	}

	/**
	 * Add e to the inventory, and if the add is successful, increase the number of that equipment type in your inventoryCount.
	 * Make sure that you cannot accidentally add the same object twice.
	 * @param e The equipment object to add
	 */
	public void add(Equipment e) {
		if(e == null){
			return;
		}
		if(!inventory.contains(e)){
			inventory.add(e);
			increaseInventoryCount(e);

		}
	}

	/**
	 * Remove e from the inventory and if successful, decrease the number of that equipment type in your inventoryCount.
	 * @param e The equipment object to remove
	 */
	public void remove(Equipment e) {
		if(e == null){
			return;
		}
		if(inventory.contains(e)){
			inventory.remove(e);
			decreaseInventoryCount(e);
		}
	}

	/**
	 * Increase the inventoryCount for the type of equipment of e by 1.
	 * If it does not exist in the inventoryCount yet, add the type to the inventoryCount.
	 * Note: this method should be private, but to allow running unit tests on it (and make our lives easier when marking),
	 * we made this method protected. The method should never be called outside of the class. 	 
	 * @param e The type of equipment for which we want to increase the inventoryCount
	 */
	protected void increaseInventoryCount(Equipment e) {
		String key = e.toString();
		if(!inventoryCount.containsKey(key)){
			inventoryCount.put(key, 1);
		}
		else{
			inventoryCount.replace(key, inventoryCount.get(key)+1);
		}
	}

	/**
	 * Decrease the inventoryCount for the type of equipment of e by 1.
	 * If the inventoryCount for this type is now 0, remove the type from the inventoryCount.
	 * If the inventoryCount does not contain this type of equipment, do nothing.
	 * Note: this method should be private, but to allow running unit tests on it (and make our lives easier when marking),
	 * we made this method protected. The method should never be called outside of the class. 	 
	 * @param e The type of equipment for which we want to decrease the inventoryCount
	 */
	protected void decreaseInventoryCount(Equipment e) {
		//if have type
		String key = e.toString();
		if(inventoryCount.containsKey(key) && inventoryCount.get(key) > 0){
			inventoryCount.replace(key, inventoryCount.get(key)-1);
		}
		
		if (inventoryCount.get(key) == 0){
			inventoryCount.remove(key);
		}
		
	}

	/** 
	 * Return the number of times this type of equipment occurs in the inventory.
	 * If it doesn't occur in the inventory, return -1 (to indicate that something went wrong somewhere).
	 * @param e
	 * @return
	 */
	public Integer getInventoryCount(Equipment e) {
		if(e == null) return -1;

		String key = e.toString();

		if(key == "Chair" || key == "Stool" || key == "Guitar" || key == "Keyboard"){
			
		Integer v = inventoryCount.get(key);
    	return (v == null) ? -1 : v; 
		}
		return -1;
		
	}
	
	/**
	 * Return the String representation of the EquipmentInventory.
	 * It should look similarly to the following:
	 * [EquipmentInventory: Guitar: 3, Stool: 3, Chair: 1, Keyboard: 2]
	 * (after adding 3 guitars, 3 stools, 1 chair and 2 keyboards).
	 * The order in which the types are printed does not matter.
	 * @return the string representation of the EquipmentInventory
	 */
	public String toString() {
		String my_str = "[EquipmentInventory: ";

		int current_size = 0;
		for (Map.Entry<String, Integer> entry : inventoryCount.entrySet()){
			current_size++;
			String key = entry.getKey();
   			String value = Integer.toString(entry.getValue());
			if(current_size < inventoryCount.size()){
				my_str = my_str +  key + ": " + value + ", ";
			}
			else{
				my_str = my_str +  key + ": " + value;
			}
		}

		my_str = my_str + "]";

		return my_str;
	}

	public static void main(String[] args) {
		
		EquipmentInventory list_inventory = new EquipmentInventory();

		
		// 3 guitars
		Equipment g1 = new Guitar();
		Equipment g2 = new Guitar();
		Equipment g3 = new Guitar();

		// 2 keyboards
		Equipment k1 = new Keyboard();
		Equipment k2 = new Keyboard();

		// 3 stools
		Equipment s1 = new Stool();
		Equipment s2 = new Stool();
		Equipment s3 = new Stool();

		// 1 chair
		Equipment c1 = new Chair();

		//Add them to the inventory
		list_inventory.add(g1);
		list_inventory.add(g2);
		list_inventory.add(g3);
		list_inventory.add(k1);
		list_inventory.add(k2);
		list_inventory.add(s1);
		list_inventory.add(s2);
		list_inventory.add(s3);
		list_inventory.add(c1);

		// Print initial inventory
		System.out.println(list_inventory);

		//Remove one keyboard and one stool
		list_inventory.remove(k1);
		list_inventory.remove(s1);

		//print updated inventroy
		System.out.println(list_inventory);



	}
}
