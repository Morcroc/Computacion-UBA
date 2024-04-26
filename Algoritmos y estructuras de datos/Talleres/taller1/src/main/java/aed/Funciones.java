package aed;

class Funciones {
    int cuadrado(int x) {
        int res = x * x;
        return res;
    }

    double distancia(double x, double y) {
        double res = Math.sqrt(x*x + y*y);
        return res;
    }

    boolean esPar(int n) {
        boolean res = (n % 2 == 0);
        return res;
    }

    boolean esBisiesto(int n) {
        boolean res = (n % 4 == 0 && n % 100 != 0) || n % 400 == 0;
        return res;
    }

    int factorialIterativo(int n) {
        int res = 1;
        for (int i = 1; i <= n; i++) {
            res *= i;
        }
        return res;
    }

    int factorialRecursivo(int n) {
        int res;
        if (n == 0 || n == 1) {
            res = 1;
        }
        else{
            res = n * factorialRecursivo(n-1);
        }
        return res;
    }

    boolean divideA(int d, int n){
        boolean res = (n % d) == 0;
        return res;
    }

    
    boolean esPrimo(int n) {
        boolean res = n > 1;
        int i = 2;
        while (res && i < n) {
            res = !divideA(i, n);
            i++;
        }
        return res;
    }

    int sumatoria(int[] numeros) {
        int res = 0;
        for (int i : numeros) {
            res += i;
        }
        return res;
    }

    int busqueda(int[] numeros, int buscado) {
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] == buscado) {
                return i;
            }
        }
        return -1;
    }

    boolean tienePrimo(int[] numeros) {
        for (int i : numeros) {
            if (esPrimo(i)) {
                return true;
            }
        }
        return false;
    }

    boolean todosPares(int[] numeros) {
        for (int i : numeros) {
            if(!divideA(2, i)){
                return false;
            }
        }
        return true;
    }

    boolean esPrefijo(String s1, String s2) {
        boolean res = true;
        if(s1.length() <= s2.length()){
            int i = 0;
            while (i < s1.length() && res) {
                res = (s1.charAt(i) == s2.charAt(i));
                i++;
            }
            return res;
        }
        return false;
    }

    boolean esSufijo(String s1, String s2) {
        return esPrefijo(invertirString(s1), invertirString(s2));
    }

    String invertirString(String s){
        String nuevoString = "";
        for (int i = 1; i <= s.length(); i++) {
            nuevoString += s.charAt(s.length() - i);
        }
        return nuevoString;
    }
}
