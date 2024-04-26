package aed;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class CoberturaTests {
    Cobertura cobertura = new Cobertura();

    @Test
    void testFizzBuzz() {
        assertEquals("FizzBuzz",cobertura.fizzBuzz(15));
        assertEquals("Fizz",cobertura.fizzBuzz(9));
        assertEquals("Buzz",cobertura.fizzBuzz(20));
        assertEquals("8",cobertura.fizzBuzz(8));
    }

    @Test
    void testNumeroCombinatorio() {
        assertEquals(1, cobertura.numeroCombinatorio(0, 0));;
        assertEquals(1, cobertura.numeroCombinatorio(1, 0));;
        assertEquals(1, cobertura.numeroCombinatorio(1, 1));;
        assertEquals(0, cobertura.numeroCombinatorio(1, 2));;
        assertEquals(2, cobertura.numeroCombinatorio(2, 1));;
        assertEquals(6, cobertura.numeroCombinatorio(4, 2));;
    }

    @Test
    void testRepeticionesConsecutivas() {
        assertEquals(1, cobertura.repeticionesConsecutivas(new int[]{1,2,3,4}));
        assertEquals(5, cobertura.repeticionesConsecutivas(new int[]{1,2,3,4,4,4,4,4}));
        assertEquals(2, cobertura.repeticionesConsecutivas(new int[]{1,2,2,3,3,4}));
        assertEquals(0, cobertura.repeticionesConsecutivas(new int[0]));
        assertEquals(0, cobertura.repeticionesConsecutivas(new int[]{1}));
    }
}
