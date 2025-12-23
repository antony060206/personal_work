package ece325.lab.assignment5;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class TestSalary{
    
    Salary salary;

    @Test
    void testPay_NoBonus() {
        assertEquals(50.0, Salary.pay(100.0, 50.0, 0), 0.001);
    }

    @Test
    void testPay_WithBonus() {
        assertEquals(55.0, Salary.pay(100.0, 50.0, 10), 0.001);
    }

    @Test
    void testPay_ZeroSalaryZeroSnacks() {
        assertEquals(0.0, Salary.pay(0.0, 0.0, 0), 0.001);
    }

    @Test
    void testPay_Salarytest() {
        assertEquals(1100.0, Salary.pay(1000.0, 0.0, 10), 0.001);
    }

    @Test
    void testPay_SnacksEqualSalary() {
        assertEquals(0.0, Salary.pay(500.0, 500.0, 10), 0.001);
    }

    // null tests

    @Test
    void testNullSalaryThrows() {
        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> Salary.pay(null, 10.0, 5));
        System.out.println("MESSAGE = " + ex.getMessage());
    }

    @Test
    void testNullSnacksThrows() {
        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> Salary.pay(100.0, null, 5));
        System.out.println("MESSAGE = " + ex.getMessage());
    }

    @Test
    void testNullBonusThrows() {
        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> Salary.pay(100.0, 10.0, null));
        System.out.println("MESSAGE = " + ex.getMessage());
    }

    // range tests

    @Test
    void testSalaryBelowZeroThrows() {
        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> Salary.pay(-1.0, 0.0, 5));
        System.out.println("MESSAGE = " + ex.getMessage());
    }

    @Test
    void testSalaryAboveMaxThrows() {
        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> Salary.pay(1001.0, 0.0, 5));
        System.out.println("MESSAGE = " + ex.getMessage());
    }

    @Test
    void testBonusBelowZeroThrows() {
        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> Salary.pay(100.0, 10.0, -1));
        System.out.println("MESSAGE = " + ex.getMessage());
    }

    @Test
    void testBonusAboveTenThrows() {
        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> Salary.pay(100.0, 10.0, 11));
        System.out.println("MESSAGE = " + ex.getMessage());
    }

    @Test
    void testSnacksGreaterThanSalaryThrows() {
        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> Salary.pay(100.0, 200.0, 5));
        System.out.println("MESSAGE = " + ex.getMessage());
    }

    @Test
    void testNegativeSnacksThrows() {
        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> Salary.pay(100.0, -5.0, 5));
        System.out.println("MESSAGE = " + ex.getMessage());
    }
}