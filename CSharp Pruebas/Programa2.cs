public class Arreglos
//Clase Arreglos
{
    static int[] myArray = { 1, 2, 1, 3, 3, 1, 2, 1, 5, 1 };
    public static void Main(string[] args)
    //Metodo main
    {
        int[] f = new int[5];
        
        foreach (int num in myArray)
        {
            if(num >= 1 && num <=5)
            {
                f[num - 1]++;
            }
        }

        for (int i = 0; i < f.Length; i++)
        {
            Console.Write((i + 1) + ": ");
            for (int j = 0; j < f[i]; j++)
            {
                Console.Write("*");
            }
            Console.WriteLine();
        }
    }
}