#define voltage_pin A4

void setup() {
  pinMode(voltage_pin, INPUT);
  
  Serial.begin(9600);
}

void loop() {
  static int voltage;

  voltage = analogRead(voltage_pin);

  //Serial.print(voltage);
  //Serial.print("\n");

  Serial.println("#! "+ String(voltage));

  delay(1); //O tempo do delay, em milisegundos, definirá a frequencia de amostragem
}
