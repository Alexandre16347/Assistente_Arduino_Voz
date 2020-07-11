String nome;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  nome.reserve(200);

  pinMode(3, OUTPUT); //Usando a porta 3 (PWM)
}

void loop() {
  // print the string when a newline arrives:
  nome = coletaDados();

  if (nome.startsWith("lumus") || nome.startsWith("lumos")) {
    analogWrite(3, 50);// toggle
  } 
  if (nome.startsWith("lumus máxima") || nome.startsWith("lumos máxima")) {
    analogWrite(3, 255);// toggle
  } 
  
  if (nome.startsWith("nox")) {
    analogWrite(3, 0);// toggle
  }

  /* if (nome.startsWith("ligar")) {
     digitalWrite(A0, !digitalRead(LED_BUILTIN));// toggle
    }*/
  delay(1000);
  

}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/

String coletaDados() {
  String nome = "";
  while (Serial.available() != 0) {
    nome += (char)Serial.read();
  }
  return nome;
}
