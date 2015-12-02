package com.company;

import java.math.BigInteger;

public class ModSquareMatrix {

    long[][] data;
    private final long modulo;

    public ModSquareMatrix(long[][] data, long modulo) {
        this.data = data;
        this.modulo = modulo;
    }

    ModSquareMatrix mult(ModSquareMatrix A) {
        long[][] C = new long[data.length][data.length];
        long[][] B = A.data;
        for (int i = 0; i < data.length; i++) {
            for (int j = 0; j < data.length; j++) {
                for (int k = 0; k < data.length; k++) {
                    C[i][j] += (((data[i][k] % modulo) * (B[k][j]) % modulo) % modulo);
                }
                C[i][j] %= modulo;
            }
        }

        return new ModSquareMatrix(C, modulo);
    }

    public static ModSquareMatrix square(ModSquareMatrix A) {
        return A.mult(A);
    }

    public ModSquareMatrix pow(long exponent) {
        if (exponent == 0) {
            return identity(data.length, modulo);
        }
        if (exponent == 1) {
            return this;
        }
        if (exponent % 2 == 0) {
            return square(this.pow(exponent / 2));
        } else {
            return square(this.pow(exponent / 2)).mult(this);
        }
    }

    // Iterative approach To avoid stack overflow when log(exponent) is too big
    public ModSquareMatrix pow(BigInteger exponent) {
        byte[] exponentBytes = exponent.toByteArray();
        ModSquareMatrix result = identity(data.length, modulo);
        for (byte exponentByte : exponentBytes) {
            result = result.pow(256).mult(this.pow(exponentByte & 0xFF));
        }
        return result;
    }

    public static ModSquareMatrix identity(int size, long modulo) {
        long[][] identity = new long[size][size];
        for (int i = 0; i< size;i++) {
            identity[i][i] = 1;
        }
        return new ModSquareMatrix(identity, modulo);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (long[] row : data) {
            sb.append("| ");
            for (long val : row) {
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
