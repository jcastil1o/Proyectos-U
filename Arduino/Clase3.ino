int estadoLed = 0;

void setup() 
{
  pinMode(2, OUTPUT);//LED roja
  pinMode(3, OUTPUT);//LED verde
  pinMode(4, OUTPUT);//LED amarilla
  Serial.begin(9600);

}

void loop() 
{
  if (Serial.available()>0)
  {
    //Encender todo
    int estadoMonitor = Serial.read();
    if (estadoMonitor == '1')
    {
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(4, HIGH);
      Serial.println("LED encendido");

    }else if (estadoMonitor == '0')
    {//Apagar todo
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      Serial.println("LED apagado");

    }
    //Encendero rojo
    if (estadoMonitor == '2')
    {
      digitalWrite(2, HIGH);
      Serial.println("LED rojo encendido");
    }else if (estadoMonitor == '3')
    {//Apagar rojo
      digitalWrite(2, LOW);
      Serial.println("LED rojo apagado");
    }
    //Encender verde
    if (estadoMonitor == '4')
    {
      digitalWrite(3, HIGH);
      Serial.println("LED verde encendido");
    }else if (estadoMonitor == '5')
    {
      //Apagar verde
      digitalWrite(3, LOW);
      Serial.println("LED verde apagado");
    }
    //Encender amarillo
    if (estadoMonitor == '6')
    {
      digitalWrite(4, HIGH);
      Serial.println("LED amarillo encendido");
    }else if (estadoMonitor == '7')
    {
      //Apagar amarillo
      digitalWrite(4, LOW);
      Serial.println("LED amarillo apagado");
    }
  }
}
