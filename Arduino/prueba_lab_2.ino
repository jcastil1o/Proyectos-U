void setup() 
{
  //Grupo 1
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  //Grupo 2
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  //Grupo 3
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  //Grupo 4
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  //Botones
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT);
  Serial.begin(9600);
}

void loop() 
{ 
  /*Mensaje en monitor serial de los push buttons
  */
  int boton1 = digitalRead(10);
  if (boton1 == HIGH)
  {
    Serial.println("Boton A");
    delay(1000);
  }
  int boton2 = digitalRead(11);
  if (boton2 == HIGH)
  {
    Serial.println("Boton B");
    delay(1000);
  }
  int boton3 = digitalRead(12);
  if (boton3 == HIGH)
  {
    Serial.println("Boton C");
    delay(1000);
  }
  int boton4 = digitalRead(13);
  if (boton4 == HIGH)
  {
    Serial.println("Boton D");
    delay(1000);
  }
  /*
    ENTRADA POR MONITOR SERIAL
    INGRESO DE DATOS COMO 1, 2, ... 5 PARA ENCENDIDO O APAGADO
  */
  //Leer entrada de monitor
  if (Serial.available()>0)
  { 
    int Monitor = Serial.read();
    //Grupo 1
    if (Monitor == '1')
    {
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      delay(1000);
      Serial.println("Grupo #1 encendido");
    }else if(Monitor == '0')
      {
        Serial.println("LEDs apagados");
        digitalWrite(2, LOW);
        digitalWrite(3, LOW);
      }
    //Grupo 2
    if (Monitor == '2')
    {
      Serial.println("Grupo #2 encendido");
      digitalWrite(4, HIGH);
      digitalWrite(5, HIGH);
    } else if (Monitor == '0')
      {
        Serial.println("LEDs apagados");
        digitalWrite(4, LOW);
        digitalWrite(5, LOW);
      }
    //Grupo 3
    if (Monitor == '3')
    {
      Serial.println("Grupo #3 encendido");
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      delay(1000);
    }else if(Monitor == '0')
      {
        Serial.println("LEDs apagados");
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
      }
    //Grupo 4
    if (Monitor == '4')
    {
      Serial.println("Grupo #4 encendido");
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
      delay(1000);
    }else if (Monitor == '0')
      {
        Serial.println("LEDs apagados");
        digitalWrite(8, LOW);
        digitalWrite(9, LOW);
      }

    //Apagar y encender todo
    if (Monitor == '5')  
    {
      Serial.println("LEDs encendidos");
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
    }else if (Monitor == '0')
      {
        Serial.println("LEDs apagados");
        digitalWrite(2, LOW);
        digitalWrite(3, LOW);
        digitalWrite(4, LOW);
        digitalWrite(5, LOW);
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
        digitalWrite(8, LOW);
        digitalWrite(9, LOW);
      }
  }  
}