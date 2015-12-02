package com.company;

import java.math.BigInteger;

import static java.math.BigInteger.ZERO;

public class SquareMatrix {

    BigInteger[][] data;

    public SquareMatrix(BigInteger[][] data) {
        this.data = data;
    }

    public SquareMatrix mult(SquareMatrix BMatrix) {
        BigInteger[][] C = new BigInteger[data.length][data.length];
        BigInteger[][] B = BMatrix.data;
        for (int i = 0; i < data.length; i++) {
            for (int j = 0; j < data.length; j++) {
                C[i][j] = ZERO;
                for (int k = 0; k < data.length; k++) {
                    C[i][j] = C[i][j].add(data[i][k].multiply(B[k][j]));
                }
            }
        }

        return new SquareMatrix(C);
    }

    public static SquareMatrix square(SquareMatrix A) {
        return A.mult(A);
    }

    public SquareMatrix pow(long exponent) {
        if (exponent == 1) {
            return this;
        }
        if (exponent % 2 == 0) {
            return square(this.pow(exponent / 2));
        } else {
            return square(this.pow(exponent / 2)).mult(this);
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (BigInteger[] row : data) {
            sb.append("| ");
            for (BigInteger val : row) {
                sb.append(val);
                sb.append(" | ");
            }
            sb.append("\n");
            sb.append("---");
            sb.append("\n");
        }

        return sb.toString();
    }
}
