int boton = 4;
int led = 3;
int RELE = 2;

void setup() 
{
  pinMode(RELE, OUTPUT);
  pinMode(led, INPUT);
  pinMode(boton, INPUT);

  Serial.begin(9600);
}

void loop() 
{
  boton = digitalRead(4);

  if(Serial.available()>0);
  {
    char monitor = Serial.read();
    if ((monitor == '0') || (boton == LOW))//high
    {
      Serial.println("\tRELE OFF");
      digitalWrite(RELE, HIGH);
      delay(100);
    }else if((monitor == '1') || (boton == HIGH))//low
    {
      Serial.println("\tRELE ON");
      digitalWrite(RELE, LOW);
      delay(100);
    }
  }
  led = digitalRead(3);
  if(led == LOW)
  {
    Serial.println("LED OFF\n");
    delay(1000);
  }
  else
  {
    Serial.println("LED ON\n");
    delay(1000);
  }
}
