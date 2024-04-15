
/*
  Potenciometro por monitor serial
  PushBottons por monitor serial
  3 LEDs de encendido y apagado
*/
int Monitor = Serial.read();

void setup() 
{
  //LEDs
  pinMode(2, OUTPUT);//verde        PADRE (EL NANO)                     2
  pinMode(3, OUTPUT);//amarillo     HIJO IZQUIERDO                3           4
  pinMode(4, OUTPUT);//rojo         HIJO DERECHO
  //PushBottons
  pinMode(10, INPUT);//PreOrden
  pinMode(11, INPUT);//InOrden
  pinMode(12, INPUT);//PostOrden
  //pin análogo del potenciómetro (A0)

  Serial.begin(9600);
}

void loop() 
{
  int potenciometro = analogRead(A0);
  Serial.println(potenciometro);
  delay(5);

  int PreOrden = digitalRead(10);
  int InOrden = digitalRead(11);
  int PostOrden = digitalRead(12);
  /*
    Programación de los botones
  */
  //PreOrden
  if(PreOrden == HIGH)
  {
    Serial.println("PreOrden");
    delay(1000);
    digitalWrite(2, HIGH);
      delay(1000);
      digitalWrite(3, HIGH);
      delay(1000);
      digitalWrite(4, HIGH);
      delay(1000);
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
  }
    
  //InOrden
  if(InOrden == HIGH)
  {
    Serial.println("InOrden");
    delay(1000);
    digitalWrite(3, HIGH);
      delay(1000);
      digitalWrite(2, HIGH);
      delay(1000);
      digitalWrite(4, HIGH);
      delay(1000);
      digitalWrite(3, LOW);
      digitalWrite(2, LOW);
      digitalWrite(4, LOW);
  }

  //PostOrden
  if(PostOrden == HIGH)
  {
    Serial.println("PostOrden");
    delay(1000);
     digitalWrite(3, HIGH);
      delay(1000);
      digitalWrite(4, HIGH);
      delay(1000);
      digitalWrite(2, HIGH);
      delay(1000);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      digitalWrite(2, LOW);
  }

  if((PreOrden == LOW) && (InOrden == LOW) && (PostOrden == LOW))
  {
    Serial.println(" ");
    delay(1000);
  }
  /*
    Programación de LEDs
  */

  if(Serial.available()>0)
  {
    Monitor = Serial.read();

  /*
              PreOrden
  Árbol:
                2
              /  \
            3      4
  Orden: 2, 3, 4
  */
  if(Monitor == '1')
    {
      digitalWrite(2, HIGH);
      delay(1000);
      digitalWrite(3, HIGH);
      delay(1000);
      digitalWrite(4, HIGH);
      delay(1000);
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
    }

  /*
              InOrden
  Árbol:
                2
              /  \
            3      4
  Orden: 3, 2, 4
  */

    if(Monitor == '2')
    {
      digitalWrite(3, HIGH);
      delay(1000);
      digitalWrite(2, HIGH);
      delay(1000);
      digitalWrite(4, HIGH);
      delay(1000);
      digitalWrite(3, LOW);
      digitalWrite(2, LOW);
      digitalWrite(4, LOW);
    }


  /*
              PostOrden
  Árbol:
                2
              /  \
            3      4
  Orden: 3, 4, 2
  */
      if(Monitor == '3')
    {
      digitalWrite(3, HIGH);
      delay(1000);
      digitalWrite(4, HIGH);
      delay(1000);
      digitalWrite(2, HIGH);
      delay(1000);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      digitalWrite(2, LOW);
    }

    if(Monitor == '0')
    {
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      digitalWrite(2, LOW);
    }
  }
}