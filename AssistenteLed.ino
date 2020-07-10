String nome;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  nome.reserve(200);

  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // print the string when a newline arrives:
  nome = coletaDados();

  Serial.print("Assistente falando: ");
  Serial.println(nome);
  
  if (nome.startsWith("ligar")) {
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));// toggle

  }
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
