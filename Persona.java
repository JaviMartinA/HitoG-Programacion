package com.ejemplo;

public abstract class Persona {
	public String comer () {
        return "Persona comiendo";
    }
	
    public String comer (String lugar){
        return "Persona comiendo en "+lugar;
    }
    //Ejemplo de sobrecarga
}//cierra clase
