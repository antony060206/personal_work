package ece325.lab.assignment5;

public class Salary {
	
	/**
	 * Returns the amount of pay a band member will get (in dollars). This amount is
	 * computed by deducting the amount spent on snacks from the base salary, and
	 * then computing and adding the bonus (if any) over that amount. So, if a band
	 * member earned 100 dollars, spent 50 on snacks, and earned a bonus of 10 (%),
	 * their total pay will be 55 dollars.
	 * 
	 * Note: The current implementation of this method is extremely buggy and can
	 * easily be abused by anyone.
	 * 
	 * @param salary       The base salary earned by this band member during this
	 *                     salary period (in dollars).
	 * @param snacksAmount The total amount spent by this band member on snacks
	 *                     during this salary period (in dollars).
	 * @param bonus        The bonus percentage that the band member earned this
	 *                     salary period (in percentage).
	 * @return the amount of pay a band member will get (in dollars)
	 */
	public static Double pay(Double salary, Double snacksAmount, Integer bonus) {

		//if salary, snackamount or bonus are null
		if(salary == null || snacksAmount == null || bonus == null){
			throw new IllegalArgumentException("salary, snacksAmount or bonus is null dumdum.");
		}

		double s = salary.doubleValue();
		double snacks = snacksAmount.doubleValue();
		int b = bonus.intValue();

		//if base salary exceeds maximum of 1000 or below 0
		if(s < 0 || s > 1000){
			throw new IllegalArgumentException("Salary has to be within 0-1000 dumdum");
		}

		//if bonus is about 10% or below 0% 
		if(b < 0 || b > 10){
			throw new IllegalArgumentException("Bonus has to be within 0-10 dumdum");
		}

		//if snacks is below 0 
		if(snacks < 0){
			throw new IllegalArgumentException("Bro tryna buy food that has negative cost. Salary needs to be bigger than 0");
		}

		//if more money is spent on snacks than basesalary
		if(snacks > s){
			throw new IllegalArgumentException("How you tryna spend more money on food than u earn? dumdum");
		}
		
		double bonusFraction = b / 100.0;
		double base = s - snacks;
		
		return (base) + ((base) * bonusFraction);
	}
}
