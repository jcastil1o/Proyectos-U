public class Arreglo2
    //Clase Arreglo2
{
    static int[] myArray = { 1, 2, 2, 4, 5, 6, 7, 8, 8, 8 };
    public static void Main(string[] args)
    {
        //Metodo Main

        //Variables para el programa, longitud, contador del arrerglo
        int largoNum = myArray[0];
        int largo = 1;
        int cNum = myArray[0];
        int c = 1;

        //Ciclo entre el primer valor hasta el ultimo del arreglo
        for (int i = 1; i < myArray.Length; i++)
        {
            //Avanzar uno a uno en posiciones del arreglo
            if (myArray[i] == cNum)
            {
                c++;
            }
            else
            {
                if(c > largo)
                {
                    largo = c;
                    largoNum = cNum;
                }
                //Agregar valor al conteo de longitud
                cNum = myArray[i];
                c = 1;
            }
        }

        //Asignar la longitud acorde a la posicion del arreglo
        if(c>largo)
        {
            largo = c;
            largoNum = cNum;
        }

        //Imprimir en pantalla
        Console.WriteLine("Longest: " + largo);
        Console.WriteLine("Number: " + largoNum);
    }
}
//Jonathan Castillo