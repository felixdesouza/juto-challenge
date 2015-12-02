package com.company;

import java.math.BigInteger;

import static java.math.BigInteger.ONE;
import static java.math.BigInteger.ZERO;

public class Main {
    public static final BigInteger TWO = BigInteger.valueOf(2);
    private static final BigInteger[][] bigIntData = new BigInteger[][]{
            {ZERO, ONE, ZERO},
            {ZERO, ZERO, ONE},
            {TWO, ZERO, ONE}
    };

    private static final long[][] longGenerator = new long[][] {
            {0,1,0},
            {0,0,1},
            {2,0,1}
    };
    private static final long MODULO = 1000000000L;

    public static void main(String[] args) {
        SquareMatrix A = new SquareMatrix(bigIntData);
        System.out.println("Created initial matrix A");

        // B = generator matrix for our recurrence relation
        SquareMatrix B = A.pow(5000000);
        System.out.println("B = A^(5*10^6) ");

        // f(5 * 10^6)
        BigInteger stage1 = B.data[0][2];
        //BigInteger stage1 = BigInteger.valueOf(10000);
        System.out.println("n = B[0][2]");

        // C[0,2] = f(f(5 * 10^6)) % 10^9
        ModSquareMatrix C = new ModSquareMatrix(longGenerator, MODULO);
        System.out.println("Created initial mod matrix C");
        ModSquareMatrix stage2 = C.pow(stage1);
        System.out.println("C = A^n");
        System.out.println();
        System.out.println(stage2);
        System.out.println();
        System.out.println("Result = " + stage2.data[0][2]);
    }

}
