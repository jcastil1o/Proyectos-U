package udemy.com.udemyprojects;
/**
 *
 * @author Jonathan
 */
public class TiposVariables 
{
    //Declarar metodo main
    public static void main(String [] args)
    {
        //Tipos de variables en Java
        //Declaracion de variables
        int VariableEntera = 10;
        /*variable entera
        Metodo de camello (mezclar mayusculas y minusculas)
        
        Para imprimir a pantalla: System.out.println("");
        */
        System.out.println("Mi variable entera: " + VariableEntera);
        //Cambiar el valor
        VariableEntera = 5;
        System.out.println("Nuevo valor de la variable: " + VariableEntera);
        
        /*
        Variable String
        Conjunto de cadena de caracteres
        
        Concatenar cadenas de texto "+"
        */
        String VariableString = "Hola Mundo";
        //Para visualizar tus variables, empieza a escribir y: "Ctrl + space bar"
        System.out.println("Mi variable string: " + VariableString);
        //Asignando nuevo valor
        VariableString = "Adios Mundo";
        System.out.println("Nuevo valor de la varialbe: " + VariableString);
        
        
        /*
        Utilizando indiferencia en Java
        
        Palabra reservada: var
        */
        
        var Variableint2 = 10;
        System.out.println("Mi variable entera: " + Variableint2);
        
        var VariableString2 = "Nueva cadena";
        /*
        Imprimir ultima variable declarada
        soutv + Tab
        */
        System.out.println("VariableString2 = " + VariableString2);
        
    }
    
}
