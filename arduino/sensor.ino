int ledPin = 11; // declaramos el led en el pin 12 del arduino
int sensorPin=7; // declaramos el sensor PIR en el pin 11

int val = 0; //variable para asignar la lectura del sensor PIR

bool sistemaActivo = false;
bool sirenaActiva = false;

void setup()
{
  pinMode(ledPin, OUTPUT); //El pin 12 del arduino lo asignamos como salida para el led
  pinMode(sensorPin, INPUT);//El pin 11 lo asignamos como entrada para la señal del sensor
  Serial.begin(9600);
  for(int i = 0; i > 30; i++) //Utilizamos un for para calibrar el sensor depende del tipo de sensor que utilicemos va a cambiar el tiempo de calibración
  {
    delay(1000);
  }
  delay(50);
}

void loop()
{

  if(sirenaActiva){
    digitalWrite(ledPin, HIGH);
  }else{
    digitalWrite(ledPin, LOW);
  }

  if(sistemaActivo){
    val = digitalRead(sensorPin);
    if (val == HIGH){
      if(!sirenaActiva){
        Serial.print("1");
        sirenaActiva = true;
        digitalWrite(ledPin, HIGH);
      }    
    }
  }

  if(Serial.available()){         //From RPi to Arduino
    char c = Serial.read();
    if (c == 'A'){
      sistemaActivo = true;
      sirenaActiva = false;     
    } else if (c == 'B'){
      sistemaActivo = false;
      sirenaActiva = false;     
    }
  }
   
}