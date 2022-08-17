import java.lang.reflect.Executable;
import java.time.Duration;
import java.util.Scanner;
import java.util.concurrent.TimeoutException;

public class apps {

/**
 * @param args
 * //@throws InterruptedException
 */
public static void main(String args[]) throws InterruptedException{

    Scanner sn = new Scanner(System.in);
    int opcion;

    System.out.println("Bienvenido a mi script");
    Thread.sleep(2000);
    System.out.println("1.- Visual Studio Code");
    System.out.println("2.- Spotify");
    System.out.println("3.- Telegram");
    System.out.println("4.- Python");
    System.out.println("5.- Git");
    System.out.println("0.- Salir del script");
    System.out.println("Esta lista estará en continuo desarrollo y se irán añadiendo nuevas aplicaciones");
    System.out.println("Introduzca el número del programa que desea instalar");
    
    opcion = sn.nextInt();

  switch (opcion){

    case 1:

  System.out.println("Instalando Visual Studio Code");
  Thread.sleep(2000);
  

  }
    
  }  
}
