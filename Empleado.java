package com.ejemplo;

public class Empleado extends Persona{
    
	private String nombre;
    private int sueldoBruto;
    private String trabajo;
	public Empleado(String nombre, int sueldoBruto, String trabajo) {
		super();
		this.nombre = nombre;
		this.sueldoBruto = sueldoBruto;
		this.trabajo = trabajo;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public int getSueldoBruto() {
		return sueldoBruto;
	}
	public void setSueldoBruto(int sueldoBruto) {
		this.sueldoBruto = sueldoBruto;
	}
	public String getTrabajo() {
		return trabajo;
	}
	public void setTrabajo(String trabajo) {
		this.trabajo = trabajo;
	}
	//ejemplo de encapsulamiento
	public String Ficha() {
		return "El empleado " + nombre + " con un sueldo bruto de " + sueldoBruto + " euros trabaja de " + trabajo +"";
	}
	
		
}//cierra clase
